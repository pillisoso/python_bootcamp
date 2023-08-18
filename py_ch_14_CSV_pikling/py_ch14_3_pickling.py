
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




# -------------------    JSON Pickling    -------------------
# ----------    json    ----------
# since JSON used in web development, we can use JSON-pickling to work with other languages

# python has "json" module
    #  it will encode and decode "python" to "json"

# json.dumps
    # not all python entity will converted to json
        # for example "tuple" will be concerted to a "List"  
        # "None" will convertred to "null"
    # json.dumps formats a python object as a STRING of JSON.



# Example 2: json.dumps demo
import json

j  = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) 
print(j)    # ["foo", {"bar": ["baz", null, 1.0, 2]}]

# we can write a file using json.dumps and use it in 'web developmnet'




# Example 3: json.dumps for CLASS
            
# there is no easy way to save a class definintion
    #  but we can save it in dictionary format

import json

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

jd = json.dumps(c.__dict__)     # convert it to dictionary and then json
print(jd)   # {"name": "Charles", "breed": "Tabby"}





# ----------    jsonpickle    ----------
#  its not a official python module
    # we need to install it using 'pip install' from pypi
    # its more like 'pickle'  but it serialize/desrialize as json

# usage:
    # create an object 
    # use "jsonpicle.encode" to transform into a "json-string"
    # use "jsonpicle.decode" to reconstruct a python object



# Example 4: worind with "jsonpickle"

import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

frozen = jsonpickle.encode(c)
print(frozen)   # {"py/object": "__main__.Cat", "name": "Charles", "breed": "Tabby"}
# Notice the "py/object": "__main__.Cat", it useful to recreate python object

# To JSONPICKLE 'c' the cat:
with open("cat.json", "w") as file:
	file.write(frozen)

# To bring back 'c' the cat using JSONPICKLE
with open("cat.json", "r") as file:
	contents = file.read()
	unfrozen = jsonpickle.decode(contents)  # re-creates a python object
	print(unfrozen)     # <__main__.Cat object at 0x000001DDCB6B3E90>




# Example 5 (CSV): Update Users Solution
import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if (row[0] == old_first) and (row[1] == old_last):
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(count)




# Example 6 (CSV): Delete Users CSV Solution
import csv

def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if (row[0] == first_name) and (row[1] == last_name):
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)



