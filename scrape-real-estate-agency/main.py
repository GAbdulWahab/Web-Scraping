
# Using BeautifulSoup to scrape a real estate agency website and generaate a CSV file based on the findings.


from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thwriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thwriter.writerow(header)

    for list in lists:
        title = list.find(
            'a', class_="listing-search-item__link--title").text.replace('\n', '')
        location = list.find(
            'div', class_="listing-search-item__location").text.replace('\n', '')
        price = list.find(
            'div', class_="listing-search-item__price").text.replace('\n', '')
        area = list.find(
            'li', class_="illustrated-features__item illustrated-features__item--surface-area").text.replace('\n', '')
        info = [title, location, price, area]
        thwriter.writerow(info)
