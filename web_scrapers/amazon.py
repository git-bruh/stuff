import requests
from bs4 import BeautifulSoup

headers = ({"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
            "/75.0.3770.100 Safari/537.36"})


def amazon_search(search_term):
    search_term = "+".join(search_term.split())
    url = f"https://www.amazon.in/s?k={search_term}"
    page = requests.get(url, headers=headers)
    content = BeautifulSoup(page.content, "lxml")
    names = content.findAll(class_="a-size-medium a-color-base a-text-normal")
    prices = content.findAll(class_="a-price-whole")
    name_list = []
    price_list = []
    for item in names:
        item = item.get_text()
        name_list.append(item)
    for item in prices:
        item = item.get_text()
        price_list.append(item)
    return name_list, price_list


print(amazon_search(input("Search Term\n> ")))
