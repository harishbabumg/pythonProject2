from time import time


# Write decorator that logs a message before executing any function


#  generic structure
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print("string")
#         func(*args, **kwargs)
#     return wrapper
#
# write a decorator to input some delay before executing any function

# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(0)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @delay  # display = delay(display)
# def display():
#     return "In display"
#
#
# print(display())

# Write a decorator which takes a string and reverse it.
# def reverse_(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
#
# @reverse_
# def spam(string):
#     return string
#
#
# print(spam("hello"))
#
# Write a decorator to execute a function for three times

#  Write a decorator which executes a function for 'n' times
# def outer(n):
#     def repeat_(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return repeat_
#
#
# @outer(3)  # @repeat_
# def add(a, b):
#     print(a + b)
#
# add(1, 2)
#
# @outer(2)
# def sub(a, b):
#     print(a - b)
# #
# sub(10, 4)

# write a decorator which inputs a delay of 'n' seconds

# def outer_(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return delay
#
#
# @outer_(3)     # @report_
# def add(a, b):
#     print(a + b)
#
#
# add(1, 2)
#
#
# @outer_(2)
# def sub(a, b):
#     print(a - b)
#
#
# sub(10, 8)

#  Write a decorator function that calculates time of execution of a function
# import time
# from time import time
# from time import sleep
#
#
# def outer_(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             start = time()
#             # time.sleep(n)
#             func(*args, **kwargs)
#             end = time()
#             print(f"time of execution is: {end - start}")
#         return wrapper
#     return delay
#
#
# @outer_(2)
# def sub(a, b):
#     print(f"output is: {a - b}")
#
# sub(1, 2)

#  assignments

# def function_decorator(func):
#     def wrapped_func(*args, **kwargs):
#         print('=' * 30)
#         func(*args, **kwargs)
#         print('=' * 30)
#     return wrapped_func()
#
#
# @function_decorator
# def test():
#     print('Hello World!')

#####################################################
#
#
# def function_decorator(func):
#     def wrapped_func(*args, **kwargs):
#         num = func(*args, **kwargs)
#         return abs(num)
#     return wrapped_func
#
#
# @function_decorator
# def test(a, b):
#     res = (a - b)
#     return res
#
# print(test(3, 5))
