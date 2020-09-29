from bs4 import BeautifulSoup
import requests


url = input('Enter a url to search for links: ')
print('\nSearching for links in url: ' + url + '\n')
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('a')
for idx, link in enumerate(links):
    link_href = link.get('href')
    if not link_href.startswith('http'):
        continue

    link_response = requests.get(link_href)

    if link_response.ok:
        link_response_status = 'GOOD'
    else:
        link_response_status = 'BAD'

    print(f'({idx + 1}) [{link_response_status}] {link_href}', end='')
    if link_response_status == 'BAD':
        print(f' (STATUS CODE {link_response.status_code})', end='')
    print()
