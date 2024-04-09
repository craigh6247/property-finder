    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    import re
    import time
    import json


    # Enable headless mode in Selenium
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  # This make Chromium reachable
    options.add_argument('--disable-dev-shm-usage')  # Overcomes limited resource problems
    options.add_argument('--disable-gpu')  # applicable to windows os only


    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)

    properties_filename = 'properties_list.json'
    base_search = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E219&minBedrooms=2&maxPrice=1500&minPrice=700&propertyTypes=&maxDaysSinceAdded=1&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords=#prop146579867'


    try:
        # Navigate to the specified URL
        driver.get(base_search)
        # Wait for the page to fully load
        time.sleep(5)

        # Get the page source
        page_source = driver.page_source

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all <a> tags with href attributes that match the specified pattern
        pattern = re.compile(r'/properties/\d+#/\?channel=RES_LET')
        property_links = soup.find_all('a', href=pattern)

        new_properties_list = []
        base_url = 'https://www.rightmove.co.uk'

        # Load existing properties from the file
        try:
            with open(properties_filename, 'r') as json_file:
                existing_properties_list = json.load(json_file)
                existing_urls = {prop['link'] for prop in existing_properties_list}
        except FileNotFoundError:
            existing_properties_list = []
            existing_urls = set()

        for link in property_links:
            href = link.get('href')
            end_pos = href.find("RES_LET") + len("RES_LET")
            deduced_href = href[:end_pos]
            url = base_url + deduced_href

            # Check if the URL is not already in the existing data
            if url not in existing_urls:
                property_added_to_market_on = time.strftime("%m/%d/%Y %H:%M:%S")
                property_dict = {
                    "Property added date": property_added_to_market_on,
                    "link": url
                }
                new_properties_list.append(property_dict)
                existing_properties_list.append(property_dict)

        # Write the updated list of property dictionaries to the JSON file
        with open(properties_filename, 'w') as json_file:
            json.dump(existing_properties_list, json_file, indent=4)

    finally:
        driver.quit()
