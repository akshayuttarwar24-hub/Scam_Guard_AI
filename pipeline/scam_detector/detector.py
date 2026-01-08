from typing import List, Dict, Any
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt
from utils import get_logger

logger = get_logger(__name__)

class ScamDetector:

    def __init__(self, strategy: str = "react"):
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"Initialized ScamDetector with strategy: {self.strategy}")

    def detect(self, message: str) -> Dict[str, Any]:
        logger.info("Started scam detection for input message.")
        try:
            prompt =build_prompt(message, self.startegy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)

            logger.info("Scam detection successful.")
            return parsed_result

        except Exception as e:
            logger.error(f"Scam detection failed: {e}")