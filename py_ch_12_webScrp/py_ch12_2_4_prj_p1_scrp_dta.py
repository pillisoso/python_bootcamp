
# ------------------    Part 1 : SCRAPE (modification 2)   ------------------
# modification 1:
    # Tricky staff: Find the "next" button
        # Grab the data from all page, untill there is no next button


# modification 2:
    # Use "SLEEP TIMER" to be more polite:
    # save to a file

from time import sleep

# http://quotes.toscrape.com
# pip install requests
import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"
page_url = "/page/1/"

# rq = requests.get("http://quotes.toscrape.com")

all_quotes = []

while page_url:
    print(f"Now scrapping: {base_url}{page_url}")
    rq = requests.get(f"{base_url}{page_url}")
    soup = BeautifulSoup(rq.text, 'html.parser')

    quotes = soup.find_all(class_="quote")
    # print(quotes)
    # print(quotes[0])

    for quote in quotes:
        all_quotes.append(
            {
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"] # Grabbing URL: bio-link (about)
            }
        )

    next_btn = soup.find(class_ = "next") 
    if next_btn:
        page_url = next_btn.find("a")["href"] 
    else:
        page_url = None

    # above can be also written as:
    # page_url = next_btn.find("a")["href"] if next_btn else None
    
    # To avoid attention
    # To avoid overload the server
    sleep(2)    # sleep 2 second to prevent BLOCKING



print(all_quotes)

# NOTE: It's a good idea to save the data into a file
import jsonpickle

frozen = jsonpickle.encode(all_quotes)
print(frozen) 

# save to a file
with open("all_quotes.json", "w") as file:
	file.write(frozen)


# # To bring back data using JSONPICKLE
# with open("all_quotes.json", "r") as file:
# 	contents = file.read()
# 	unfrozen = jsonpickle.decode(contents)  # re-creates a python object
# 	print(unfrozen)     # <__main__.Cat object at 0x000001DDCB6B3E90>


# python py_ch12_2_4_prj_p1_scrp_dta.py