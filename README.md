# NLPStudy

A structured learning project for Natural Language Processing (NLP) and Machine Learning. This project serves as both a learning environment and a practical reference for NLP and ML concepts, focusing on hands-on exercises from Kaggle's Intermediate Machine Learning course.

## Project Structure

```
/
├── .github/           # GitHub configuration
├── data/              # Data storage
│   ├── pdfs/          # PDF documents for processing
│   └── processed/     # Processed data outputs
├── lessons/           # ML/NLP study materials and exercises
│   └── categorical_variables/
│       └── categorical_variables.py
├── src/               # Source code
├── venv/              # Python virtual environment
├── requirements.txt   # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.12+
- Git
- Virtual environment (venv)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd NLPStudy
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Current Lessons

### 1. Categorical Variables (Kaggle Intermediate ML)
**Location:** [lessons/categorical_variables/](lessons/categorical_variables/)

**Topics covered:**
- Handling categorical data in machine learning
- Three approaches:
  1. Drop categorical variables
  2. Ordinal (Label) Encoding
  3. One-Hot Encoding
- Understanding cardinality and its impact
- Handling unknown categories in validation/test data

**Key concepts:**
- When to use each encoding method
- Memory and performance trade-offs
- Train/validation data consistency

**Run the exercise:**
```bash
python lessons/categorical_variables/categorical_variables.py
```

## Development Environment

This project uses a local Python virtual environment for development:
- **venv/**: Isolated Python environment
- **requirements.txt**: Project dependencies (pandas, scikit-learn, numpy, etc.)
- **data/**: Storage for datasets and processed outputs

## Contributing

This is a personal learning project, but suggestions and improvements are welcome:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Project Status
🚧 **Work in Progress** 🚧

This project is actively evolving as new lessons and concepts are added. Check back regularly for updates and new content.

## License

This project is licensed under the MIT License - see the LICENSE file for details.