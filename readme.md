
# Rightmove Scraper

This project is a web scraping application using Python, Selenium, and BeautifulSoup.

## Environment Setup

To run this project, you need Python installed on your system, along with the Selenium and BeautifulSoup libraries. It's recommended to use a virtual environment for Python projects to manage dependencies.

### Prerequisites

- Python 3
- pip (Python package installer)

### Setting up a Virtual Environment

1. **Create a Virtual Environment:**

   Navigate to your project directory in the terminal and run the following command to create a virtual environment named `venv`:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**

   - On Windows, run:

     ```bash
     .\venv\Scripts\activate
     ```

   - On Unix or MacOS, run:

     ```bash
     source venv/bin/activate
     ```

   Your command prompt should now reflect the virtual environment's name, indicating that it is active.

### Install Required Packages

1. **Install Dependencies:**

   Ensure you have a `requirements.txt` file in your project directory with the following content:

   ```
   selenium
   beautifulsoup4
   ```

   Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

### WebDriver

For Selenium to interact with a web browser, you need to have the appropriate WebDriver:

- For Chrome, download ChromeDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/).
- For Firefox, download geckodriver from [GitHub - mozilla/geckodriver](https://github.com/mozilla/geckodriver).

Make sure the WebDriver executable is in your PATH or specify its location directly in your script.

## Running the Application

With the virtual environment activated and dependencies installed, you can run the Python script that contains your web scraping code. For example:

```bash
python my_scraping_script.py
```

Replace `my_scraping_script.py` with the name of your Python script.

## Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to your global Python environment.

