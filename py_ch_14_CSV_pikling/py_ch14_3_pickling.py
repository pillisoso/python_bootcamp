
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
