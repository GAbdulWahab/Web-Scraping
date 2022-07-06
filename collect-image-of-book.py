import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"
page_URL = "http://books.toscrape.com/catalogue/page-{}.html"
for i in range(50):
    current_URL = page_URL.format(i)
    r = requests.get(current_URL)
    soup = BeautifulSoup(r.content, 'lxml')
    tree = soup.find_all(
        "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for element in tree:
        img = element.find("img")["src"]
        book_name = element.find("img")["alt"]
        with open("pic/{}.jpg".format(book_name), "wb") as f:
            f.write(requests.get(URL+img).content)
