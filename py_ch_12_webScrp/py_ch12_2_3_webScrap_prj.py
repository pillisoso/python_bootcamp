
# Courses: colt_py_bootcamps    332, 334

# ----------------    Beautiful Soup: Web Scraping Project    ----------------

# We'll build a quotes guessing game. 
    # When run, your program will scrape a website for a 'collection of quotes'. 
    # Pick one at random and display it. 

# The player will have 'four chances' to guess who said the quote. 
    # After every wrong guess they'll get a hint about the author's identity.



# Requirements
# Create a file called "scraping_project.py" which, when run, 'grabs data' on every quote from the website 
    # http://quotes.toscrape.com

# You can use 'bs4' and 'requests' to get the data. 
    # For each quote you should grab the 'text' of the quote, 
    # the 'name of the person' who said the quote, and 
    # the 'href' of the link to the person's bio. 
    # Store all of this information in a 'list'.

# Next, display the quote to the user and ask who said it. 
    # The player will have four guesses remaining.
        # After each incorrect guess, the number of guesses remaining will decrement. 
        # If the player gets to zero guesses without identifying the author, the player loses and the game ends. 
        # If the player correctly identifies the author, the player wins!

# After every incorrect guess, the player receives a hint about the author. 
    # For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and 
        # tell the player the author's birth date and location.
    # The next two hints are up to you! Some ideas: 
        # the first letter of the author's first name, 
        # the first letter of the author's last name, 
        # the number of letters in one of the names, etc.

# When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.


# Keep your code as simple as posiible




# Go to the web page, notice the 'next' button, we'll be using it to get to the last page



# ------------------    Part 1 : SCRAPE (modification 1)   ------------------

# Tricky staff: Find the "next" button
    # Grab the data from all page, untill there is no next button

# http://quotes.toscrape.com
# pip install requests
import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"
page_url = "/page/1/"

# rq = requests.get("http://quotes.toscrape.com")


""" 
# work with MOCKED HTML
from bs4 import BeautifulSoup
import data_str
html_str = data_str.mocked_html
soup = BeautifulSoup(html_str, 'html.parser')
# ---------------------
"""



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

print(all_quotes)

# Tricky staff: Find the "next" button
    # Grab the data from all page, untill there is no next button





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


# ----------------    save using JSONPICKLE    ----------------

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



# ----------------    save using CSV: DictWriter & DictReader    ----------------

# To write scrapped data using "CSV"
from csv import DictWriter

def write_quote(qts):
    with open("quotes.csv", "w", encoding="utf-8") as file: 
        headers = ["text", "author", "bio-link"] 
        csv_writer = DictWriter(file, fieldnames = headers) 
        csv_writer.writeheader()
        for quote in qts:
            csv_writer.writerow(quote)

# write_quote(qts=all_quotes)



# reading from CSV
from csv import DictReader

def read_quote(filename):
    with open(filename, "r", encoding="utf-8") as file: 
        csv_reader = DictReader(file) 
        for quote in csv_reader:
            print(quote)
        return list(csv_reader)
    
qts_csv_lst = read_quote("quotes.csv")






# ------------------    Part 2 : GAME LOGIC   ------------------
# select random quote
# Check for the right answer
# give 4 chances and hints
# finally ask the user to end the game

import requests
import jsonpickle
from random import choice
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"

# To bring back data using JSONPICKLE
with open("all_quotes.json", "r") as file:
	contents = file.read()
	all_quotes = jsonpickle.decode(contents)  # re-creates a python object

quote = choice(all_quotes)
print("Here's aquote")
print(quote["text"])


# game logic begins
remaining_guess = 4
guess= ''
print(quote["author"]) # for testing
while guess.lower() != quote["author"].lower():
    guess = input(f"who said the qoute? Gesses Remaining : {remaining_guess} \n")
    if guess.lower() == quote["author"].lower():
         print("Correct!!")
         break
    
    remaining_guess -= 1
    if remaining_guess == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        res_soup = BeautifulSoup(res.text, 'html.parser')
        # print(res_soup.body)
        # Birth & Location scraping\
        birth_date = res_soup.find(class_ = "author-born-date").get_text()
        birth_place = res_soup.find(class_ = "author-born-location").get_text()
        print(f"Hint: \n author birth-date : {birth_date} \n author birth-place : {birth_place}")
    elif remaining_guess == 2:
        print(f"Hint: \n author's first name's first letter : {quote['author'][0]}")
    elif remaining_guess == 1:
        last_initial = quote['author'].split(" ")[1][0]
        print(f"Hint: \n author's Last name's first letter : {last_initial}")
    elif remaining_guess == 0:
        print(f"sorry, you ran outta guesses. \n answer is: {quote['author']}")
        break
    

