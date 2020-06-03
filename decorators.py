# High Order Function
# Returns a func or accepts a func as an arg
# example
def calculator(n, func):
    return func(n)

def my_square(x):
    return x*x

print(calculator([7,2], sum))
print(calculator(7, my_square))

# Remember there can be nested functions

# Decorators are functions that wrap other functions to enhance behavior
# they are higher order funcs

# The concept of decorators is to wrap a function which could be done this way
def be_polite(fn):
    def wrapper():
        print("Pleasure to meet you")
        fn()
        print("Have a nice day")
    return wrapper

def greet():
    print("My name is ...")

greet = be_polite(greet)
# Here's the right way/easier

def be_polite(fn):
    def wrapper():
        print("Pleasure to meet you")
        fn()
        print("Have a nice day")
    return wrapper

@be_polite
def greet():
    print("My name is ...")

@be_polite
def rage():
    print("Go... AWAY!")

greet()
rage()

# Decorators with different signatures e.g. you're wrapping multiple types of functions that have a dif num args

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        pass
    return wrapper

# Preserving func metadata for your libraries! If you place a decorator on a method it will return the docstring of the wrapper
# So you need this!
from functools import wraps
def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        pass
    return wrapper

# Speed-test decorator
from functools import wraps
from time import time
def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f'Total time = {end - start} seconds for {fn.__name__}')
        return result
    return wrapper

@speed_test
def sum_nums_gen():
    return sum(x for x in range(10000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(10000000)])

print(sum_nums_gen())
print(sum_nums_list())

# Print all args as tuple and kwargs as dict

from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)

    return wrapper

from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [result, result]
    return wrapper

# You could use a wrapper to make sure no kwargs, no ints, no funcs, etc are passed!

from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        return fn(*args, **kwargs)
    return wrapper

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner

from functools import wraps

def ensure_authorized(fn):
    wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') == 'admin':
            return fn(*args, **kwargs)
        return 'Unauthorized'
    return wrapper


# if you need to pass a decorator an arg like
@decorator_with_arg(arg)
def func(*args, **kwargs):
    pass

# it's really
func = decorator_with_args(arg)(func)

# to construct this function there now needs to be another layer!

from functools import wraps

def ensure_first_arg_is(val): #extra layer
    def inner(fn):
        @wraps(fn)
        def wrapper():
            if args and args[0] != val:
                return f"First arg must be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner # extra layer

@ensure_first_arg_is('id')
def validate(id, secure_string):
    pass

# Enforce certain types of args

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
               newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)
# repeat_msg("hello", '5')
divide('1', '4')

from functools import wraps
from time import sleep

def delay(amt):
    def inner(fn):
        wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(amt, fn.__name__))
            sleep(amt)
            return fn(*args, **kwargs)
        return wrapper
    return inner