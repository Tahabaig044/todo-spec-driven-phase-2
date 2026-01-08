# FROM python:3.11-slim

# WORKDIR /app

# # Install system dependencies needed for asyncpg and other packages
# RUN apt-get update && apt-get install -y \
#     gcc \
#     g++ \
#     build-essential \
#     libpq-dev \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements and install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application
# COPY . .

# # Make the startup script executable
# RUN chmod +x start.sh

# # Set environment variables
# ENV PYTHONPATH=/app:$PYTHONPATH

# # Create a non-root user for security
# RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
# USER app

# # Expose port (Hugging Face will use the port specified)
# EXPOSE 8000

# # Health check for Hugging Face (using default port, as PORT may not be available in healthcheck context)
# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
#     CMD curl -f http://localhost:${PORT:-8000}/health || exit 1

# # Run the application with startup script
# CMD ["./start.sh"]
FROM python:3.11-slim

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]