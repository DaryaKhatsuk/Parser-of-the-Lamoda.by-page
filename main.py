import requests
import bs4


class Parser():
    def __init__(self):
        self.send()

    def send(self):
        request = requests.get('https://www.lamoda.by/c/7628/shoes-women-shoes-cossacks/?sitelink=topmenuW&l=6')
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        # print(bs)
        for i in bs.find_all('span', class_='x-product-card-description__price-WEB8507_price_no_bold'):
            print(i.text)
        for i in bs.find_all('div', class_='x-product-card-description__brand-name'):
            print(i.text)
        for i in bs.find_all('div', class_='x-product-card-description__product-name'):
            print(i.text)


pars = Parser()
pars.send()