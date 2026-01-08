"""Configuration for Paper Q&A System"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PDF_DIR = DATA_DIR / "pdfs"
PROCESSED_DIR = DATA_DIR / "processed"

# Processing settings
CHUNK_SIZE = 500  # characters per chunk
CHUNK_OVERLAP = 50  # overlap between chunks
MIN_CHUNK_SIZE = 100  # minimum chunk size to keep

# Create directories if they don't exist
PDF_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Print confirmation when run directly
if __name__ == "__main__":
    from rich.console import Console
    console = Console()
    
    console.print("[green]✓ Configuration loaded[/green]")
    console.print(f"PDF Directory: {PDF_DIR}")
    console.print(f"Processed Directory: {PROCESSED_DIR}")
    console.print(f"Chunk Size: {CHUNK_SIZE}")