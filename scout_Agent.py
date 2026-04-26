from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class GoogleMapsScraper:
    """
    MCP-style Scraping Agent.
    Directly navigates Google Maps to extract live venue data and direct links.
    """
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def search_places(self, location, query):
        search_query = f"{query} in {location}"
        url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
        self.driver.get(url)
        time.sleep(5) # Wait for JS rendering

        results = []
        # Selection logic for Google Maps result cards
        places = self.driver.find_elements(By.CLASS_NAME, "Nv2y3c")[:3] 

        for place in places:
            try:
                title = place.find_element(By.CLASS_NAME, "qBF1Pd").text
                link = place.find_element(By.TAG_NAME, "a").get_attribute("href")
                results.append({"title": title, "url": link})
            except:
                continue
        return results

    def close(self):
        self.driver.quit()