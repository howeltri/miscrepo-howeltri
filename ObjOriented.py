# class - blueprint of objects
# object - instance of a class
# abstraction - expose only relevant data in a class interface hiding private attributes + methods from user
# encapsulation - place code into logical, hierarchial groupings using classes
# private attributes/methods should be designated with a leading _
#


# ----------------__init__--------------------
# python will auto execute __init__
# self refers to the specific current instance of this class that you initilaize eg user
#
class User:

    active_users = 0
    allowed ages = list(range(0,100))

    def __init__(self, name, age):
        self.name = name
        self.age = age
        user.active_users += 1

    def pup__birthday(self):
        return f"Happy Birthday {self.name}, you are now {self.age + 1} years old!"

# Define the Comment class below:
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

user1 = User('Scout', 2)
user2 = User('Ham', 7)
print(f"A pup by the name of {user2.name} at the young age of {user2.age}")

print(user.active_users)

# __<val>__ - only when you're overwriting something python auto looks for
# _<val> - this is supposed to be private - only supposed to be used for other defs in the class
# __<val> - this is called name mangling and you will not be able to access outside with that name
# it just adds the class name so there's no conflict when that method is inherited


# Class Attributes
# these are specific to an entire class not one instance of it. For instance
# each time a new user is created increment total user count


class Chicken:
    total_eggs = 0

    @classmethod
    def get_egg_count(cls):
        return f'We got some serious eggs out here: {cls.total_eggs}'

    # This could be a pretty handy use for class methods!
    @classmethod
    def define_chix_from_string(cls, data_string):
        name, species = data_string.split(',')
        cls(name, species)
        # Basically should just initiliaze a chicken from a string since we don't want to intitialize regularly
        # or we're doing a LOT of chickens!

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1


# Class Methods
# performs ops on overall class not instances
# specified via @classmethod decorator

@classmethod
    def define_chix_from_string(cls, data_string):
        name, species = data_string.split(',')
        cls(name, species)
        # Basically should just initiliaze a chicken from a string since we don't want to intitialize regularly
        # or we're doing a LOT of chickens!

# __repr__ - provides a nice string representation

def __repr__(self):
    return self.name


#----------------------Inheritance--------------------------------------------------
# basees or parent classes
# inherit from
class Cat(Animal):

#-----------------------Properties--------------------------------------------------
# designate with @property
# normally used for getter functions
@property
def age(self):
    return self._age

print(obj.age)

# @ .setter
# method that takes attribute.setter
# changes value

@age.setter
def age(self, new_age):
    self._age = new_age

jane.age = 23



#----------------------Super()----------------------------------------------------
def __init__(self, attributes, attribute)
    super().__init__(attributes):
    self.attribute = attribute

# initializes inheritited based on parent
# super only helps initialize attributes
# methods are available just from passing the parent into class definition

#--------------------Multiple Inheritance-------------------------------------------
# Normally not used a whole lot, tends to complicate
# object can have multiple parents
class Penguin(Land, Sea):

# uses super().__init__ from the first arg class passed
# if we also wanted Sea class init its just
Sea.__init__(self, blah)

# ------------------------ Method Resolution Order-----------------------------\
# where it looks for methods first
# reference with __mro__
# mro()
# help(cls)

# Define your classes below:
class Mother():
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Father():
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Child(Mother, Father):
    def __init__(self, eye_color, hair_color, hair_type):
        super().__init__(eye_color, hair_color, hair_type)

#Alternate way

class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    pass

#Child will have mother attributes

#---------------------------Polymorphism--------------------
# an objects ability to take many forms
# the same class method work in a similar way for different classes
# OR same operation works for different kinds of objects
# example: len can work with tuples strings and lists

# Override method, rewrite same method in child classes to perform behavior

class Animal():
    def speak(self):
        raise NotImplementedError("Great when we want something defined at the lower levels")

class Shark(Animal):
    def speak(self):
        return 'Not really speaking but CHOMPING'

class Sea_Urchin(Animal):
    def speak(self):
        return 'Not really speaking but URCHINING'

#---------------------dunder methods-----------------------------
# for your classes you can redefine all sorts of dunder methods to do whatever you'd like!
# like __repr__ or __len__ or __add__ etc etc!


