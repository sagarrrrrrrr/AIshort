# Use lightweight Python image
FROM python:3.10-slim

# Install system packages
RUN apt update && apt install -y \
    ffmpeg \
    wget \
    fonts-dejavu-core \
    fonts-freefont-ttf

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Flask app
CMD ["python", "app.py"]
