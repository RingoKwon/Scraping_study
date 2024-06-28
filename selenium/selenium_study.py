from selenium import webdriver
from selenium.webdriver.chrome.service import Service # add by ringo

website = 'https://www.adamchoi.co.uk/overs/detailed' # https://www.adamchoi.co.uk/overs/detailed
# /Users/ringokwon/Project/python_project/scraping_study2/chromedriver
path = '/Users/ringokwon/Project/python_project/scraping_study2/selenium/chromedriver'
driver = webdriver.Chrome( service=Service(  path)) #add by ringo
driver.get(website)

# time.sleep(10)
while True: # add by ringo
    pass