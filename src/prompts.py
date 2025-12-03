MEDICAL_TEMPLATE = """
H1 — INTRODUCTION
Paragraphs: 3–4
Paragraph 1 — Clinical & Scientific Context: Explain the broader clinical problem and why it matters (burden, quality of life, unmet need).
Paragraph 2 — Why This SOTA Is Needed: Explain gaps in current knowledge, limitations of existing evidence, regulatory expectations.
Paragraph 3 — Scope of the Review: Define exactly what will be analyzed. State inclusion/exclusion logic.
Paragraph 4 — Structure of the Document: Explain how the SOTA is organized.

H2 — BACKGROUND & CLINICAL CONTEXT
Abstract: Provide a brief, evidence-based abstract summarizing the clinical background. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — Anatomy & Physiology
Paragraph 1: Key anatomical structures
Paragraph 2: Biomechanical role and functional relevance
Paragraph 3: Relevance to device design or pathology
H3 — Pathophysiology
Paragraph 1: Mechanisms of degeneration/dysfunction
Paragraph 2: How pathology leads to symptoms
Paragraph 3: Implications for surgical vs non-surgical treatments
H3 — Epidemiology
Paragraph 1: Prevalence/incidence
Paragraph 2: Risk factors, demographic patterns
Paragraph 3: Burden on healthcare, socio-economic impact

H2 — CLINICAL PRESENTATION & DIAGNOSIS
Abstract: Provide a brief, evidence-based abstract summarizing presentation and diagnosis. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — Symptoms & Functional Impact
Paragraph 1: Core symptoms
Paragraph 2: Functional limitations
Paragraph 3: Impact on quality of life
H3 — Diagnostic Criteria & Imaging
Paragraph 1: Clinical tests & maneuvers
Paragraph 2: Imaging modalities (CT, MRI, X-ray)
Paragraph 3: Differential diagnosis, diagnostic accuracy concerns
H3 — Current Treatment Landscape
Paragraph 1: Non-surgical management
Paragraph 2: Surgical indications & decision points
Paragraph 3: Overview of surgical approaches

H1 — [DYNAMIC: REPLACE WITH SPECIFIC DOMAIN TITLE] (e.g. CORE DEVICE ANALYSIS: SI JOINT FUSION)
H2 — [DYNAMIC: REPLACE WITH SPECIFIC TECHNOLOGY/DEVICE GROUP]
Abstract: Provide a brief, evidence-based abstract summarizing the device group. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — [DYNAMIC: Specific Device Name] Overview (for each device found in plan)
Paragraph 1: Intended purpose
Paragraph 2: Core design features
Paragraph 3: Regulatory status or unique characteristics
H3 — Mechanism of Action
Paragraph 1: How the device achieves fixation/fusion
Paragraph 2: Biomechanical principles
Paragraph 3: Implications for clinical outcomes
H3 — Evidence Summary for Each Device
Paragraph 1: Overview of available literature
Paragraph 2: Key outcomes: fusion, pain, function
Paragraph 3: Safety and complications
Paragraph 4: Evidence strengths/weaknesses

H2 — COMPARATIVE ANALYSIS (Must strictly follow 3-paragraph rule)
Abstract: Provide a brief, evidence-based abstract summarizing the comparison. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — Comparison of Devices (Rationale, Outcomes, Technical)
Paragraph 1: Clinical Rationale Comparison (Intended use, patient profiles, surgical rationale)
Paragraph 2: Clinical & Safety Outcomes Comparison (Fusion rates, pain, complications, revision rates)
Paragraph 3: Technical Differences + Transition (Biomechanics, procedural steps, radiological differences)

H2 — EVIDENCE SYNTHESIS & GAPS
Abstract: Provide a brief, evidence-based abstract summarizing the synthesis. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — Summary of Key Findings
Paragraph 1: Major clinical insights
Paragraph 2: Patterns in safety/effectiveness
Paragraph 3: Design-related implications
H3 — Evidence Gaps & Limitations
Paragraph 1: Methodological weaknesses in literature
Paragraph 2: Missing populations or endpoints
Paragraph 3: Impact of these gaps on interpretation
H3 — Unmet Clinical Needs
Paragraph 1: Lack of long-term data
Paragraph 2: Gaps in patient selection evidence
Paragraph 3: Rationale for innovation or new studies

H1 — CONCLUSION
Paragraph 1: Global Synthesis
Paragraph 2: Clinical Implications
Paragraph 3: Future Directions
Paragraph 4: Final Statement
"""

