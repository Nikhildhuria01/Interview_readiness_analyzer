FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Print logs immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system libraries
RUN apt-get update && apt-get install -y \
    gcc \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better Docker caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]