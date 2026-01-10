from pathlib import Path
from app_utils import load_file

PROMPTS_DIR = Path(__file__).parent / "prompt"

def load_prompt(file_name: str) -> str:
    return load_file(PROMPTS_DIR / file_name)

PROMPT = load_prompt("react.md")

def generate_prompt(user_input: str) -> str:
    return f"{PROMPT}\n\nUser Input:\n{user_input.strip()}"