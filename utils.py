import logging
import re
import json
from pathlib import Path

def load_file(file_path: str) -> str:
    return Path(file_path).read_test().strip()

def logger(name: str) -> logging.Looger:
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    return logging.getLogger(name)