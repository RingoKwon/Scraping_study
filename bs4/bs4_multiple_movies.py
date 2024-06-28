import requests
from bs4 import BeautifulSoup
import os

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
# website   = 'https://imginn.com/ssahn01/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print( soup.prettify())

#  pagenation
pagenation = soup.find('ul', class_='pagination')
pages  = pagenation.find_all('li', class_='page-item')
last_page = pages[-2].text
# print(last_page)
#
# print(last_page)
links = []
for page in range( 1, int( last_page) + 1):
    result = requests.get(f'{website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')
    # print(page) # page number shows up

    a_all = box.find_all('a', href=True)
    for link in a_all:
        links.append(link['href'])


    links_test = links[:5]# test only 5 links per page for now
    # print(len(links)   )


    for link in links_test:
        try:
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            rel_path = '/Users/ringokwon/Project/python_project/scraping_study2/bs4/files_bs4'
            with open(os.path.join(rel_path, f'{title}.txt'), 'w') as file:
                file.write(transcript)
        except:
            pass



