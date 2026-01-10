import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent
load_dotenv(PROJECT_ROOT / '.env')

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DEFAULT_GEMINI_MODEL = "gemini-2.5-flash-lite"
MAX_RETRIES = 3
RETRY_DELAY = 2

OUTPUT_DIR = PROJECT_ROOT.parent / "outputs"
LOGS_DIR = OUTPUT_DIR / "logs"