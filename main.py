import os
import sys
import json
import time
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

# Import our modular classes
from src.ingest import IngestionPipeline
from src.planner import SOTAPlanner
from src.writer import SOTAWriter

# Load environment variables
load_dotenv()
console = Console()

def check_setup():
    """Verifies API keys and directory structure."""
    if not os.getenv("GEMINI_API_KEY"):
        console.print("[bold red]ERROR: GEMINI_API_KEY missing in .env file[/bold red]")
        sys.exit(1)
    
    # Ensure standard paths exist
    os.makedirs("input_pdfs", exist_ok=True)
    os.makedirs("output/01_extracted", exist_ok=True)
    os.makedirs("output/02_plans", exist_ok=True)
    os.makedirs("output/03_final", exist_ok=True)

def main():
    console.clear()
    console.rule("[bold magenta] SOTA GENERATOR - RESEARCH PIPELINE [/bold magenta]")
    
    check_setup()

    # --- PHASE 1: INGESTION ---
    # We allow the user to specify a custom folder, or default to 'input_pdfs'
    path_input = console.input("\n[bold]Enter path to PDF folder (press Enter for default 'input_pdfs'): [/bold]").strip()
    if not path_input:
        path_input = "input_pdfs"
    
    if not os.path.exists(path_input):
        console.print(f"[bold red]Path not found: {path_input}[/bold red]")
        return

    # Initialize and run Ingestion - this will create 'output/01_extracted/corpus.json'
    ingestor = IngestionPipeline(input_dir=path_input, output_dir="output/01_extracted")
    ingestor.run()


    # --- PHASE 2: PLANNING ---
    console.rule("[bold cyan] PHASE 2: ARCHITECTURE [/bold cyan]")
    
    user_topic = console.input("\n[bold]What is the specific Topic/Angle of this SOTA? [/bold]")
    if not user_topic:
        console.print("[red]Topic is required.[/red]")
        return

    planner = SOTAPlanner(corpus_path="output/01_extracted/corpus.json", output_dir="output/02_plans")
    plan = planner.generate_plan(user_topic)

    if not plan:
        console.print("[bold red]Planning failed. Aborting.[/bold red]")
        return

    # User Review Loop
    plan_path = os.path.join("output/02_plans", "draft_plan.json")
    console.print(f"\n[bold yellow]ACTION REQUIRED:[/bold yellow] A draft plan has been saved to '{plan_path}'.")
    console.print("[dim]Please open this JSON file, edit the structure if needed, and save it.[/dim]")
    
    console.input("\n[bold reverse] Press ENTER once you have finished editing the Plan... [/bold reverse]")

    # Reload the plan to get user edits
    try:
        with open(plan_path, "r", encoding="utf-8") as f:
            plan = json.load(f)
        console.print("[green]Updated plan loaded successfully![/green]")
    except Exception as e:
        console.print(f"[bold red]Error loading updated plan: {e}[/bold red]")
        return


    # --- PHASE 3: WRITING & GUARDRAILS ---
    console.rule("[bold green] PHASE 3: PRODUCTION [/bold green]")
    
    writer = SOTAWriter(corpus_path="output/01_extracted/corpus.json", output_dir="output/03_final")
    
    # This method handles writing AND calls the RailGuard internally
    final_output_path = writer.write_sota(plan)

    if final_output_path:
        console.print(Panel(f"Process Complete.\nFinal SOTA: [bold]{final_output_path}[/bold]", style="bold green"))
    else:
        console.print("[bold red]Writing process failed.[/bold red]")

if __name__ == "__main__":
    main()