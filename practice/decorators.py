# from time import time
# from time import sleep
import time

#
# """print * 10 times before and after the output of some function"""
# def my_decorator(func):
#     def wrapper_function(*args, **kwargs):
#         print("*"*10)
#         func(*args, **kwargs)
#         print("*"*10)
#     return wrapper_function
#
#
# @my_decorator
# def say_hello():
#     print("Hello")
#
#
# @my_decorator
# def say_bye():
#     print("Bye")
#
#
# say_hello()
# say_bye()

# """execution time of the function object passed"""
from time import time

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {repr(func.__name__)} executed in {(t2-t1):.4f} seconds')
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f} seconds')  # anyone can be used
        return result
    return wrap_func
#
#
@timer_func
def long_time(n):
    for i in range(n):
        for j in range(1000000):
            i*j
#
#
long_time(5)
#
# """write a decorator to input some delay before executing any function"""
#
# import time
#
#
# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(3)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @delay  # display = delay(display)
# def display():
#     return "taking 3 seconds of time"
#
# @delay
# def message():
#     return "hello"
#
#
# print(display())
# print(message())
#

"""Write a decorator which takes a string and reverse it."""

# def rev_str(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
#
# @rev_str
# def string(message):
#     return message
#
#
# print(string("012345"))

# """ Write a decorator which executes a function for 'n' times. """
#
#
# def outer(n):
#     def n_time(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return n_time
#
#
# @outer(3)
# def sent(a, b):
#     print(a+b)
#
#
# sent(1, 3)
#
# """write a decorator which inputs a delay of 'n' seconds"""
# import time
#
# def outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return delay
#
#
# @outer(3)
# def add(a, b):
#     print(a+b)
#
# add(1, 2)
