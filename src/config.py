"""
Central configuration file for the SOTA Generator.
"""

# --- MODEL SELECTION ---
# The primary model for generating the plan and the content.
PRIMARY_MODEL = "gemini-2.0-flash"

# --- GENERATION SETTINGS ---
# Lower temperature = more deterministic/factual.
# Higher temperature = more creative.

TEMP_PLANNING = 0.3      
TEMP_WRITING = 0.3       
TEMP_VERIFICATION = 0.0