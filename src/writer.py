# src/writer.py
import time
from src.railguard import verify_citations
from rich.console import Console
import src.planner as planner
from src.prompts import ONE_SHOT_MASTER_PROMPT

console = Console()


def generate_with_retry(client, model_name, contents, config=None):
    """
    Robust generation
    Args:
        config (dict): Optional. Pass {'response_mime_type': 'application/json'} for JSON mode.
    """
    max_retries = 5
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model=model_name,
                contents=contents,
                config=config
            )
        except Exception as e:
            if "429" in str(e):
                console.print(f"[yellow]Resources Exhausted. Waiting 20s... (Attempt {attempt+1})[/yellow]")
                time.sleep(20)
            else:
                console.print(f"[red]Generation Error: {e}[/red]")
                return None
                
    console.print("[red]Failed after max retries.[/red]")
    return None


# --- MAIN FUNCTION ---

def write_full_sota(client, docs_dict, plan_json):
    # Pre-format context once
    structured_context = planner.format_context_for_gemini(docs_dict)
    
    console.rule("[bold red] WRITING (ONE-SHOT GENERATION) [/bold red]")
    
    # Initialize the final document
    full_document = f"# {plan_json.get('title', 'SOTA Review')}\n\n"
    
    # Construct the prompt
    plan_instruction = ""
    
    for i, section in enumerate(plan_json.get('sections', [])):
        s_title = section['section_title']
        k_points = section['key_points']
        target_sources = section.get('mapped_sources', [])
        
        plan_instruction += f"\n### SECTION {i+1}: {s_title}\n"
        plan_instruction += f"Goals: {k_points}\n"

        formatted_sources = [
            f"{f['id']} ({f.get('author','Unknown')}, {f.get('year','n.d.')})"
            for f in target_sources
        ]
        plan_instruction += f"Mapped Sources: {formatted_sources}\n"
    
    # Construct the final prompt, ONE_SHOT_MASTER_PROMPT expects {global_plan_instruction} and {structured_context}
    final_prompt = ONE_SHOT_MASTER_PROMPT.format(
        global_plan_instruction=plan_instruction,
        structured_context=structured_context
    )

    # save final sota prompt for debugging in md file
    with open("output/final_sota_prompt_debug_2.md", "w", encoding="utf-8") as f:
        f.write(final_prompt)

    try:
        response = generate_with_retry(
            client, 
            'gemini-2.0-flash-lite',
            contents=[final_prompt]
        )
        if response and response.text:
            generated_content = response.text
        else:
            generated_content = "> *[Error: Empty response from model]*"
    except Exception as e:
        console.print(f"[red]CRITICAL FAILURE in One-Shot Generation: {e}[/red]")
        generated_content = f"> *[System Error: Could not generate the document]*"

    # RailGuard (Verification), We pass the full docs_dict to the RailGuard
    score, hallucinations = verify_citations(generated_content, docs_dict)

    hallucinations_text = ""    
    if score < 100:
        console.print(f"[bold red]RailGuard Alert: {len(hallucinations)} unverified citations. (Score: {score:.1f}%)[/bold red]")
        # Append Warning directly to the text
        hallucinations_text += "\n\n> **Citation Warning:** The following citations could not be grounded in the source text:\n"
        for h in hallucinations:
            hallucinations_text += f"> * {h}\n"
    else:
        console.print(f"[bold green]Citations Verified (100%)[/bold green]")
        
    return generated_content, hallucinations_text