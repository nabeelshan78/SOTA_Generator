import os
import json
import time
from typing import List, Dict, Any, Optional

import json_repair
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.config import PRIMARY_MODEL, TEMP_PLANNING

# Load environment variables
load_dotenv()

console = Console()

# Import the template
try:
    from src.prompts import SOTA_PLAN_TEMPLATE
except ImportError:
    console.print("[bold red]CRITICAL: src/prompts.py not found.[/bold red]")
    SOTA_PLAN_TEMPLATE = "ERROR: Missing Template. Context: {context_material} User Prompt: {topic}"

class SOTAPlanner:
    def __init__(self, corpus_path: str = "output/01_extracted/corpus.json", output_dir: str = "output/02_plans"):
        """
        Initialize the Planner.
        
        Args:
            corpus_path: Path to the JSON file created by ingest.py
            output_dir: Where to save the generated plans
        """
        self.corpus_path = corpus_path
        self.output_dir = output_dir
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")
            
        self.client = genai.Client(api_key=self.api_key)
            
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            console.print(f"[dim]Created output directory: {self.output_dir}[/dim]")

    def load_corpus(self) -> List[Dict]:
        """Loads the processed corpus from step 1 (ingest.py)."""
        if not os.path.exists(self.corpus_path):
            console.print(f"[bold red]Corpus not found at {self.corpus_path}.[/bold red]")
            console.print("[yellow]Please run 'python main.py' or 'src/ingest.py' first.[/yellow]")
            return []
        
        try:
            with open(self.corpus_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError:
            console.print(f"[bold red]Error decoding {self.corpus_path}. File might be corrupt.[/bold red]")
            return []

    def _clean_text_for_xml(self, text: Any) -> str:
        """
        Sanitizes text to ensure it doesn't break the XML structure injected into the prompt.
        """
        if text is None:
            return ""
        
        text = str(text)
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        
        return text

    def _format_context_for_gemini(self, corpus: List[Dict]) -> str:
        """
        Converts the corpus list into a structured XML string.
        We inject the FULL TEXT of each paper within <paper> tags. this allows the planner to see the specific methodology and results sections.
        """
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

    def generate_plan(self, topic: str) -> Optional[Dict]:
        """
        Orchestrates the planning process:
        1. Loads context
        2. Formats prompt
        3. Calls LLM
        4. Saves output
        """
        console.rule("[bold cyan]SOTA Pipeline: Planning Layer")
        
        # 1. Load Data
        corpus = self.load_corpus()
        if not corpus:
            return None
        
        console.print(f"[dim]Loaded {len(corpus)} papers. Preparing Prompt...[/dim]")

        # 2. Prepare Context
        context_str = self._format_context_for_gemini(corpus)
        
        # 3. Construct Prompt
        final_prompt = SOTA_PLAN_TEMPLATE.replace("{topic}", topic).replace("{context_material}", context_str)
        
        # DEBUG: Save prompt to file (useful for inspecting what we sent to the LLM)
        debug_path = os.path.join(self.output_dir, "debug_plan_prompt.txt")
        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(final_prompt)
        console.print(f"[dim]Debug: Full prompt saved to {debug_path}[/dim]")

        # 4. Call Gemini
        console.print(f"[bold green]Generating Plan (Gemini)...[/bold green]")
        
        # Retry logic for robustness
        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=PRIMARY_MODEL,
                    contents=final_prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type='application/json',
                        temperature=TEMP_PLANNING
                    )
                )
                
                # 5. Parse & Validate
                plan_json = json_repair.loads(response.text)
                
                # Basic validation to ensure the LLM followed the schema
                if "sections" not in plan_json:
                    raise ValueError("Invalid Plan: Missing 'sections' key in JSON response")
                if "title" not in plan_json:
                    plan_json["title"] = f"SOTA Review: {topic}" # Fallback

                # 6. Save Plan
                output_file = os.path.join(self.output_dir, "draft_plan.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(plan_json, f, indent=2)
                
                console.print(Panel(f"Plan generated successfully!\nFile: [bold]{output_file}[/bold]", title="Success", style="green"))
                
                return plan_json

            except Exception as e:
                console.print(f"[yellow]Attempt {attempt+1} failed: {str(e)}[/yellow]")
                if "429" in str(e): # Resource Exhausted
                    console.print("[red]Rate limit hit. Waiting 20s...[/red]")
                    time.sleep(20)
                else:
                    time.sleep(2)
        
        console.print("[bold red]Failed to generate plan after 3 attempts.[/bold red]")
        return None