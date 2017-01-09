# Animal is a object, look at the extra credit

class Animal(object):
	pass

# Dog is an Animal
class Dog(Animal):
	def __init__(self, name):
		# Deach og has a name
		self.name = name

# Cat is an Animal
class Cat(Animal):
	def __init__(self, name):
		# Each Cat has its own name
		self.name = name

# Person is a Animal
class Person(object):
	def __init__(self, name):
		# each person has one's own name
		self.name = name

		# Person has a pet of some kind
		self.pet = None


# Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
		# 
		super(Employee, self).__init__(name)
		##
		self.salary = salary

#
class Fish(object):
	pass

class Salmon(Fish):
	pass


class Halibut(Fish):
	pass

# rover is a Dog
rover = Dog("Rover")

# satan is a cat
satan = Cat("Satan")

# mary is a personl
mary = Person("Mary")

mary.pet = satan

# frank is a person and also a employee
frank = Employee("Frank", 12000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

