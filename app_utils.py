import logging
import re
import json
from pathlib import Path

def load_file(file_path: str) -> str:
    return Path(file_path).read_text().strip()

def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    return logging.getLogger(name)

def extract_json(text):
    """
    Finds the first '{' and the last '}' in a string 
    and parses it as JSON.
    """
    try:
        # Regex to find the JSON block inside the text
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"JSON Parsing Error: {e}")
    
    # Fallback if parsing fails
    return {
        "label": "Uncertain", 
        "reasoning": "Could not parse AI response",
        "intent": "Unknown",
        "risk_factors": ["Parsing Error"]
    }

def extract_json_from_text(text: str) -> dict:
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {}
    except Exception as e:
        return {}
    

