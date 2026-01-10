from typing import Optional
from app_utils import get_logger
from llm.client import LLMClient

logger = get_logger(__name__)
class LLMExecutor:

    def __init__(self, model: Optional[str] = None):
        logger.info("""Initializing LLMExecutor with Gemini API client.""")
        self.llm: LLMClient = LLMClient(model) if model else LLMClient()

    def execute(self, prompt: str) -> str:
        logger.info("Executing LLM prompt.")
        try:
            response = self.llm.call(prompt)
            return response
        except Exception as e:
            logger.error(f"LLM execution failed: {e}")
            raise Exception(f"LLM execution failed: {e}")  
        