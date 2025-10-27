FROM python:3.9-slim

WORKDIR /app

# Install basic dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy lesson files
COPY . .

# Default command to run Python scripts
CMD ["python", "/app/work/categorical_variables.py"]