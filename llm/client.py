import time
from google import genai
from config import GEMINI_API_KEY, DEFAULT_GEMINI_MODEL, MAX_RETRIES, RETRY_DELAY
from app_utils import get_logger

logger = get_logger(__name__)

class LLMClient:
    def __init__(self, model_name=DEFAULT_GEMINI_MODEL, max_retries=MAX_RETRIES, retry_delay=RETRY_DELAY):
        self.model_name = model_name
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        print(f"API Key: {GEMINI_API_KEY}")
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        logger.info(f"LLMClient initialized with model: {self.model_name}")

    def call(self, prompt: str, **kwargs) -> str:
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Calling LLM API, attempt {attempt + 1}...")
                response =self.client.models.generate_content(
                    model= self.model_name,
                    contents= prompt, 
                    **kwargs
                )
                if response and response.text:
                    return response.text.strip()
                else:
                    raise Exception("Received empty response from LLM.")
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise Exception(f"LLM API call failed after {self.max_retries} attempts: {e}")
                time.sleep(self.retry_delay * (2** attempt))