import requests, os, bs4
import logging


logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)


while True:
    try:
        limit = int(input('How many comics would you like to download? '))
        break
    except ValueError:
        logging.error('Enter an integer.')


count = 0
while not url.endswith('#'):
    count += 1

    logging.info(f'({count}) Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic_elem = soup.select('#comic img')

    if not comic_elem:
        logging.info('Coud not find comic image.')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        logging.info(f'({count}) Downloading image {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')

    if count == limit:
        break


logging.info('Done.')
