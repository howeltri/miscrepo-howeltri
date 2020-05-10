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
