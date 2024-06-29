from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

print(webdriver.__version__)
website = 'https://imginn.com/ssahn01/'
path = '/Users/ringokwon/Project/python_project/scraping_study2/chromedriver'

# Create a Chrome Options object
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")  # To disable notifications
chrome_options.add_argument("--disable-infobars")  # To disable infobars

driver = webdriver.Chrome(service=Service(path), options=chrome_options)

driver.get(website)

# Wait until the element is visible and interactable
wait = WebDriverWait(driver, 10)
try:
    all_matches_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="download"]')))
    all_matches_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    while True:
        driver.title
except:
    pass