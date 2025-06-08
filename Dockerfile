FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for moviepy + rendering
RUN apt update && apt install -y \
    ffmpeg \
    wget \
    libx11-6 \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port
EXPOSE 5000

CMD ["python", "app.py"]
