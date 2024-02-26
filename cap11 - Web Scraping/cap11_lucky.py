#!/home/pdajgs/python_labs/py3.7/bin/python3

# abre os resultados das pesquisas no google em abas

import requests, sys, webbrowser, bs4

print('Pesquisando...')

try:
    search = '+'.join(sys.argv[1:])
    link = requests.get(f'http://google.com/search?q={search}')
    link.raise_for_status()
    # soup = bs4.BeautifulSoup(link.text, 'html.parser')
    soup = bs4.BeautifulSoup(link.text, features="lxml")
    # linkElement = soup.select('div#main > div > div > div > a')
    linkElements = soup.select('.kCrYT > a')
    # linkElement = soup.select('.r > a') #exemplo do livro, não funfa
    # print(linkElement[0].get('href'))
    numOpen = min(5, len(linkElements))
    for i in range(numOpen): #o range foi utilizado pois "int object is not iterable"
        webbrowser.open('http://google.com%s' %(linkElements[i].get('href')))
except Exception as e:
    print(e)