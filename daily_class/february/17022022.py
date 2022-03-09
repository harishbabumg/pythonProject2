from time import time
from time import sleep
from collections import defaultdict

# def reverse(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result[::-1]
#         return result
#     return wrapper
#
# @reverse
# def add(a):
#     return a
#
#
# print(add("HBMG"))
#
#
# def positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, (float, int)):
#             return abs(result)
#         return result
#     return wrapper
# #
# @positive
# def greet():
#     return "hello"
#
# print(greet())
# #
# @positive
# def sub(a, b):
#     return a + b
#
# print(sub(-10, -60))
#
#
# time decorator
#
# from time import time
#
# def _time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(f"execution time of function {repr(func.__name__)} is {end-start} seconds")
#         return f"result of {repr(func.__name__)} is {result}"
#     return wrapper
#
# @_time
# def sub(a, b):
#     return a + b
# #
# print(sub(4,5))
#
#
#
#
#
# function and count decorator
#
# counts = defaultdict(int)
#
#
# def func_count(func):
#     def wrapper(*args, **kwargs):
#         counts[func.__name__] += 1
#         return func(*args, **kwargs)
#     return wrapper
#
# @func_count
# def greet():
#     return "Hello"
#
# @func_count
# def message():
#     return "Good_Morning"
#
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(counts)
#
# print(message())
# print(message())
# print(message())
# print(message())
# print(counts)



 # func.count
#
# def _func_count(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         func.count += 1
#         result = func(*args, **kwargs)
#         print(f"function {repr(func.__name__)} was invoked {func.count} times")
#         return result
#     return wrapper
#
# @_func_count
# def greet():
#     return "Hello"
#
# print(greet())
# print(greet())
# print(greet())
#
 # max_count

# def max_calss(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         func.count += 1
#         if func.count > 5:
#             raise ValueError(f"maximum calls to function {repr(func.__name__)} exceeded")
#         return func(*args, **kwargs)
#     return wrapper
#
# @max_calss
# def greet():
#     return "Hello Hari"
#
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# # print(greet())
# print(greet())
#
# repeat method
#
# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(2):
#             func(*args, **kwargs)
#             sleep(2)
#     return wrapper
#
#
# @repeat
# def greet():
#     print("Harisha")
#
#
# greet()
# #
# #
# @repeat
# def add(a, b):
#     print("hello")
#     print(a + b)
#
#
# add(1, 2)
#
# cache Decorator
# def cache(func):
#     func._cache = {}
#     def wrapper(*args, **kwargs):
#         if args in func._cache:
#             print("Getting result from cache")
#             return func._cache[args]
#         print("Executing func for the first time")
#         result = func(*args, **kwargs)
#         func._cache[args] = result
#         return result
#     return wrapper
#
# @cache
# def sub(a, b):
#     sleep(10)
#     return a - b
#
# @cache
# def mul(a, b):
#     sleep(15)
#     return a * b
#
# print(sub(100, 50))
# print(sub(200, 100))
# print(sub(100, 50))
# print(mul(100, 10))
# print(mul(10, 15))



#
# """To add the prefixes of +91- to numbers and return as it is for the numbers which starts with other than +91"""
#
# numbers = ([1234567890, 9087654532, 119876543210])
#
#
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith("91"):
#         str_number = "+" + str_number[:2] + "-" + str_number[2:len(str_number)]
#         return str_number
#     else:
#         return str_number
#
# #
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         temp = args[0]
#         processed_numbers = [add_prefix(number) for number in temp]
#         return func(processed_numbers)
#     return wrapper
#
#
# @prefix_country_code
# def print_number(phone_numbers):
#     for item in phone_numbers:
#         print(item)
#
#
# print_number(numbers)
#
#  parameterized decorators
#
# def spam(*names):
#     def _spam(func):
#         def wrapper(*args, **kwargs):
#             print(names)
#             return func(*args, **kwargs)
#         return wrapper
#     return _spam
#
#  Q) 1
#
# def validate(*expected_types):
#     def _validate(func):
#         def wrapper(*args, **kwargs):
#             for expected_type, actual_value in zip(expected_types, args):
#                 if not isinstance(actual_value, expected_type):
#                     raise TypeError()
#             return func(*args, **kwargs)
#         return wrapper
#     return _validate
#
#
# #  ORORORORORORORORORO
#
def validate_types(expected_types, actual_values):
    for expected_type, actual_value in zip(expected_types, actual_values):
        if not isinstance(actual_value, expected_type):
            raise TypeError()
#
#
#
def validate(*expected_types):
    def _validate(func):
        def wrapper(*args, **kwargs):
            validate_types(expected_types, args)
            return func(*args, **kwargs)
        return wrapper
    return _validate


@validate(float, float)
def sub(a, b):
    return a-b

print(sub(1.0, 1.0))

@validate(int, int)
def add(a, b):
    return a+b

print(add(1, 3))


@validate(str, str)
def greet(a, b):
    return f"There are {a} and {b} in group"

# print(greet("hai", "hello"))