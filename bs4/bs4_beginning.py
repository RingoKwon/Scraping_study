import requests
from bs4 import BeautifulSoup

website= 'https://subslikescript.com/movie/Titanic-120338'
# website   = 'https://imginn.com/ssahn01/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print( soup.prettify())

box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip = True, separator=' ')
# test
print(title)

# print( '---')
print(transcript)