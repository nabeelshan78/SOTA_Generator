import re
import json
from rich.console import Console
from google.genai import types
from src.config import PRIMARY_MODEL, TEMP_VERIFICATION

console = Console()

def verify_with_llm(client, potential_hallucinations, author_index):
    """
    Uses the LLM to double-check citations that Regex flagged.
    This handles typos, formatting variations, or implicit references.
    """
    if not potential_hallucinations:
        return []

    # Prepare context for the LLM
    valid_sources_str = json.dumps(author_index, indent=2)
    
    # We only send the unique unverified citations
    warnings_text = "\n".join(potential_hallucinations)

    prompt = f"""
    You are a Citation Auditor. I have a list of citations from a text that FAILED regex verification against my database.
    
    Your job is to determine if they are:
    1. VALID (Just formatted differently, e.g., "Smith '23" vs "Smith 2023")
    2. INVALID (Hallucinations, wrong year, or authors not in database)

    ### VALID SOURCE DATABASE (JSON):
    {valid_sources_str}

    ### SUSPICIOUS CITATIONS TO CHECK:
    {warnings_text}

    ### INSTRUCTIONS:
    - Return a JSON list of objects: {{ "citation_text": "...", "verdict": "VALID" or "INVALID", "reason": "..." }}
    - Be strict. If the author is completely missing, it is INVALID.
    - If it's a simple typo (e.g. Smyth vs Smith), mark VALID.
    """

    try:
        response = client.models.generate_content(
            model=PRIMARY_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
                temperature=TEMP_VERIFICATION
            )
        )
        
        # Parse output safely
        try:
            audit_results = json.loads(response.text)
        except json.JSONDecodeError:
            return potential_hallucinations
        
        # Filter: Keep only the ones the LLM confirmed are INVALID
        confirmed_hallucinations = []
        for res in audit_results:
            if res.get('verdict') == 'INVALID':
                confirmed_hallucinations.append(f"{res.get('citation_text')} -> {res.get('reason')}")
                
        return confirmed_hallucinations

    except Exception as e:
        console.print(f"[yellow]LLM Verification failed: {e}. Keeping original warnings.[/yellow]")
        return potential_hallucinations

def verify_citations(generated_text, corpus_list, client=None):
    """
    Verifies citations in generated text against the corpus METADATA.
    
    Architecture:
    1. Layer 1 (Regex/Python): Fast, strict matching. Catches 90% of cases.
    2. Layer 2 (LLM Prompt): If Layer 1 flags a citation, 
       and a 'client' is provided, we ask the LLM to verify if it's a hallucination 
       or just a formatting mismatch.
    """
    
    # 1. Map: "Last Name" -> [List of {year: '2023', id: 'file_id'}]
    author_index = {}
    
    for paper in corpus_list:
        p_id = paper.get('file_id', 'unknown')
        
        # Normalize Author Metadata: "Smith, J. and Jones, B." -> ["smith", "jones"]
        raw_authors = paper.get('authors', '').lower()
        
        # Split by common delimiters to handle "Smith, Jones & Lee"
        tokens = re.split(r'[ ,&;]+', raw_authors)
        
        # Filter for valid last names (ignore 'and', 'et', 'al', single letters)
        last_names = {t for t in tokens if len(t) > 2 and t not in ['and', 'the', 'for', 'et', 'al']}
        
        paper_year = str(paper.get('year', '')).strip()
        
        for name in last_names:
            if name not in author_index:
                author_index[name] = []
            author_index[name].append({'year': paper_year, 'id': p_id})

    # 2. Extract Citations from Text
    citation_pattern = r'\((?P<author>[A-Za-z0-9\-\s&\'\.]+?)(?:,?\s*et\s*al\.?)?,?\s*(?P<year>19\d{2}|20\d{2}[a-z]?)\)'
    
    # Split text into sentences for context logging
    sentences = re.split(r'(?<=[.!?])\s+(?=\S)', generated_text)
    
    verified_count = 0
    total_citations_found = 0
    
    # We store full details of "suspects" to send to LLM if needed
    suspect_citations = []

    for sentence in sentences:
        matches = re.findall(citation_pattern, sentence)
        
        for author, year in matches:
            total_citations_found += 1
            
            # Clean Cited Author: "Smith & Jones" -> "Smith", "Jones"
            cited_author_clean = author.lower().replace("et al", "").strip()
            cited_tokens = re.split(r'[ ,&;]+', cited_author_clean)
            cited_names = [t for t in cited_tokens if len(t) > 2]
            
            # Fallback for short names or failures
            if not cited_names:
                cited_names = [cited_author_clean]

            # --- VERIFICATION LOGIC (LAYER 1: REGEX) ---
            match_found = False
            
            # If ANY of the cited names matches an uploaded paper's author AND year, it's valid.
            for name in cited_names:
                if name in author_index:
                    candidates = author_index[name]
                    for cand in candidates:
                        # Fuzzy Year Match (allow "2020a" to match "2020")
                        if year in cand['year'] or cand['year'] in year:
                            match_found = True
                            break
                if match_found:
                    break
            
            if match_found:
                verified_count += 1
            else:
                # Store as suspect for Layer 2
                context_snippet = sentence.strip().replace('\n', ' ') + "..."
                suspect_msg = f"({author}, {year}) in context: \"{context_snippet}\""
                suspect_citations.append(suspect_msg)

    # --- VERIFICATION LOGIC (LAYER 2: LLM) ---
    final_hallucinations = []
    
    if suspect_citations:
        if client:
            console.print(f"[yellow]Regex flagged {len(suspect_citations)} potential hallucinations. Consulting LLM Judge...[/yellow]")
            # The LLM returns ONLY the confirmed invalid ones
            confirmed_invalids = verify_with_llm(client, suspect_citations, author_index)
            
            # Calculate how many were "saved" by the LLM
            saved_count = len(suspect_citations) - len(confirmed_invalids)
            verified_count += saved_count
            final_hallucinations = confirmed_invalids
            
            if saved_count > 0:
                console.print(f"[green]LLM cleared {saved_count} false positives.[/green]")
        else:
            # If no client provided, we must accept Regex's verdict
            final_hallucinations = [f"UNVERIFIED (Regex): {s}" for s in suspect_citations]

    if total_citations_found == 0:
        return 100, []

    score = round((verified_count / total_citations_found) * 100, 1)
    return score, final_hallucinations