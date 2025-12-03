import os
import sys
import glob
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from src import ingest, planner, writer
import json

# Load environment variables
load_dotenv()
console = Console()

# API SETUP
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    console.print("[bold red]ERROR: GEMINI_API_KEY missing in .env file[/bold red]")
    sys.exit(1)

# Initialize the Client
client = genai.Client(api_key=API_KEY)

def main():
    console.clear()
    console.rule("[bold magenta] SOTA GENERATOR - PIPELINE [/bold magenta]")
    
    # INPUT HANDLING
    # We accept a Folder (for multiple papers) or a Single File
    path_input = console.input("[bold]Enter path to PDF or Folder of PDFs: [/bold]").strip('"').strip("'")
    if not os.path.exists(path_input):
        console.print(f"[bold red]Path not found: {path_input}[/bold red]")
        return

    # INGESTION
    docs_dict = {}
    try:
        # extract_text_locally returns a list of dict -- > [{"page_number": page_num, "text": text}, ]
        if os.path.isdir(path_input):
            console.print(f"[cyan]Detected Directory. Scanning for PDFs...[/cyan]")
            pdf_files = glob.glob(os.path.join(path_input, "*.pdf"))
            if not pdf_files:
                console.print("[red]No PDFs found in this folder.[/red]")
                return
            for pdf_path in pdf_files:
                filename = os.path.basename(pdf_path)
                console.print(f"   - Ingesting: {filename}...")
                extracted = ingest.extract_text_locally(pdf_path)
                author, year = ingest.extract_pdf_metadata(pdf_path)

                docs_dict[filename] = {
                    "id": filename,     
                    "chunks": extracted,
                    "author": author,
                    "year": year
                }
        else:
            # Single File Case
            if not path_input.lower().endswith('.pdf'):
                console.print("[yellow]Warning: File does not end in .pdf[/yellow]")
            filename = os.path.basename(path_input)
            console.print(f"[cyan]Ingesting Single File: {filename}...[/cyan]")
            extracted = ingest.extract_text_locally(path_input)
            author, year = ingest.extract_pdf_metadata(path_input)
            docs_dict[filename] = {
                "id": filename,     
                "chunks": extracted,
                "author": author,
                "year": year
            }
    except Exception as e:
        console.print(f"[bold red]Ingestion Error: {e}[/bold red]")
        return
    console.print(f"[green]Ingestion Complete. {len(docs_dict)} document(s) loaded.[/green]")

    # PLANNING
    user_prompt = console.input("\n[bold]What is the specific Topic/Angle of this SOTA? [/bold]")
    plan = planner.generate_plan(client, docs_dict, user_prompt)

    # Save plan for user editing
    with open("output/plan_for_user_edit_2.json", "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=4, ensure_ascii=False)

    console.print("\n[bold yellow]Plan has been saved to 'output/plan_for_user_edit_2.json'.[/bold yellow]")
    console.print("[cyan]Please edit this JSON file if needed. Save it when done.[/cyan]")

    console.input("\nPress ENTER once you have finished editing the JSON file...")

    # Load the user-edited JSON plan
    with open("output/plan_for_user_edit_2.json", "r", encoding="utf-8") as f:
        plan = json.load(f)
    console.print("[green]Loaded updated plan successfully![/green]\n")
    
    # WRITING - The Writer needs the docs_dict for RailGuard verification
    final_sota, hallucinations_text = writer.write_full_sota(client, docs_dict, plan)

    # save hallucinations log
    if hallucinations_text:
        with open("output/hallucinations_log.md", "w", encoding="utf-8") as f:
            f.write(hallucinations_text)
        console.print(f"[bold red]Hallucinations log saved to 'output/hallucinations_log.md'[/bold red]")
    
    # print final sota preview
    console.rule("[bold blue] FINAL SOTA PREVIEW [/bold blue]")
    console.print(final_sota[:1000] + "\n...[truncated]...")
    
    # OUTPUT
    os.makedirs("output", exist_ok=True)
    output_filename = "output/final_sota_output_debug_2.md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(final_sota)
        
    console.rule("[bold green] SUCCESS [/bold green]")
    console.print(f"[bold white]Document saved to: {output_filename}[/bold white]")

if __name__ == "__main__":
    main()



