FROM python:3.9-slim-buster

# Install system dependencies needed for psutil and other packages
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    python3-dev \
    build-essential \
    && apt-get clean

WORKDIR /app

# Copy the requirements.txt and install Python dependencies
COPY requirements.txt . 
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5002 for the Flask application
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

