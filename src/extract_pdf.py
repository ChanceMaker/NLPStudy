import fitz  # PyMuPDF
from pathlib import Path
from typing import List, Dict, Optional
import json
from rich.console import Console
from rich.progress import track
import re

console = Console()

# Optional OCR imports - only if needed
try:
    from PIL import Image
    import pytesseract
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False
    console.print("[yellow]⚠️  OCR not available. Install: pip install pytesseract pillow[/yellow]")


class PDFProcessor:
    """Extract and process text from research papers with OCR fallback"""
    
    def __init__(self, pdf_path: str, use_ocr: bool = True):
        self.pdf_path = Path(pdf_path)
        self.doc = fitz.open(str(pdf_path))
        self.paper_name = self.pdf_path.stem
        self.use_ocr = use_ocr and OCR_AVAILABLE
        
    def extract_text_by_page(self) -> List[Dict]:
        """Extract text from each page with OCR fallback"""
        pages = []
        
        console.print(f"[blue]Processing {self.paper_name}...[/blue]")
        
        for page_num in track(range(len(self.doc)), description="Extracting pages"):
            page = self.doc[page_num]
            
            # Try normal text extraction first
            text = page.get_text("text")
            
            # If barely any text and OCR available, use OCR
            if len(text.strip()) < 100 and self.use_ocr:
                console.print(f"  [yellow]Using OCR for page {page_num+1}[/yellow]")
                text = self._ocr_page(page)
            
            # Clean up text
            text = self._clean_text(text)
            
            pages.append({
                'page_number': page_num + 1,
                'text': text,
                'char_count': len(text),
                'paper': self.paper_name,
                'used_ocr': len(text.strip()) > 100 and self.use_ocr
            })
        
        return pages
    
    def _ocr_page(self, page) -> str:
        """OCR a single page"""
        if not OCR_AVAILABLE:
            return ""
        
        try:
            # Convert page to high-res image for better OCR
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better quality
            pix = page.get_pixmap(matrix=mat)
            
            # Convert to PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # OCR with Tesseract
            text = pytesseract.image_to_string(img, lang='eng')
            
            return text
            
        except Exception as e:
            console.print(f"  [red]OCR failed: {e}[/red]")
            return ""
    
    def _clean_text(self, text: str) -> str:
        """Clean extracted text"""
        # Remove excessive whitespace
        text = ' '.join(text.split())
        
        # Fix common OCR errors
        text = text.replace('ﬁ', 'fi')  # ligature
        text = text.replace('ﬂ', 'fl')  # ligature
        text = text.replace('–', '-')   # en dash
        # text = text.replace(''', "'")   # smart quote
        # text = text.replace('"', '"')   # smart quote
        # text = text.replace('"', '"')   # smart quote
        
        return text
    
    def extract_metadata(self) -> Dict:
        """Extract paper metadata"""
        metadata = self.doc.metadata or {}
        
        return {
            'title': metadata.get('title', self.paper_name),
            'author': metadata.get('author', 'Unknown'),
            'pages': len(self.doc),
            'paper_name': self.paper_name,
            'used_ocr': self.use_ocr
        }
    
    def chunk_text(self, pages: List[Dict], chunk_size: int = 500, 
                   overlap: int = 50) -> List[Dict]:
        """Split text into overlapping chunks"""
        chunks = []
        chunk_id = 0
        
        for page in pages:
            text = page['text']
            page_num = page['page_number']
            
            # Skip pages with very little text
            if len(text.strip()) < 50:
                continue
            
            # Split into sentences
            sentences = self._split_into_sentences(text)
            
            current_chunk = []
            current_length = 0
            
            for sentence in sentences:
                sentence_length = len(sentence)
                
                if current_length + sentence_length > chunk_size and current_chunk:
                    chunk_text = ' '.join(current_chunk)
                    
                    chunks.append({
                        'chunk_id': chunk_id,
                        'text': chunk_text,
                        'page_number': page_num,
                        'paper': page['paper'],
                        'char_count': len(chunk_text)
                    })
                    
                    chunk_id += 1
                    
                    # Keep overlap
                    overlap_sentences = self._get_overlap_sentences(
                        current_chunk, overlap
                    )
                    current_chunk = overlap_sentences + [sentence]
                    current_length = sum(len(s) for s in current_chunk)
                else:
                    current_chunk.append(sentence)
                    current_length += sentence_length
            
            # Last chunk
            if current_chunk:
                chunk_text = ' '.join(current_chunk)
                chunks.append({
                    'chunk_id': chunk_id,
                    'text': chunk_text,
                    'page_number': page_num,
                    'paper': page['paper'],
                    'char_count': len(chunk_text)
                })
                chunk_id += 1
        
        return chunks
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """Simple sentence splitter"""
        # Split on period followed by space and capital
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _get_overlap_sentences(self, sentences: List[str], 
                               target_chars: int) -> List[str]:
        """Get last N sentences for overlap"""
        overlap = []
        char_count = 0
        
        for sentence in reversed(sentences):
            if char_count + len(sentence) <= target_chars:
                overlap.insert(0, sentence)
                char_count += len(sentence)
            else:
                break
        
        return overlap
    
    def process_and_chunk(self, chunk_size: int = 500, 
                         overlap: int = 50) -> Dict:
        """Complete processing pipeline"""
        # Extract pages (with OCR if needed)
        pages = self.extract_text_by_page()
        
        # Create chunks
        chunks = self.chunk_text(pages, chunk_size, overlap)
        
        # Get metadata
        metadata = self.extract_metadata()
        
        result = {
            'metadata': metadata,
            'pages': pages,
            'chunks': chunks,
            'stats': {
                'total_pages': len(pages),
                'total_chunks': len(chunks),
                'avg_chunk_size': sum(c['char_count'] for c in chunks) / len(chunks) if chunks else 0,
                'ocr_pages': sum(1 for p in pages if p.get('used_ocr', False))
            }
        }
        
        return result


# Quick test
if __name__ == "__main__":
    from config import PDF_DIR, PROCESSED_DIR
    
    pdf_files = list(PDF_DIR.glob("*.pdf"))
    
    if not pdf_files:
        console.print("[red]No PDF files found in data/pdfs/[/red]")
    else:
        console.print(f"[green]Found {len(pdf_files)} PDF(s)[/green]")
        for pdf_file in pdf_files:
            processor = PDFProcessor(pdf_file, use_ocr=True)
            result = processor.process_and_chunk()
            
            # Save
            output_path = PROCESSED_DIR / f"{result['metadata']['paper_name']}_chunked.json"
            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2)
            
            console.print(f"[green]✓ {pdf_file.name}: {result['stats']['total_chunks']} chunks ({result['stats']['ocr_pages']} pages used OCR)[/green]")

