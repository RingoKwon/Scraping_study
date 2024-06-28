import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com'
website = f'{root}/movies'
# website   = 'https://imginn.com/ssahn01/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print( soup.prettify())

links = []
box = soup.find('article', class_='main-article')
a_all = box.find_all('a', href=True)
for link in a_all:
    links.append(link['href'])

links_test = links[:5]
print(links_test)

for link in links_test:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)
