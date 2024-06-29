from selenium import webdriver
from selenium.webdriver.chrome.service import Service # add by ringo
print(webdriver.__version__)
website = 'https://www.adamchoi.co.uk/overs/detailed' # https://www.adamchoi.co.uk/overs/detailed
# /Users/ringokwon/Project/python_project/scraping_study2/chromedriver
path = '/Users/ringokwon/Project/python_project/scraping_study2/selenium/chromedriver'
driver = webdriver.Chrome( service=Service(  path)) #add by ringo
driver.get(website)

# all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
all_matches_button.click()


# driver.quit()
# # time.sleep(10)
try:
    while True: # add by ringo
        driver.title
except:
    pass