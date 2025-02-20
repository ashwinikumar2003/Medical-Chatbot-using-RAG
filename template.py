import os
from pathlib import Path
import logging

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")
        
    if not filepath.exists():
        filepath.touch()
        logging.info(f"Created file: {filepath}")
        
    else:
        logging.info(f"File already exists: {filepath}")