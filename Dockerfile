# Use an official Python runtime as a parent image
FROM python:3.9

# Install system dependencies for Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Selenium to use Chromium
ENV SELENIUM_DRIVER_NAME=chrome
ENV SELENIUM_DRIVER_EXECUTABLE_PATH=/usr/bin/chromium-driver
ENV SELENIUM_DRIVER_ARGUMENTS='--headless --no-sandbox --disable-dev-shm-usage'

# Specify the command to run the Python script when the container launches
CMD ["python", "propertylookup.py"]
