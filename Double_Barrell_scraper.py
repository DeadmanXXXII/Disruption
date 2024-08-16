from selenium import webdriver
from selenium.webdriver.chrome.service import Service                                                                 from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By                                                                           from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC                                                      import time
                                                                                                                      # Path to your chromedriver
chrome_driver_path = '/usr/bin/chromedriver'                                                                          
# Set up Chrome options                                                                                               chrome_options = Options()
chrome_options.add_argument('--headless')  # Ensure GUI is not needed
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome driver                                                                                        service = Service(chrome_driver_path)                                                                                 driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = 'https://www.linkedin.com/posts/blu-corbel-bb5700265_design-a-resiliency-strategy-for-ransomware-activity-7229928845817122817-HcxN'
    driver.get(url)                                                                                                   
    # Wait for the page to load                                                                                           WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                                                                                                                          # Example: Scrape all links
    links = driver.find_elements(By.TAG_NAME, 'a')                                                                        for link in links:
        print(link.get_attribute('href'))                                                                             
finally:                                                                                                                  # Clean up
    driver.quit()