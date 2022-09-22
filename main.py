import requests
import bs4
import json


JSON = 'shoes.json'
HOST = 'https://www.lamoda.by/'
URL = 'https://www.lamoda.by/c/209/shoes-domashnaja/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='x-product-card__card')
    cards = []
    for item in items:
        cards.append(
            {
                'brand_name': item.find('div', class_='x-product-card-description__brand-name').get_text(),
                'product_name': item.find('div', class_='x-product-card-description__product-name').get_text(),
                'actual_price': item.find('span',
                                          class_='x-product-card-description__price-WEB8507_price_no_bold').get_text(),
            }
        )
    return cards


def safe_doc(items, path):
    with open(path, 'w', newline='', encoding='UTF-8') as file:
        sl = {}
        sc = 1
        for item in items:
            sl.update({"Бренд " + str(sc): item["brand_name"],
                       "Название продукта " + str(sc): item["product_name"],
                       "Актуальная цена " + str(sc): item["actual_price"]})
            sc += 1
        json.dump(sl, file, indent=4, ensure_ascii=False)


def parser():
    PAGENATION = int(input("Введите количество страниц: "))
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION + 1):
            print(f"Парсим страницу {page}")
            html = get_html(URL, params='page=' + str(page))
            cards.extend(get_content(html.text))
        print(cards)
        safe_doc(cards, JSON)
        pass
    else:
        print("Error")


parser()
