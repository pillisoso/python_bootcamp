

# Courses: colt_py_bootcamps    335, 336

# ------------------    Part 2 : GAME LOGIC (MOD: Play again & refactor)  ------------------
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



# game logic begins
def start_game():
    quote = choice(all_quotes)
    print("Here's aquote")
    print(quote["text"])
    remaining_guess = 4
    guess= ''
    print(quote["author"]) # for testing
    while guess.lower() != quote["author"].lower():
        guess = input(f"who said the qoute? Gesses Remaining : {remaining_guess} \n")
        if guess.lower() == quote["author"].lower():
            print("Correct!!")
            guess= ''
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
        

    # Play again Mechanism
    #  two way to do it:
        # Use another layer of while loop, where current while loop nested inside
            # Set a Boolian variable to controll the new while loop
            # Change the Boolian value by the 'play again mechanism'

        # Deine a function
            # trigger this function using "play again mechanism"
            # notice the following is also indented, it's part of the function

    again = " "
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")

    if again.lower() in ('y', 'yes'):
        print("Let's Play Again")
        return start_game()
    else:
        print("Ok, GOODBYE!")
     
start_game()

# python py_ch12_2_5_prj_p2_game.py
