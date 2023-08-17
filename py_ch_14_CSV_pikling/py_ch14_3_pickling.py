
# Courses: colt_py_bootcamps    320, 321

# -------------------    Pickling    -------------------
# NOTE: it works with PYTHON
    # dont use pickle file with other language (JAVA or C++ or JS)
# its not related to "CSV"
# its related to FILIO

# if we have python data or python object
# it stores the current state of data into a file
# for example we're saving some csv data during web scrapping

# we have to use pickle module
    # it creates a pickle file
    # Data is "serialized" into byte-stream
    # we can then un-pickle the data whenever we want



# Example 1 : Pickling demo
import pickle

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
    # NOTICE: the binary writing mode "wb"
with open("pets.pickle", "wb") as file:
	pickle.dump(blue, file)

# To unpickle something:
# commentout the writing pickle file
    # NOTICE: the binary reading mode "rb"
with open("pets.pickle", "rb") as file:
	zombie_blue = pickle.load(file)
	print(zombie_blue)
	print(zombie_blue.play())


# NOTE:we actually do not use pickle to store user data in web development
    # it's just a quick way to store and grabbing data



# ---------    321 revw


# -------------------    JSON Pickling    -------------------
# since JSON used in web development, we can use JSON-pickling to work with other languages

start 1:00

# json demo

import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

# To JSONPICKLE 'c' the cat:
with open("cat.json", "w") as file:
	frozen = jsonpickle.encode(c)
	file.write(frozen)

# To bring back 'c' the cat using JSONPICKLE
# with open("cat.json", "r") as file:
# 	contents = file.read()
# 	unfrozen = jsonpickle.decode(contents)
# 	print(unfrozen)




# json pickling
import json

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed
		
c = Cat("Charles", "Tabby")

# json.dumps returns a JSON STRING:

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# results in '["foo", {"bar": ["baz", null, 1.0, 2]}]'

j = json.dumps(c.__dict__)
# results in '{"name": "Charles", "breed": "Tabby"}'





Update Users Solution
import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(count)






Delete Users CSV Solution
import csv

def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)




