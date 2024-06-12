import requests
from bs4 import BeautifulSoup


class Page:
    def __init__(self, url):
        self.url = url  # This is the url of the book page
        html = requests.get(self.url)
        soup = BeautifulSoup(html.content, 'html.parser')

        self.title = soup.find('h1').text  # Here are the book title
        # scrape book cover URL 
        self.image_url = 'http://books.toscrape.com' + soup.find('img')['src'].removeprefix('../..')
        # scrape book category
        self.category = soup.findAll('li')[2].text.replace('\n', '')
        # scrape book description
        self.product_description = soup.find('article', {'class': 'product_page'}).select('p')[3].text

        # to scrape infos related to the book
        product_info = soup.findAll('tr')
        self.upc = product_info[0].find('td').text  # product code of the book
        self.price_excluding_tax = product_info[2].find('td').text  # book price without taxes
        self.price_including_tax = product_info[3].find('td').text  # book price with taxes
        self.number_available = product_info[5].find('td').text  # amount of available books
        self.review_rating = product_info[6].find('td').text  # book rating
