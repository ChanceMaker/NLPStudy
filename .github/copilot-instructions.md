# AI Agent Instructions for NLPStudy

This document provides essential context for AI agents working with the NLPStudy codebase.

## Project Overview
NLPStudy is a personal study project focused on Machine Learning and containerized NLP applications. The project serves as a learning environment for exploring NLP concepts and container-based deployments.

## Repository Structure
```
/
├── automation/     # Automation scripts and tools
├── containers/     # Docker configurations and container-related files
├── docs/          # Project documentation
├── lessons/       # NLP study materials and exercises
│   └── categorical_variables/
└── res/           # Resources and assets
```

## Development Environment
- Python-based project with virtual environment support
- Uses Docker for containerization
- VS Code as the preferred IDE

## Key Conventions
1. **Virtual Environment**:
   - Create using `python -m venv nlpenv` or `venv`
   - Environment files are gitignored (`nlpenv/`, `venv/`, `.env/`)

2. **Dependencies**:
   - Python package dependencies should be documented
   - Use virtual environment for dependency isolation

3. **Git Practices**:
   - Byte-compiled Python files are ignored (`*.py[cod]`)
   - VS Code settings are excluded from version control
   - Archive files (`.zip`, `.tar.gz`) are not tracked

## Work in Progress
This is an evolving study project. When contributing:
- Place new lessons under appropriate subdirectories in `lessons/`
- Document container configurations in `containers/`
- Add automation scripts in `automation/`

## Note to AI Agents
- Focus on educational clarity in code and documentation
- Maintain separation between study materials and implementation
- Consider container-based deployment when suggesting solutions