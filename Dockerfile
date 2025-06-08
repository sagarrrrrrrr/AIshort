# Use a slim Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by MoviePy & fonts
RUN apt update && apt install -y \
    ffmpeg \
    wget \
    fonts-dejavu-core \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . .

# Install Python packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
