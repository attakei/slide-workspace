import shutil
from pathlib import Path

pycache_dir = Path("__pycache__")

if pycache_dir.exists():
    shutil.rmtree(pycache_dir)
