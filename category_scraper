import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)
category_link = []  # list of all the category links

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    ul = soup.find('ul', {'class': 'nav nav-list'}).select('li')

    # this loop gatter all category links
    for i in ul:
        a = i.find('a')
        category_link.append(a['href'])

    del category_link[0]  # remove the first link as it is a general category


def category_page(category_url, links=None, count=1):
    """
    :param count: this variable counts the number of pages visited
    :param links: list of all book links
    :param category_url: takes category's url
    :return: list of URLs for books in the specified category
    """
    if links is None:
        links = []

    category_html = requests.get(category_url)
    if category_html.ok:
        category_soup = BeautifulSoup(category_html.text, 'html.parser')

        # scrape page infos
        links.append(by_page_category(category_url))

        # other_page checks if the category spans multiple pages
        other_page = category_soup.find('ul', {'class': 'pager'})

        if other_page is None:
            pass

        # if there is other pages
        else:
            # next_page verify if the link trouvé leads to the next page
            next_page = other_page.find('li', {'class': 'next'})

            # if the link goes to the previous page
            if next_page is None:
                pass

            # if the link leads to the next page
            else:
                next_page_link = next_page.find('a')
                # page_extension will help remove extensions from previous web pages
                page_extension = ('page-' + str(count) + '.html')
                if 'index.html' in category_url:
                    count = count + 1
                    category_url.removesuffix('index.html')
                    category_page(category_url.removesuffix('index.html') +
                                  next_page_link['href'], links, count)

                else:
                    count = count + 1
                    category_url.removesuffix(page_extension)
                    category_page(category_url.removesuffix(page_extension) +
                                  next_page_link['href'], links, count)

    return links


def by_page_category(lien):
    """
    :param lien: single page link
    :return: list of books on a category page
    """
    reponse = requests.get(lien)
    if reponse.ok:
        category_soup = BeautifulSoup(reponse.text, 'html.parser')

        links = []  # list containing the links of one-page books by category
        tag_links = category_soup.findAll('h3')
        for tl in tag_links:
            a = tl.find('a')
            links.append(url + 'catalogue' + a['href'].removeprefix('../../..'))
        return links
