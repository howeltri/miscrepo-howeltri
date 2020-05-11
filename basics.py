# Vars start with letter or underscore and then consist of only nums, letters, underscores
# They're case-sensitive... you know that right?
# snake_case is the naming convention, stop using camelCase :(
# vars like __var__ are private and should be left alone
# None = nothing ~ like null
# Double vs Single quotes = they actually don't matter which, I thought they did :(
# You'd just need to do like this "To say 'really...'" or this "to say 'really really.'"
# Escape chars ~ \n, \"
# multiplying *= 5
# f strings -  looks like f"this is the {x} time that's happened"
# vars have truthiness and falsiness - 1 is true 0, empty, None = false
# comparisons == != > < >= <=
# and or not
# == = is the value/s the same while is = is the memory location the same
# range ~ typically used for for loops
# range(7) - 0 through 6
# range(1,8) - 1 through 7
# range(1, 10, 2) odds 1 to 10
# range(7, 0, -1) decrement
# break out of loops with: break
# list = [] ~ len(list) - OR ~ list(range(1,4))
# to decrement in lists its just list[-1] etc
# Remember the in method
#------------List Basics-----------------------
# Items in lists are mutable
# .append() - one item at the end to append (if you passed a list it would be a nested value
# .insert(<insertionPosition>, <val>) -
# .extend() - used for multiple items or to add another list
# .clear() - removes everything
# .pop(<index> or nothing) - removes last item by default or item at index specified
# .remove(<value>) - removes first occurrence of that value, throws error if not found
# .index(<value>) - returns index of the passed value
# .count(<value>) - nmumber of times value appears in list
# .reverse()
# .sort() - ascending order in place
# .join() - use as "<value>".join(<list>) to join together seperated by passed value
# Slices!
# list[start:end:step] - : need to be included or else it'll just return val at that index
# ex: list[1:] - index 1 to end OR list[-3:] returns last three values
# can make a copy in dif mem space with list2 = list[:]
# ex: list[2:4] or list[:3]
# finally count by 2 across a range ~ list[:10:2]
# reverse a list ~ list_r = list[::-1]
# can swap in lists by doing names[0], names[1] = names[1], names[0]
# --------------List Comprehension----------------------- see quickListCompExamples.py
# new_list_from_old = [num * 2 for num in numbers]
# [<your_operation> for <item_to_operate_on> in <list>]
# You can use conditional logic in there too!
# list2 = [num for num in numbers if num is True]
# even better
# list3 = [num*2 if num % 2 == 0 else num/2 for num in numbers]

answer0 = [num for num in [1,2,3,4] if num in [3,4,5,6]]
answer1 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
names = ["Ellie", "Tim", "Matt"]
answer2 = [name[0] for name in names]
numbers = [1,2,3,4,5,6]
answer3 = [num for num in numbers if num % 2 == 0]
answer4 =  [num for num in range(1, 101) if num % 12 == 0]
answer5 = [letter for letter in 'amazing' if letter not in 'aeiou']
answer6 = [[num for num in range(3)] for high_num in range(3)]
answer7 = [[num for num in range(10)] for high_num in range(10)]

# -------------nested lists---------------------------------
# nest_list = [[1,23,4][6,7,8,9]['hello','goodbye!']]
# nest_list[0][1] = 23
# nested list compreehension
# [[print(val) for val in upper_vals] for upper_vals in nested_list]
# --------------dictionaries---------------------------
# key value pair
# instructor = {
# "name": "Tristan",
# "dog": True,
# etc: etc
# }
# OR dict(name="cat", age=5)
# Access by instructor["name"] - throws error if the <val> isn't in there
# dict.values() - returns all values as a list
# can iterate through with [value for value in dict.values()]
# dict.keys() - returns all keys as a list
# dict.items() returns tuples but returns key and value for all
# iterate with for key, value in dict.items() OR [key, value for key, value in dict.items()]
# to check if in a dictionary... you guessed it "if phone in instructor" - CHECKS FOR KEYS!!! NOT VAL
# To check for vals - if 4 in instructor.values()
# .clear() - empty dictionary
# .copy() - clones with same vals but dif mem locations
# .fromkeys - fromkeys(<list_of_keys>, default_value_to_sign_to_each)
# .get(<key>) - returns value assigned to a key
# .pop(<key>)
# .popitem() - pops a random item
# .update() - adds every key value to that dictionary thats not already in it and will update any values that have that key
# ------------------Dictionary Comprehension------------ see dictComprehensionExamples.py
# squared_numbers = {key: value ** 2 for key,value in numbers.items()}
# basically {key:value for key,value in dictionary.items()}
# With conditional logic - {key:(value with logic - must include if and else) for value in dictionary.items()}
# conditional logic has to include if and else because it won't leave the key or value as None by default

