from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed' # https://www.adamchoi.co.uk/overs/detailed
# /Users/ringokwon/Project/python_project/scraping_study2/chromedriver
path = '/Users/ringokwon/Project/python_project/scraping_study2/selenium/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)
print(driver.page_source)