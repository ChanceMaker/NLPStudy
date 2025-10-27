# NLPStudy

A structured learning project for Natural Language Processing (NLP) and Machine Learning, organized through containerized lessons. This project serves as both a learning environment and a practical reference for NLP concepts and container-based deployments.

## Project Structure

```
/
├── automation/     # Automation scripts and tools
├── containers/     # Docker configurations for each lesson
│   └── lesson1_categorical_variables/
│       ├── Dockerfile
│       ├── docker-compose.yml
│       └── requirements.txt
├── docs/          # Project documentation
├── lessons/       # NLP study materials and exercises
│   └── categorical_variables/
│       └── categorical_variables.py
└── res/           # Resources and assets
```

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Git
- Python 3.9+ (for local development)

### Running a Lesson
Each lesson is containerized for reproducibility and isolation. To run a lesson:

```bash
# Navigate to the lesson's container directory
cd containers/lesson1_categorical_variables

# Build and run the container
docker-compose up --build
```

## Lessons Overview

### 1. Categorical Variables
- Basic handling of categorical data
- Label Encoding and One-Hot Encoding
- Practical examples with pandas and scikit-learn

## Development Environment

### Container-Based Approach
Each lesson is packaged in its own container, ensuring:
- Consistent environments
- Isolated dependencies
- Reproducible results
- Version controlled progress

### Local Development
While containers are the preferred method, you can also work locally:
1. Create a virtual environment: `python -m venv venv`
2. Install requirements: `pip install -r containers/lesson*/requirements.txt`
3. Run scripts directly: `python lessons/*/script.py`

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