import math

"""Duck typing philosophy of Python"""


# class Duck(object):
#     def talk(self):
#         print("Quack Quack")
#
#
# class Human(object):
#     def talk(self):
#         print("Namasthe, Hello, Hi")
#
#
# class Dog(object):
#     def bark(self):
#         print("Bow! Bow!")
#
#
# def call_talk(obj):
#     obj.talk()
#
#
# x = Duck()
# call_talk(x)  # Duck().talk()
#
# y = Human()
# call_talk(y)

# z = Dog()
# call_talk(z)  # AttributeError: 'Dog' object has no attribute 'talk'

# now it should work fine

# def call_talk(obj):
#     if hasattr(obj, 'talk'):
#         obj.talk()
#     elif hasattr(obj, 'bark'):
#         obj.bark()
#     else:
#         print("Wrong object passed")
#
#
# x = Duck()
# call_talk(x)  # Duck().talk()
#
# y = Human()
# call_talk(y)
#
# z = Dog()
# call_talk(z)

"""OPERATOR OVERLOADING"""

#  addition to add the pages of the book

class Bookx:
    def __init__(self, pages):
        self.pages = pages

class Booky(object):
    def __init__(self, pages):
        self.pages = pages
#
# b1 = Bookx(40)
# b2 = Booky(60)
# b1 + b2  # TypeError: unsupported operand type(s) for +: 'Bookx' and 'Booky'

#  so we are here to overload the "+" operator to add two class object by overloading __add__ magic method

# def __add__(self, other):
#     return self.pages + other.pages


# class Bookx:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
# class Booky(object):
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return self.pages + other.pages  # __add__ should be in both classes to add in (a + b) and (b + a)


# b1 = Bookx(40)
# b2 = Booky(60)
# print(b2 + b1)


#  overloading the > greater symbol to addthe classes of Ramayana and Mahabharatha
# class Ramayana(object):
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#
# class Mahabharatha(object):
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
# print(1>2)
#
# r = Ramayana(1000)
# m = Mahabharatha(2000)
#
# print(m>r)


# Overloading the "*" multiply operator for our next program

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __mul__(self, other):
#         return self.salary * other.days
#
#
# class Attendance(object):
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
#
#     def __mul__(self, other):
#         return self.days * other.salary
#
#
# # print(10*10)
#
# e = Employee("HB", 1000)
# a = Attendance("HB", 20)
# print(e*a)

"""METHOD OVERLOADING"""

# class Myclass:
#     def sum(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             print(f"Sum of three= {a+b+c}")
#         elif a!=None and b!=None:
#             print(f"Sum of two= {a+b}")
#         else:
#             print('Please enter any two or three values')

# m = Myclass()
# #
# (m.sum(1, 5, 45))
# m.sum(1.2, 5.3, 5.001)

"""METHOD OVERRIDING"""

# import math
# from math import pi
# #
# class Square(object):
#     def area(self, x):
#         print(f"Area of square = {x * x}")
#
# class Circle(Square, object):
#     def area(self, x):
#         print(f"Area of a circle = {pi * x * x}")
#
#
# s = Square()
# s.area(15)
# c = Circle()
# c.area(10)



