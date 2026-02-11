FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY config/ ./config/

# Create memory directory
RUN mkdir -p memory

# Set Python path
ENV PYTHONPATH=/app/src

# Run the application
CMD ["python", "src/main.py"]