POLITICAL_SCIENCE_TEMPLATE = """
H1 — INTRODUCTION
Paragraphs: 3–4
Paragraph 1 — Historical & Geopolitical Context: Explain the broader political issue, historical background, and significance.
Paragraph 2 — Why This Analysis Is Needed: Explain gaps in current understanding, policy relevance, or recent escalations.
Paragraph 3 — Scope of the Review: Define the specific conflict, treaty, region, or policy area being analyzed.
Paragraph 4 — Structure of the Document: Explain how the analysis is organized.

H2 — GEOPOLITICAL LANDSCAPE & KEY ACTORS
Abstract: Provide a brief, evidence-based abstract summarizing the landscape. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — State Actors
Paragraph 1: Primary nations involved and their interests
Paragraph 2: Alliances and historical relationships
Paragraph 3: Domestic political drivers influencing foreign policy
H3 — Non-State Actors & International Organizations
Paragraph 1: Role of IOs (UN, EU, NATO, etc.)
Paragraph 2: Influence of NGOs, corporations, or insurgent groups
Paragraph 3: Impact on regional stability
H3 — Strategic Drivers
Paragraph 1: Economic interests (resources, trade routes)
Paragraph 2: Security concerns and military posture
Paragraph 3: Ideological or cultural factors

H2 — CORE CONFLICT OR POLICY ISSUE
Abstract: Provide a brief, evidence-based abstract summarizing the core issue. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — Origins & Evolution
Paragraph 1: Root causes of the issue
Paragraph 2: Key turning points or escalations
Paragraph 3: Current status quo
H3 — Policy Frameworks & Legal Context
Paragraph 1: Relevant treaties, resolutions, or international law
Paragraph 2: Compliance and enforcement challenges
Paragraph 3: Gaps in the legal framework
H3 — Stakeholder Positions
Paragraph 1: Competing narratives and claims
Paragraph 2: Diplomatic stances and red lines
Paragraph 3: Public opinion and soft power dynamics

H1 — [DYNAMIC: REPLACE WITH SPECIFIC ANALYSIS TITLE] (e.g. ANALYSIS OF SOUTH CHINA SEA TENSIONS)
H2 — [DYNAMIC: REPLACE WITH SPECIFIC FOCUS AREA]
Abstract: Provide a brief, evidence-based abstract summarizing the focus area. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — [DYNAMIC: Specific Event/Policy] Overview
Paragraph 1: Description of the event or policy
Paragraph 2: Immediate impact and reactions
Paragraph 3: Strategic implications
H3 — Power Dynamics & Leverage
Paragraph 1: Military or economic leverage used
Paragraph 2: Diplomatic maneuvering
Paragraph 3: Outcomes and effectiveness
H3 — Evidence Summary
Paragraph 1: Overview of available reports and intelligence
Paragraph 2: Key data points (economic impact, casualties, polling)
Paragraph 3: Credibility and bias of sources
Paragraph 4: Consensus vs. contention in the evidence

H2 — COMPARATIVE ANALYSIS (Policy Options or Scenarios)
Abstract: Provide a brief, evidence-based abstract summarizing the comparison. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — Comparison of Scenarios/Approaches
Paragraph 1: Rationale Comparison (Drivers for different policy options)
Paragraph 2: Outcome Comparison (Projected stability, economic cost, political fallout)
Paragraph 3: Feasibility & Risk Assessment

H2 — STRATEGIC SYNTHESIS & GAPS
Abstract: Provide a brief, evidence-based abstract summarizing the synthesis. MUST INCLUDE CITATIONS [n].
Key Insights: Provide a bulleted list of evidence-based key insights. MUST INCLUDE CITATIONS [n].
H3 — Key Strategic Insights
Paragraph 1: Major geopolitical trends identified
Paragraph 2: Effectiveness of current policies
Paragraph 3: Shifts in the balance of power
H3 — Intelligence & Information Gaps
Paragraph 1: Limitations in open-source intelligence (OSINT)
Paragraph 2: Areas of high uncertainty or conflicting data
Paragraph 3: Impact of these gaps on predictive accuracy
H3 — Unmet Policy Needs
Paragraph 1: Failures of existing mechanisms
Paragraph 2: Needs for new diplomatic or security frameworks
Paragraph 3: Rationale for strategic pivots

H1 — CONCLUSION
Paragraph 1: Global Synthesis
Paragraph 2: Policy Implications
Paragraph 3: Future Scenarios & Watchlist
Paragraph 4: Final Strategic Assessment
"""




