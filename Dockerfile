# Use a slim Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by MoviePy & fonts
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

# Copy app files
COPY . .

# Install Python packages
RUN pip install --upgrade pip \
 && pip install --no-cache-dir moviepy \
 && pip install --no-cache-dir -r requirements.txt
 
# Expose Flask port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
