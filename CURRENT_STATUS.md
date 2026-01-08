cd ~/Documents/GIT/NLPStudy

# Create context file
cat > CURRENT_STATUS.md << 'EOF'
# Paper Q&A Project Status

## What I'm Building
10-day transformer project: Scientific Paper Q&A system using RAG
- Upload research papers (GPT-1, BERT, etc.)
- Ask questions, get answers with citations

## Current Progress

### Day 1: PDF Processing ✅ (mostly done)
- Discovered papers are scanned (need OCR)
- Set up PyMuPDF with Tesseract OCR
- Created robust PDF processor with OCR fallback
- Just created config.py

### Project Structure
```
NLPStudy/
├── data/
│   ├── pdfs/          # Research papers (scanned)
│   └── processed/     # Will contain extracted chunks
├── src/
│   ├── config.py      # Project configuration
│   └── extract_pdf.py # PDF processor with OCR
├── venv/
└── requirements.txt
```

### Tech Stack So Far
- Python 3.12
- PyMuPDF (fitz) for PDF extraction
- Tesseract for OCR on scanned pages
- Rich for console output

### Next Steps
1. Finish running PDF extraction on all papers
2. Verify chunk quality
3. Day 2: Generate embeddings with SciBERT
4. Day 3-4: Vector database (ChromaDB) and search
5. Day 5-6: Question answering pipeline

### Papers Processing
- GPT-1: Improving Language Understanding by Generative Pre-Training
- BERT
- Layer Normalization  
- GPT-2

### Recent Issues Solved
- ✅ Python 3.12 compatibility (numpy version)
- ✅ OCR for scanned PDFs
- ✅ Import error (created config.py)

### What I Need Help With
Continue Day 1, then move to embeddings and vector search.
EOF
```

Then in VS Code Claude, just say:
```
Read CURRENT_STATUS.md - I need help continuing this project