from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import json

# Enable headless mode in Selenium
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')  # This make Chromium reachable
options.add_argument('--disable-dev-shm-usage')  # Overcomes limited resource problems
options.add_argument('--disable-gpu')  # Applicable to windows os only

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

base_search = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E219&minBedrooms=2&maxPrice=1500&minPrice=700&propertyTypes=&maxDaysSinceAdded=1&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords=#prop146579867'

try:
    driver.get(base_search)
    time.sleep(5)
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    property_cards = soup.find_all('div', class_='propertyCard')
    
    new_properties_list = []
    base_url = 'https://www.rightmove.co.uk'
    
    for card in property_cards:
        link_tag = card.find('a', {'data-test': 'property-details'})
        price_tag = card.find('div', class_='propertyCard-rentalPrice-primary')
        location_tag = card.find('address', class_='propertyCard-address')
        agency_tag = card.find('a', class_='propertyCard-branchLogo-link')
        
        if link_tag and link_tag.get('href'):
            url = base_url + link_tag.get('href').split('?')[0]
            price = price_tag.text.strip() if price_tag else 'N/A'
            location = location_tag.text.strip() if location_tag else 'N/A'
            agency = agency_tag['title'] if agency_tag else 'N/A'
            
            property_added_to_market_on = time.strftime("%m/%d/%Y %H:%M:%S")
            property_dict = {
                "Property added date": property_added_to_market_on,
                "link": url,
                "price": price,
                "location": location,
                "agency": agency
            }
            new_properties_list.append(property_dict)

    # Write the updated list of property dictionaries to the JSON file
    with open('property_list.json', 'w') as file:
        json.dump(new_properties_list, file,ensure_ascii=False, indent=4)

finally:
    driver.quit()
