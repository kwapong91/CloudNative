# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Install system dependencies needed for building and running the application
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    dirmngr \
    gnupg \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138 0E98404D386FA1D9 \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    python3-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy your application code here
COPY . /app

# Set the working directory
WORKDIR /app

# Install any Python dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]
