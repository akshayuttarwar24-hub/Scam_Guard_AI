from typing import Dict, Any
from app_utils import get_logger, extract_json_from_text

logger = get_logger(__name__)

class OutputParser:
    def parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        logger.info("Parsing LLM output...")

        parsed_json = extract_json_from_text(llm_output)

        if parsed_json:
            logger.info("LLM output parsed successfully.")
            return parsed_json
        else:
            logger.warning("Failed to parse LLM output.")
            return {
                "label": "Uncertain", 
                "reasoning": "Could not parse LLM output",
                "intent": "Unknown",
                "risk_factors": ["Parsing Error"]
            }   