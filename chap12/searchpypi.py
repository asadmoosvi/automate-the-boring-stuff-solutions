import requests, sys, webbrowser, bs4


url = 'https://pypi.org/search/?q=' + '+'.join(sys.argv[1:])
print('Searching url: ' + url)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.package-snippet')
num_open = min(5, len(link_elems))

for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print(f'Opening url: {url_to_open}')
    print('\a', end='')
    webbrowser.open(url_to_open)
