
# Courses: colt_py_bootcamps    331

# -------------    First Scraping Program    -------------
    # we scrap webpage, using Beautiful soup with requests
    # we write the data to a csv file

# we scrape following data from a site: Rithm-school
    # Titele
    # post link
    # date


# --------    Let's scrape data into a CSV!    --------
    # Goal: Grab all links from Rithm School blog 
    # Data: store URL, anchor tag text, and date

# it is crucial to analyze the "HTML-architecture" of the site and get the proper tags
    # To do this we'll use : "Chrome Inspect tool" / "Developer Tools"


# https://www.rithmschool.com/blog 
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.rithmschool.com/blog"

res = requests.get(URL)
print(res.text)
soup = BeautifulSoup(res.text, "html.parser")

res = requests.get(URL)
# print( response.text)
soup = BeautifulSoup(res.text, "html.parser") 
articles = soup.find_all("article")
# print(articles)


# find data and save it to a csdv file
with open("blog_data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file) 
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text() 
        url = a_tag['href']
        date = article.find("time")["datetime"] 
        csv_writer.writerow([title, url, date])
        print(title, url, date)


# -------- forbidden: problem ---------
# items = soup.find_all("jet-listing-grid__item")
# print(items)
# articles = items[1].find_all("jet-listing-dynamic-field__content")
# print(articles)

# python py_ch12_3_1_ext_prj_1.py

