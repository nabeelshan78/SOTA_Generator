import os
import json
import time
import re
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.prompts import ONE_SHOT_MASTER_PROMPT
from src.config import PRIMARY_MODEL, TEMP_WRITING

# Import the RailGuard verification logic
from src.railguard import verify_citations

load_dotenv()
console = Console()

class SOTAWriter:
    def __init__(self, corpus_path: str, output_dir: str):
        self.corpus_path = corpus_path
        self.output_dir = output_dir
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")
            
        self.client = genai.Client(api_key=self.api_key)
        os.makedirs(self.output_dir, exist_ok=True)

    def load_corpus(self):
        with open(self.corpus_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _clean_text_for_xml(self, text):
        """Sanitize text for prompt injection."""
        if text is None:
            return ""
        text = str(text)
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        return text
    
    def _format_context(self, corpus) -> str:
        context_string = ""
        console.print(f"[dim]Formatting {len(corpus)} papers for context injection...[/dim]")

        for paper in corpus:
            # Extract metadata safely
            p_id = paper.get('file_id', 'unknown')
            p_title = self._clean_text_for_xml(paper.get('title', 'Unknown Title'))
            p_auth = self._clean_text_for_xml(paper.get('authors', 'Unknown'))
            p_year = self._clean_text_for_xml(paper.get('year', 'n.d.'))
            
            # Reconstruct full text from page dict
            # We sort keys to ensure pages appear in order (1, 2, 3...)
            pages = paper.get('page_content', {})
            sorted_page_nums = sorted(pages.keys(), key=lambda x: int(x) if str(x).isdigit() else 0)
            
            full_text = ""
            for num in sorted_page_nums:
                full_text += pages[num] + "\n"
            
            clean_body = self._clean_text_for_xml(full_text)

            # Structure: <paper> tags act as the "RailGuard" boundaries
            context_string += f"""
<paper id="{p_id}">
    <metadata title="{p_title}" author="{p_auth}" year="{p_year}" />
    <full_text>
    {clean_body}
    </full_text>
</paper>
"""
        return context_string

    def _format_plan_instructions(self, plan_json):
        """Converts the JSON plan into natural language instructions."""
        instructions = ""
        sections = plan_json.get('sections', [])
        
        for section in sections:
            heading = section.get('heading', 'Untitled Section')
            instructions += f"\n## SECTION: {heading}\n"
            
            # Handle recursive subsections (Uniformity Rule)
            subsections = section.get('subsections', [])
            for sub in subsections:
                sub_head = sub.get('sub_heading')
                goal = sub.get('content_goal', '')
                points = sub.get('key_points', [])
                sources = sub.get('mapped_sources', [])
                
                if sub_head:
                    instructions += f"   - Sub-topic: {sub_head}\n"
                
                instructions += f"   - Goal: {goal}\n"
                instructions += f"   - Key Points to cover: {'; '.join(points)}\n"
                
                # Explicitly tell the model which sources to use for this paragraph
                source_list = [f"{s.get('id')} ({s.get('author')}, {s.get('year')})" for s in sources]
                instructions += f"   - REQUIRED CITATIONS for this part: {', '.join(source_list)}\n"
        
        return instructions

    def write_sota(self, plan_json):
        console.print("[bold cyan]Initializing Writer Engine...[/bold cyan]")
        
        # 1. Prepare Data
        corpus = self.load_corpus()
        context_str = self._format_context(corpus)
        plan_str = self._format_plan_instructions(plan_json)
        
        # 2. Build Prompt
        final_prompt = ONE_SHOT_MASTER_PROMPT.format(
            structured_context=context_str,
            global_plan_instruction=plan_str
        )
        
        # Debug Prompt
        with open(os.path.join(self.output_dir, "debug_writer_prompt.txt"), "w", encoding="utf-8") as f:
            f.write(final_prompt)

        # 3. Generate
        console.print("[bold green]Generating Full SOTA Review...[/bold green]")
        
        try:
            # High token limit for long output
            response = self.client.models.generate_content(
                model=PRIMARY_MODEL,
                contents=final_prompt,
                config=types.GenerateContentConfig(temperature=TEMP_WRITING)
            )
            
            content = response.text
            
            # 4. RailGuard Check
            console.rule("[bold red] RAILGUARD VERIFICATION [/bold red]")
            score, hallucinations = verify_citations(content, corpus, client=self.client)
            
            # Append Audit Report to the document
            audit_report = "\n\n---\n## RailGuard Audit Report\n"
            audit_report += f"**Verification Score:** {score}/100\n\n"
            
            if hallucinations:
                console.print(f"[bold red]Found {len(hallucinations)} unverified citations![/bold red]")
                audit_report += "**Unverified Citations (Potential Hallucinations):**\n"
                for h in hallucinations:
                    audit_report += f"- {h}\n"
            else:
                console.print("[bold green]PASS: All citations verified against source text.[/bold green]")
                console.print(f"[bold green]Verification Score: {score}/100[/bold green]")
                audit_report += "All citations successfully verified against uploaded PDFs."
            
            final_content = content + audit_report

            # 5. Save
            filename = f"SOTA_Review_{int(time.time())}.md"
            out_path = os.path.join(self.output_dir, filename)
            
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(final_content)
                
            return out_path

        except Exception as e:
            console.print(f"[red]Writing failed: {e}[/red]")
            return None