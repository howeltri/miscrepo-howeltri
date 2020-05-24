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

