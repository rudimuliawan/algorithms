import sys
from pathlib import Path


DS_PATH = f"{Path(__file__).resolve(strict=True).parent.parent.parent}"
sys.path.append(f"{DS_PATH}")


from data_structures.python import Stack, Queue
