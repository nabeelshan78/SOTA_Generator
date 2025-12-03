# src/ingest.py
# pip install google-genai

# src/ingest.py
# pip install google-genai

# src/ingest.py
import time
from google import genai
from rich.console import Console
import fitz  # PyMuPDF
import os

console = Console()

def upload_to_gemini(client, pdf_path):
    """
    Uploads file using the Client.
    """
    console.print(f"[cyan]Uploading {pdf_path} to Gemini...[/cyan]")
    
    # SDK Upload
    myfile = client.files.upload(file=pdf_path)
    
    # Wait for processing
    console.print("[yellow]Waiting for processing...[/yellow]")
    while myfile.state.name == "PROCESSING":
        time.sleep(2)
        myfile = client.files.get(name=myfile.name)
        
    if myfile.state.name != "ACTIVE":
        raise Exception(f"File processing failed: {myfile.state.name}")
        
    console.print(f"[green]File Ready! Name: {myfile.name}[/green]")
    return myfile



def extract_pdf_metadata(pdf_path):
    doc = fitz.open(pdf_path)
    metadata = doc.metadata
    
    # Extract author(s)
    author = metadata.get("author", "").strip()
    if not author:
        author = f"Need to find in source document - {os.path.basename(pdf_path)}"  # fallback
    
    # Extract year
    creation_date = metadata.get("creationDate", "")
    year = "n.d."  # default if missing
    if creation_date.startswith("D:") and len(creation_date) >= 6:
        year = creation_date[2:6]  # D:YYYYMMDDHHmmSS
    
    return author, year


def extract_text_locally(pdf_path):
    doc = fitz.open(pdf_path)

    extracted = []  # list of chunks with metadata

    for page_index, page in enumerate(doc):
        page_num = page_index + 1
        text = page.get_text("text")

        extracted.append({
            "page_number": page_num,
            "text": text
        })

    doc.close()
    return extracted