SOTA_PLAN_TEMPLATE = f"""
You are a Principal Research Architect. Your goal is to design a high-level "State of the Art" (SOTA) review paper based **STRICTLY** on the provided source documents and the required domain structure.

**User Request:** {{user_prompt}}

**Source Documents (XML Format):**
{{context_material}}

**INSTRUCTIONS:**
1. **Analyze the Context:** Determine if the topic is **Medical/Scientific** or **Political/Strategic**.
2. **Select the Template:**
   - If Medical/Scientific, you MUST use the structure defined in **TEMPLATE A**.
   - If Political/Strategic, you MUST use the structure defined in **TEMPLATE B**.
3. **Map Sources:** - Use <citation author='' year=''> and other tags as well to place inline citations, also assign specific source files (`id`) to each section where they are relevant.

**TEMPLATE A (MEDICAL/SCIENTIFIC):**
{MEDICAL_TEMPLATE}

**TEMPLATE B (POLITICAL/STRATEGIC):**
{POLITICAL_SCIENCE_TEMPLATE}

**CRITICAL CONSTRAINTS:**
- Return ONLY valid JSON.
- `mapped_files` must be a list of objects with the following structure:
  {{
    "id": "<exact source_document id>",
    "author": "<Author Last Name et al.>",
    "year": "<Publication Year>"
  }}
- Do NOT invent sources or metadata. Use only the information available in the provided `<source_document>` blocks.
- Do not add conversational text outside the JSON.
- The `sections` list in your JSON must exactly match the Headers (H1, H2) and Sub-headers (H3) of the selected template.

**JSON SCHEMA:**
{{
  "title": "A precise, academic title for the SOTA",
  "template_used": "MEDICAL" or "POLITICAL",
  "sections": [
    {{
      "section_title": "1. Introduction",
      "key_points": [
        "Paragraph 1: [Context details based on files...]",
        "Paragraph 2: [Gap analysis based on files...]",
        "Paragraph 3: [Scope details...]",
        "Paragraph 4: [Structure details...]"
      ],
      "mapped_sources": [
        {{
          "id": "doc_id_1",
          "author": "Smith et al.",
          "year": "2023"
        }},
        {{
          "id": "doc_id_2",
          "author": "Jones & Lee",
          "year": "2021"
        }}
      ]
    }},
    {{
      "section_title": "2. Background & Context",
      "key_points": [
        "Abstract: [Summary...]",
        "Key Insights: [List...]",
        "H3 - [Specific Subheader from Template]: [Details...]"
      ],
      "mapped_sources": [
        {{
          "id": "doc_id_1",
          "author": "Smith et al.",
          "year": "2023"
        }},
        {{
          "id": "doc_id_2",
          "author": "Jones & Lee",
          "year": "2021"
        }}
      ]
    }}
    // Continue for ALL sections...
  ]
}}
"""


