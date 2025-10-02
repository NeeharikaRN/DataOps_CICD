# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements if you have one (optional)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python scripts and data folder into container
COPY transform.py .
COPY data ./data

# Install dependencies
RUN pip install pandas

# Default command to run your transform script
CMD ["python", "transform.py"]
