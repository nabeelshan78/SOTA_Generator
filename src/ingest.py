import os
import json
import time
import glob
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict

from google import genai
from google.genai import types
import fitz  # PyMuPDF
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

console = Console()

@dataclass
class ProcessedPaper:
    """Schema for a processed paper in our corpus."""
    file_id: str          # filename without extension
    title: str
    authors: str
    year: str
    page_content: Dict[int, str] # Map of page_num -> text

class IngestionPipeline:
    def __init__(self, input_dir: str = "input_pdfs", output_dir: str = "output/01_extracted"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            console.print("[bold red]ERROR: GEMINI_API_KEY not found in .env[/bold red]")
            raise ValueError("Missing API Key")

        # Initialize the new GenAI Client
        self.client = genai.Client(api_key=self.api_key)
        
        # Ensure output directory if donot exists
        os.makedirs(self.output_dir, exist_ok=True)

    def _extract_local_data(self, pdf_path: str) -> Dict[str, Any]:
        """
        Uses PyMuPDF to extract text page-by-page and basic metadata.
        """
        doc = fitz.open(pdf_path)
        metadata = doc.metadata
        
        # 1. Basic Metadata Extraction
        title = metadata.get("title", "").strip()
        author = metadata.get("author", "").strip()
        creation_date = metadata.get("creationDate", "")
        year = "n.d."
        if creation_date.startswith("D:") and len(creation_date) >= 6:
            year = creation_date[2:6]

        # 2. Text Extraction (Page-level for Traceability)
        extracted_pages = {}
        
        for i, page in enumerate(doc):
            text = page.get_text("text")
            extracted_pages[i + 1] = text # 1-based indexing

        doc.close()

        return {
            "title": title,
            "author": author,
            "year": year,
            "pages": extracted_pages
        }

    def _refine_metadata_with_llm(self, text_sample: str, current_meta: Dict) -> Dict:
        # Only invoke if data looks bad
        if len(current_meta['title']) > 5 and current_meta['author'] and current_meta['year'] != "n.d.":
            return current_meta

        console.print("   [yellow]Metadata incomplete. Refining...[/yellow]")
        
        prompt = f"""
        Extract the Title, valid Author list (e.g. 'Smith et al.'), and Year from this text snippet (first page of a paper).
        Return JSON only: {{ "title": "...", "authors": "...", "year": "..." }}
        
        Text:
        {text_sample[:2000]}
        """

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-lite", # Use Flash for speed/cost
                contents=prompt,
                config=types.GenerateContentConfig(response_mime_type="application/json")
            )
            
            refined = json.loads(response.text)
            
            # Merge: Only overwrite if new value is better
            return {
                "title": refined.get("title") or current_meta["title"] or "Unknown Title",
                "author": refined.get("authors") or current_meta["author"] or "Unknown Authors",
                "year": refined.get("year") or current_meta["year"]
            }
        except Exception as e:
            console.print(f"   [red]Metadata refinement failed: {e}[/red]")
            return current_meta

    def run(self):
        """
        Main execution flow.
        """
        console.rule("[bold cyan]SOTA Pipeline: Ingestion Layer")
        
        pdf_files = glob.glob(os.path.join(self.input_dir, "*.pdf"))
        if not pdf_files:
            console.print(f"[red]No PDFs found in {self.input_dir}[/red]")
            return

        corpus = []

        for pdf_path in track(pdf_files, description="Processing PDFs..."):
            file_id = os.path.splitext(os.path.basename(pdf_path))[0]
            
            # 1. Local Extraction (Fast)
            local_data = self._extract_local_data(pdf_path)
            
            # 2. Metadata Refinement (Smart)
            # Pass the first two page text to help identify the paper
            first_two_pages = (
                local_data["pages"].get(1, "") + "\n\n" + 
                local_data["pages"].get(2, "")
            )
            meta = self._refine_metadata_with_llm(first_two_pages, {
                "title": local_data["title"],
                "author": local_data["author"],
                "year": local_data["year"]
            })

            # 3. Construct Object
            paper = ProcessedPaper(
                file_id=file_id,
                title=meta["title"],
                authors=meta["author"],
                year=meta["year"],
                page_content=local_data["pages"],
            )
            
            corpus.append(asdict(paper))

        # 4. Save Corpus with clear name
        output_path = os.path.join(self.output_dir, "corpus.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(corpus, f, indent=2, ensure_ascii=False)

        console.print(Panel(f"Successfully processed {len(corpus)} papers.\nCorpus saved to: [bold]{output_path}[/bold]", title="Ingestion Complete", style="green"))

if __name__ == "__main__":
    pipeline = IngestionPipeline()
    pipeline.run()