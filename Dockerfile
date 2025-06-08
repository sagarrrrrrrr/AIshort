# Use official lightweight Python image
FROM python:3.10-slim

# Install system dependencies
RUN apt update && apt install -y \
    ffmpeg \
    wget \
    fonts-dejavu-core \
    fonts-freefont-ttf

# Set working directory
WORKDIR /app

# Copy files from local folder to the image
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Start the Flask app
CMD ["python", "app.py"]
