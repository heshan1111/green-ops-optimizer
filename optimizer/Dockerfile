FROM python:3.11-slim

WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Show Python output immediately
ENV PYTHONUNBUFFERED=1

# Start the optimizer
CMD ["python", "main.py"]