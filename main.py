from pathlib import Path
import sys
from pipeline.scam_detector.detector import ScamDetector
from app_utils import get_logger

#Path Normalization
project_root = Path(__file__).parent
sys.path.append(str(project_root))
logger = get_logger(__name__)

def main():
    detector = ScamDetector()
    test_message = "Congratulations! You've won a free cruise to the Bahamas. Click here to claim your prize."
    try:
        logger.info("Running the scam detection workflow.")
        result = detector.detect(test_message)
        print(f"Detection Result: {result}")
        logger.info("Scam detection workflow completed successfully.")
    except Exception as e:
        logger.error(f"Error during scam detection workflow: {e}")
        print(f"Error during scam detection workflow: {e}")


if __name__ == "__main__":
    main()