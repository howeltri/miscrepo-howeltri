# Iterators
# any object that can be iterated upon. Can call next() on until the end
# Iterable
# Returns an iterator

# Iterables will be converted with iter() then will continually have next() called on them
# list string tuple etc are all iterable but need to be changed to iter() before next() can sequence through

# Writing a Custom Iterator
# In your class you can redefine both __iter__ and __next__


# Generators are iterators
# created with generator function
# use yield keyword
# can be created with generator expressions

# where functions use return generators use yield
# func can return once gen can yield many times
#  func returns return val where gen returns generator

# when a generator is created it will always have a static value at yield,m when next() is called on it then it will run
# until it again yields

def week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day

day = week()
next(day)
Monday
next(day)
Tuesday
etc etc

#Generators are really handy for reducing memory even though at times they're slower than lists
g = (num for num in range(1,10))
next(g)
