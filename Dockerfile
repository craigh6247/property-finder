# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install git
RUN apt-get update && apt-get install -y git

# Clone the specific repository
RUN git clone https://github.com/craigh6247/property-finder .

# Now the requirements.txt should be in the current directory
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Chromium and chromedriver for Selenium
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Selenium to use Chromium
ENV SELENIUM_DRIVER_NAME=chrome
ENV SELENIUM_DRIVER_EXECUTABLE_PATH=/usr/bin/chromedriver
ENV SELENIUM_DRIVER_ARGUMENTS='--headless'

# Run the Python script when the container launches
# Update 'your_script.py' to the actual script name in the repository

CMD ["python", "propertylookup.py"]