new_dict = {num: num**2 for num in [1,2,3,4,5]}
instructor = {'name': "sam", 'city': 'ashburn', 'pal': 'scout'}
yelling_instructor = {key.upper():val.upper() for key, val in instructor.items()}
yelling_instructor_logic = {(key.upper() if key == "pal" else key):val.upper() for key, val in instructor.items()}
answer = {list1[i]:list2[i] for i in range(0, len(list1))}
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#The three of these would work
answer = {persons[0]:persons[1] for persons in person}
answer = {k:v for k,v in person}
answer = dict(person)
answer = {letter:0 for letter in 'aeiou'}
answer = {asc:chr(asc) for asc in range(65,91)}

#--------------------Tuples+Sets-----------------------------------
# tuple - ordered collection
# num = (1,2,3) - tuples are immutable - can't add to them or change
# faster than lists!
# data does not need to be unique
# tuple can be nested in a dict where list CAN NOT
# .count(<value>)
# .index(<value>)
# Sets - no duplicates and no order
# cannot acccess by index because there is no order
# set = {1,4,5, 'a'}
# .add(<value>) - throws no error if already in set
# .remove(<value>) - throws error if item isn't in there to remove
# .copy()
# .clear()
# Set Math
# set_name | 2ndset_name - only prints out unique from both
# set_name & 2ndset_name - only prints out values in both
# set comprehension
# {x**2 for s in range(10)} - no key, value because its a set and is not key value paired
#--------------------Functions--------------------------------------
# def name() or(<parameter>, ... n param) Default (<paramater>=<value>
# default values need to go at the end or they all need to have def values
# kwargs
# invoke a func like add_func(func=add, denominator=2)
# scope
# use global <var> to refer to a global variable inside your func
# if you're trying to call a variable from a nested function
# so calling a var in the function above you need to declare as nonlocal!
#--------------------docstrings--------------------------
"""This is a docstring and it will go for many many lines and more if you'd like"""
# also for help you can call these for any built in func and for any you have defined a docstring
# within
# like this func.__doc__
# right after your def put the doc string
# def func(<val>):
"""This is the docstring for instructions on running this"""
#------------------args and kwargs-------------------------
# *args - paramater we can pass to func with whatever we want
# collects any num of additional parameters and creates as a tuple
# could be named *<anything> but *args is standard
# when you reference the tuple it provides you just reference as args
# **kwargs
# stores as many as you want in a dictionary
# def fav_colors(**kwargs) or could be**anything
# fav_colors(colt="red",scout="green"...etc)
# parameter ordering
# parameters *args default parameters *kwargs
# example display(a,b,*args,instructor="ham",**kwargs)
# to unpack tuples and lists just add * in fromt of the variable and
# they'll be passed one at a time
# if i had list [1,4,6,7,3,1,54,7,89,0,7,4r3455,1] and wanted to pass into a func as indiv args
myFunc(*list)
# dictionary unpacking
# just do **<dict> when passing to a func
#--------------------Lambdas--------------------------------
# lambda is basically a no named one line function, called anonymous function in other languages
# ex: square_root = lambda <variable>: <variable> * <variable>
add = lambda a,b: a + b
# then you call these as you would a function
print(add(3,10))
# lambdas are super nice to just pass a no name function into another function
#--------------------map-----------------------------------
# GO BACK AND FINISH THIS SECTION



#--------------------debugging + error handling------------------
# common errors
# syntax, name (variable isn't defined), type (wrong type), index (out of range etc)
# value (recieves appropriate arg type but inaprop val in it
# Attribute error - variable does not have an attribute
# Raising our own errors
# can raise a variety of exceptions ~ most vague is raise Exception
# more specific is raise TypeErrorr("Oh no") or raise ValueError("Oh no again") etc
# could be a check for a func like ~ if type(color) is not str
#--------------------handling errors------------------------
# try:   ~ at its most basic
#   randomness
# except:
#   print("That's a no go")
# print("you tried")
#
try:
except NameError:
    print("var needs to be defined")
except ZeroDivisionError as err:
    print("Don't divide by 0")
    print(err)


def divide(num1, num2):
    try:
        a = num1 / num2
    except ZeroDivisionError:
        return "Please do not divide by zero"
    except TypeError:
        return "Please provide two integers or floats"
    return a
#
# try:
# except: #runs if try fails
# else:  #runs if try succeeds
# finally: # runs even if the previous ones had break statements
#
#--------------------Debugging------------------------------
# with pdb (python debugger)
import pdb; pdb.set_trace()
# can explore all values that are set and step through by pressing 'n' quit with 'q'
# 'c' to move all the way through
#--------------------Modules---------------------------------
# from random import randint as renamed_random
# renamed_random.choice(['fork','spoon'])
# to import specific things
# from random import choice, randint
# Important note
# import random = imports everything as attribute of random, so random.choice()
# vs from random import * = everything is imported into current namespace ~ choice()
#-------------------custom modules---------------------------
# import <fileName> without .py
#-------------------external modules------------------------
# use pip to install external then import normally
pip install -m autopep8
# then run from command line on your program
#--------------------__name__-----------------------------
# __main__ will be the __name__ if running that program
# but will be func name if running as an import!
# when imported all code is run
# so we need to do
if __name__ == "__main__":