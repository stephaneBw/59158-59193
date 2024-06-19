import csv
import os
import requests

from category_scraper import category_link, category_page
from book_page_scraper import Page

# URL of the website to scrape
url_link = 'http://books.toscrape.com/'

# list who contains scraped information headers
info_id = ['product_page_url', 'title', 'universal_ product_code (upc)',
           'price_including_tax', 'price_excluding_tax', 'number_available',
           'review_rating', 'product_description', 'category', 'image_url']

# the loop visit each book category on the site 'http://books.toscrape.com/'
for cl in category_link:
    # retrieve all the links of the books in the category
    # links contains all the links of the books in the category,
    # these links are grouped by web page in the category.
    links = category_page(url_link + cl, links=None)

    # nom_fichier est le nom que va prendre le fichier csv pour chaque category
    file_name = str(cl[25:].removesuffix('/index.html')) + '.csv'
    category_infos = []  # va contenir les données de tous les livres d’une category
    images = []  # va contenir les urls et les titres des images de couverture

    # pour chaque page de la category
    for page in links:
        # pour chaque livre de la page
        for link in page:
            p = Page(link)  # infos for one book
            # add book infos to the category list
            category_infos.append([p.url, p.title, p.upc, p.price_including_tax,
                                   p.price_excluding_tax, p.number_available, p.review_rating,
                                   p.product_description, p.category, p.image_url])
            images.append([p.title, p.image_url])

    # putting infos in a csv file
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=info_id)
        writer.writeheader()
        for i in category_infos:
            di = {}
            for c in range(0, 10):
                di[info_id[c]] = i[c]
            writer.writerow(di)

    # download cover images
    cwd = os.getcwd()
    try:
        new = file_name.removesuffix('.csv') + '_images'
        os.mkdir(os.path.join(cwd, new))
    except FileExistsError:
        print('dans le repertoire courant, il y a un dossier qui a le même nom : ',
              file_name + '_images')
        new = input('Veuillez entrer un autre nom manuellement : ')
        os.mkdir(os.path.join(cwd, new))

    # to acces the new folder to put the covers images
    os.chdir(os.path.join(cwd, new))

    # scraper les photos de couverture
    for s in images:
        img_name = s[0][:7].replace(':', '-').replace('/', '_').replace("\'", ' ')
        with open(img_name.replace('"', '').replace("'", '') + '.jpg', 'wb+') as image_file:
            image_file.write(requests.get(s[1]).content)
    os.chdir(cwd)
    print('la category ', file_name.removesuffix('.csv'), ' est termine')