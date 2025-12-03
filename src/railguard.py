# src/railguard.py
import re
from rich.console import Console

console = Console()

def extract_keywords(text):
    """
    Simple heuristic to get significant words (ignoring stop words).
    """
    stop_words = {
        'the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of', 'and', 'is', 'are', 
        'was', 'were', 'by', 'with', 'that', 'this', 'it', 'from', 'as', 'be',
        'has', 'have', 'had', 'will', 'would', 'could', 'should'
    }
    # Filter for words > 2 chars to remove noise
    words = re.findall(r'\b\w+\b', text.lower())
    return {w for w in words if w not in stop_words and len(w) > 2}

def verify_citations(generated_text, docs_dict):
    """
    Advanced Verification (Claim-Based Overlap):
    1. Parses citations mapped to specific sentences.
    2. Uses proximity search to locate the correct source file.
    3. Verifies lexical overlap (keywords) between the generated claim and the source file.
    
    Args:
        generated_text (str): The content written by Gemini.
        docs_dict (dict): { 'filename': {'chunks': [{'text': '...'}], 'author': '...', ...} }
    """
    
    # 1. Split text into sentences to isolate claims
    sentences = re.split(r'(?<=[.!?])\s+(?=\S)', generated_text)
    
    # Regex to capture (Author, Year)
    citation_pattern = r'\((?P<author>[A-Za-z\-\s]+)(?: et al)?.*?,?\s*(?P<year>19\d{2}|20\d{2})\)'
    
    verified_count = 0
    total_citations = 0
    hallucinations = []

    # Optimization: Cache tokenized source texts
    source_tokens_cache = {}

    for sentence in sentences:
        matches = re.findall(citation_pattern, sentence)
        
        if not matches:
            continue
            
        for author, year in matches:
            total_citations += 1
            author_clean = author.replace("et al", "").strip().split()[-1]
            
            # --- STEP 1: SOURCE DISCOVERY (Find the file) ---
            found_source_file = None
            source_content = ""
            
            for filename, doc_data in docs_dict.items():
                
                # --- CRITICAL FIX FOR YOUR DATA STRUCTURE ---
                text = ""
                if isinstance(doc_data, dict):
                    raw_chunks = doc_data.get("chunks", [])
                    if isinstance(raw_chunks, list):
                        # FIX: Loop through list of dicts and extract 'text' key
                        text_parts = []
                        for chunk in raw_chunks:
                            if isinstance(chunk, dict):
                                text_parts.append(chunk.get("text", ""))
                            else:
                                text_parts.append(str(chunk)) # Fallback if it's already a string
                        text = " ".join(text_parts)
                    else:
                        text = str(raw_chunks)
                else:
                    text = str(doc_data)

                # Now perform the Regex check on the extracted text
                safe_author = re.escape(author_clean)
                
                # Widen window to 3000 chars to handle PDF formatting issues
                proximity_pattern = f"({safe_author}.{{0,3000}}{year})|({year}.{{0,3000}}{safe_author})"
                
                if re.search(proximity_pattern, text, re.IGNORECASE | re.DOTALL):
                    found_source_file = filename
                    source_content = text
                    break
            
            if not found_source_file:
                hallucinations.append(f"SOURCE NOT FOUND: ({author}, {year}) - Author/Year combo not found in documents.")
                continue

            # --- STEP 2: CLAIM VERIFICATION ---
            claim_keywords = extract_keywords(sentence)
            
            if not claim_keywords:
                verified_count += 1
                continue
            
            # Tokenize source only once per file
            if found_source_file not in source_tokens_cache:
                source_tokens_cache[found_source_file] = set(re.findall(r'\b\w+\b', source_content.lower()))
            
            source_words = source_tokens_cache[found_source_file]
            common_words = claim_keywords.intersection(source_words)
            overlap_ratio = len(common_words) / len(claim_keywords)
            
            if overlap_ratio >= 0.3: # 30% threshold for paraphrasing
                verified_count += 1
            else:
                missing_words = claim_keywords - source_words
                sentence_context = sentence.strip().replace('\n', ' ')[:60] + '...'
                hallucinations.append(f"LOW OVERLAP: ({author}, {year}) in '{found_source_file}'. Claim '{sentence_context}' missing terms: {list(missing_words)[:3]}")

    if total_citations == 0:
        return 100, []

    score = int((verified_count / total_citations) * 100)
    return score, hallucinations