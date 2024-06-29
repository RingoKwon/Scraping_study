from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print(webdriver.__version__)
website = 'https://imginn.com/ssahn01/'
path = '/Users/ringokwon/Project/python_project/scraping_study2/chromedriver'

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

driver = webdriver.Chrome(service=Service(path), options=options)

driver.get(website)

# Wait until the element is visible and interactable
wait = WebDriverWait(driver, 10)
try:
    all_matches_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="download"]')))
    all_matches_button.click()
except Exception as e:
    print(f"An error occurred: {e}")

# Handle pop-up ads
try:
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[-1])
    # Close the new window
    driver.close()
    # Switch back to the main window
    driver.switch_to.window(driver.window_handles[0])
except Exception as e:
    print(f"An error occurred while handling pop-up ads: {e}")

try:
    while True:
        driver.title
except:
    pass