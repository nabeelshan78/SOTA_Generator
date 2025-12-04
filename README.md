# SOTA Generator: Automated Literature Review Pipeline

A state-of-the-art (SOTA) generation engine that ingests raw PDFs, plans a research-grade architecture, and writes a comprehensive literature review.  

**Key Feature:** This system uses a Hybrid RailGuard (Regex + LLM) to strictly enforce citations. It will **not hallucinate sources**; every claim is traced back to the uploaded PDFs.

---

## Quick Start

### 1. Prerequisites
- Python 3.11
- Gemini API Key

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/nabeelshan78/SOTA_Generator.git
cd SOTA_Generator

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 3. Configuration

Add your API key: Inside `.env` file in the root directory

```env
GEMINI_API_KEY="your_actual_api_key_here"

```

- Adjust model settings in src/config.py if you want to switch between models and adjust temperature settings.

## 4. How to Run

The entire pipeline is orchestrated via main.py:

```
python main.py
```

## The Workflow

### Ingestion Phase
- The script asks for a folder path containing your PDFs (default is `input_pdfs/`).
- It ingest the text and builds a `corpus.json` index.

### Planning Phase
- You provide a specific topic (e.g., `"Surgical Interventions"`).
- The AI acts as a Research Architect and generates a JSON plan saved to `output/02_plans/draft_plan.json`.
- **Action:** The script pauses! You can open this JSON file, edit the structure/headings if you want, and save it. Press **Enter** in the console to confirm.

### Writing & Verification Phase
- The AI writes the paper section-by-section using the approved plan.
- **RailGuard Check:** Finally, the system audits the citations.
  1. **Layer 1:** Checks if citations exist in the corpus using strict Regex.
  2. **Layer 2:** On top of Regex, it consults an LLM for strict guardrails and verification.

## Output
The final report is saved in `output/03_final/` as a Markdown file.

# Structure
Plaintext

```
SOTA_Generator/
├── input_pdfs/           # Drop your PDF here
```