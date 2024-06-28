import requests
from bs4 import BeautifulSoup

website = ('https://imginn.com/p/C8tKHSNpsO0/')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

response = requests.get(website, headers=headers)
print(response.text)