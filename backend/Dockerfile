# Stage 1: Build stage to compile dependencies securely
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies required to build some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies in user space
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# Stage 2: Final lightweight run stage
FROM python:3.11-slim AS runner

WORKDIR /app

# Copy only the compiled packages from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Update system PATH so Python can locate installed packages
ENV PATH=/root/.local/bin:$PATH

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Run the API server using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]