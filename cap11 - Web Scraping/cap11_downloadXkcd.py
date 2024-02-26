#!/home/pdajgs/python_labs/py3.7/bin/python3

import requests, os, bs4

try:
    url = 'http://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)
except Exception as e:
    print(e)

while not url.endswith('#'):
    print('Download page %s...' %(url))
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as f:
        print(f)

    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not found comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Download image %s...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        
        for i in res.iter_content(1000):
            imageFile.write(i)
        imageFile.close()
    
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')