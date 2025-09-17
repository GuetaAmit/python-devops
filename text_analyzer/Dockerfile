# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install uv and dependencies
RUN pip install --upgrade pip uv

# Install TextAnalyzer package
RUN uv pip install -e .

# Set default command to run tests
CMD ["uv", "run", "python", "test_script/main.py"]
