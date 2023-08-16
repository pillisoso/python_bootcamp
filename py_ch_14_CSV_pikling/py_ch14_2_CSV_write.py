
# Courses: colt_py_bootcamps    315, 316

# --------------    Writing CSV    --------------
# we can write using "list" or 'ditioneries'

# Writing CSV Files Using "LISTS"
	# We use writer(), which creates a writer object for writing to CSV 
	# writerow() method on a 'writer' object to write a "ROW" to the CSV



# Example 1: Demo of writing a CSV file
from csv import writer

with open("fighters_2.csv", "w") as file: 
	csv_writer = writer(file)
	csv_writer.writerow(["Character", "Move"]) 
	csv_writer.writerow(["Ryu", "Hadouken"])
	csv_writer.writerow(["Ben", "Kadichi"])




# Example 2: Read from a file, change the data and store to another file
# scream.py
from csv import reader, writer
# using     "NESTED WITH"     statements
with open('fighters.csv') as input_file:
	csv_reader = reader(input_file) 	# data never converted to "list"
	with open('screaming_fighters.csv', "w") as output_file:
		csv_writer = writer(output_file)
		for fighter in csv_reader:		# can iterate only once
			# notice  "list-comprehension is used inside FOR-loop 
			# because we're dealing with list-of-lists"
			csv_writer.writerow([s.upper() for s in fighter])



# Examle 2 (Version 2): Other approach, with only 1 file open at a time
with open('fighters.csv') as file:
	csv_reader = reader(file)
	# data converted to list and saved to variable
	# notice "NESTED LIST COMPREHENSION"
	fighters = [[s.upper() for s in row] for row in csv_reader]

with open('screaming_fighters.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)






# ---------------    DictWriter    ---------------
# Not necessarily faster than the normal writer
	# More detailed/explicit code to easily understand

# DictWriter:
	# creates a writer object for writing using dictionaries 
	# fieldnames - 'kwarg' for the DictWriter specifying 'headers'
		# 'headers' is a "LIST" or "TUPLE"
	# writeheader - method on a writer to write 'header row '
	# writerow - method on a writer to write a 'row' based on a dictionary



# Example 3: Demo of using DictWriter
from csv import DictWriter 

with open("example.csv", "w") as file:
	heaDers = ["Character", "Move"]
	csv_writer = DictWriter(file, fieldnames=heaDers) 
	csv_writer.writeheader() 
	csv_writer.writerow(
		{
			"Character": "Ryu",
			"Move":	"Hadouken"
		}
	)




# Example 4: write cats.csv using DictWriter
from csv import writer, DictWriter
# ----    Version using "writer"    ----
# with open("cats.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])

# Version using DictWriter
with open("cats.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow(
		{
			"Name": "Garfield",
			"Breed": "Orange Tabby",
			"Age": 10
		}
	)




# Example 5: Inch to cm converter for fighters.csv
	# instead of NESTED "with" we open the files seperately
from csv import DictReader, DictWriter

# converter function from "inch" to "cm"
def cm_to_in(cm):
	return float(cm) * 0.393701		# notice the type-conversion

with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)		# its a 'list of dictionaries'
	# print(fighters)

with open("inches_fighters.csv", "w") as file:
	headers = ("Name","Country","Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for fitr in fighters:
		csv_writer.writerow(
			{
				"Name":fitr["Name"],
				"Country": fitr["Country"],
				"Height": cm_to_in(fitr["Height (in cm) "])		# notice the space
			}
		)




# Example 6: Print Users CSV Solution
import csv

def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))




# Example 7: Find User CSV Solution
import csv

def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = (first_name == row[0])
            last_name_match = (last_name == row[1])
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)




# -----------    enumerate    -----------
""" 
enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. 
This enumerated object can then be used directly FOR-loops or converted into a 'list of tuples' using the list() function. 

Syntax: 

	enumerate(iterable, start=0)


	Parameters:

		Iterable: any object that supports iteration
		Start: the index value from which the counter is to be started, by default it is 0

"""


# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))


# Return type: <class 'enumerate'>
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

