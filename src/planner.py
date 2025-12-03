import json
import time
from src.prompts import SOTA_PLAN_TEMPLATE
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()


def format_context_for_gemini(docs_dict):
    """
    Wraps text in XML tags and injects metadata (author, year).
    docs_dict structure: {
        'file_name.pdf': {
            'id': 'optional_id',
            'chunks': [{'page_number': 1, 'text': '...'}, ...],
            'author': 'Author Name',
            'year': '2023'
        }
    }
    """
    context_string = ""

    for filename, doc_info in docs_dict.items():
        doc_id = doc_info.get("id", filename)
        author = doc_info.get("author", f"Need to find in source document - {filename}")
        year = doc_info.get("year", "n.d.")
        chunks = doc_info.get("chunks", [])

        # Include author and year as attributes for citation
        context_string += f"<source_document id='{doc_id}' author='{author}' year='{year}'>\n"

        for chunk in chunks:
            page_num = chunk.get("page_number", "?")
            text = chunk.get("text", "")
            # Escape XML special chars
            clean_text = text.replace("<", "&lt;").replace(">", "&gt;")
            context_string += f"<page number='{page_num}'>\n{clean_text}\n</page>\n"

        context_string += "</source_document>\n\n"

    return context_string


def generate_plan(client, docs_dict, user_prompt):
    console.print("[bold cyan]Generating Plan...[/bold cyan]")
    
    # Prepare Structured Context
    structured_context = format_context_for_gemini(docs_dict)
    
    # Inject Context into Prompt Template
    final_prompt = SOTA_PLAN_TEMPLATE.replace("{user_prompt}", user_prompt).replace("{context_material}", structured_context)

    # save final prompt for plan generation for debugging in md file
    with open("output/plan_prompt_debug_2.md", "w", encoding="utf-8") as f:
        f.write(final_prompt)

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-lite',
                contents=final_prompt, 
                config={'response_mime_type': 'application/json', 'temperature': 0.2}
            )
            return json.loads(response.text)
        except Exception as e:
            if "429" in str(e):
                console.print(f"[yellow]Resources Exhausted. Waiting 20s...[/yellow]")
                time.sleep(20)
            else:
                console.print(f"[red]Error: {e}[/red]")
                return None
    return None