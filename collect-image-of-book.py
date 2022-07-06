import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"
pnum_URL = "http://books.toscrape.com/catalogue/page-{}.html"
for i in range(50):
    URL = pnum_URL.format(i)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')
    tree = soup.find_all(
        "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for i in tree:
        img = i.find("img")["src"]
        book_name = i.find("img")["alt"]
        with open("pic/{}.jpg".format(book_name), "wb") as f:
            f.write(requests.get(URL+img).content)