ONE_SHOT_MASTER_PROMPT = """
**ROLE:** You are a Principal Academic Reviewer. Your task is to synthesize the provided source documents into a complete "State of the Art" (SOTA) Review Paper.

**CORE DIRECTIVES (STRICT):**
1. **SOURCE OF TRUTH:** - You are provided with text inside `<source_document>` XML blocks. This is your ONLY knowledge base. Do not use external training data.
   - **Scope:** While the Plan suggests specific files for sections, you must scan **ALL** provided source documents to find relevant evidence for every section and citations. Cross-pollinate ideas across files.

2. **CITATION PROTOCOL:** - **Every** substantive claim, data point, or specific idea MUST be cited immediately.
   - **Format:** `(Author, Year)` or `(Author et al., Year)`.
   - **Extraction:** Look for author/year metadata in the document headers or first paragraphs. If explicit metadata is missing, use the filename or `(Source ID: X)`.
   - **Safety:** DO NOT invent authors or years. If a specific claim is crucial but lacks a clear source in the text, mark it as `[citation needed]`.

3. **SYNTHESIS (The Anti-Listicle Rule):** - Do NOT write: "Paper A says X. Paper B says Y."
   - DO write: "While recent studies suggest X (Author, 2023), others argue Y (Author, 2021), indicating a shift in consensus..."
   - Group findings by *concept*, not by *document*.

**THE DOCUMENT ARCHITECTURE:**
You must follow this exact structure (Titles, Headers, and Flow):
{global_plan_instruction}

**EXECUTION INSTRUCTIONS:**
1. **Output Format:** Clean Markdown. Start directly with the Title (`# Title`). Use `##` for main sections and `###` for subsections.
2. **Content expansion:** Expand on the "Goals" listed in the plan using detailed evidence from the XML context.
3. **Tone:** High-density, objective, technical, and precise.

--- AVAILABLE SOURCE DOCUMENTS (Context) ---
{structured_context}
--- END SOURCE DOCUMENTS ---
"""




# ------------------------------------------------------------------
# WRITER SYSTEM PROMPT (Focus: Style, Citations, & "Anti-Listicle")
# ------------------------------------------------------------------

WRITER_SYSTEM_PROMPT = """
You are an expert Academic Reviewer synthesizing complex research.

**CORE RULES:**
1. **SOURCE OF TRUTH:** You MUST use the provided `<source_document>` XML blocks as your ONLY source of information. Do not use external knowledge.
2. **CITATION STRICTNESS:** 
   - Every substantive claim, idea, or piece of data MUST be cited immediately in APA style `(Author, Year)` or `(Author et al., Year)`.
   - Extract authors and publication year from the source document text wherever possible. If the document contains references, use them.
   - **DO NOT invent authors, papers, or years.** If the text does not provide a citation, indicate it as `[citation needed]`.
4. **STYLE & FORMAT:** High-density, objective, technical, and precise. Avoid conversational or verbose fillers. Output only in clean Markdown.
"""



# # ------------------------------------------------------------------
# # WRITER USER PROMPT (Focus: Context Awareness & Specificity)
# # ------------------------------------------------------------------

# WRITER_USER_PROMPT = """
# **STATUS:** You are writing **Section {section_title}**.

# **OBJECTIVE:** Cover these key points: 
# {key_points}

# **GLOBAL CONTEXT (DO NOT REPEAT CONTENT FROM OTHER SECTIONS):**
# {global_plan_instruction}

# **INSTRUCTIONS:**
# 1. **FOCUS:** Focus heavily on the content within the `<source_document>` blocks that were mapped to this section. Use the source text to craft the content required by the key points.
# 2. **COHERENCE:** Ensure smooth transitions from the previous section (if applicable) using the Global Context as a reference for the flow.
# 3. **DO NOT REPEAT:** Do not repeat definitions or foundational content covered in earlier sections (check the Global Context).

# --- AVAILABLE SOURCE DOCUMENTS (Read Carefully) ---
# {structured_context}
# --- END SOURCE DOCUMENTS ---

# **WRITE THE SECTION CONTENT NOW:**
# """

