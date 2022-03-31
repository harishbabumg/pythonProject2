import sys
# class Teacher:
#     def setid(self, id):
#         self.id = id
#
#     def getid(self):
#         return self.id
#
#     def setname(self, name):
#         self.name = name
#
#     def getname(self):
#         return self.name
#
#     def setaddress(self, address):
#         self.address = address
#
#     def getaddress(self):
#         return  self.address
#
#     def setsalary(self, salary):
#         self.salary = salary


    # def getsalary(self):
    #     return self.salary

# inheriting from Teacher class

# class Student(Teacher):
#     def setmarks(self, marks):
#         self.marks = marks
#
#     def getmarks(self, marks):
#         return self.marks
#
# s = Student()
# s.setid(123)
# print(s.getid())

# s.setaddress('MuthyalammanaHalli, Madhugiri')
# print(s.getaddress())
#
# s.setsalary(1000)
# print(s.getsalary())
#
# print(s.setname("hb"))
# print(s.getname())

"""Constructors in inheritance"""

class Father:
    def __init__(self):
        self.property = 800000.00

    def display(self):
        print(f"Fathers's property: {self.property}")

class Son(Father):
    pass

# s = Son()
# print(s.property)
# s.display()

""" OVERRIDING """
# class Father:
#     def __init__(self):
#         self.property = 800000.00
#
#     def display(self):
#         print(f"father's property is {self.property}")
#
# class Son(Father):
#     def __init__(self):
#         self.property = 200000.00
#     def display(self):
#         print(f"Son's property is {self.property}")
#
# s = Son()
# print(s.property)
# s.display()

"""Overriding Super class constructors and methods"""

# class Father:
#     def __init__(self, property=0):
#         self.property = property
#     def display(self):
#         print(f"father's property is {self.property}")
#
# class Son(Father):
#     def __init__(self, property1=1000, property=0):
#         super().__init__(property)
#         self.property1 = property1
#
#     def display(self):
#         print(f"Son's property is {self.property1}, His father's propety is {self.property}")
#
# s = Father()
# # s.property = 10000
# # print(s.property)
# s.display()
#
# c = Son()
# # print(c.property1)
# c.display()

#  similar program

# class Square:
#     def __init__(self, x):
#         self.x = x
#
#     def area(self):
#         print(f'Area of square is {self.x * self.x}')
#
#
# class rec(Square):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self.y = y
#
#     def area(self):
#         super().area()
#         print(f"Area of rectangle is {self.x * self.y}")

# s = Square(55)
# s.area()
# r = rec(5, 10)
# r.area()

#
# a, b = [float(x) for x in input("Enter two measurements: ").split()]
# r = rec(a, b)
# r.area()

"""Single Inheritance"""

# class Bank(object):
#     cash = 100000000
#
#     @classmethod
#     def available_cash(cls):
#         print(cls.cash)
#
#
# class AndhraBank(Bank):
#     pass
#
#
# class StateBank(Bank):
#     cash = 20000000
#
#     @classmethod
#     def available_cash(cls):
#         print(cls.cash + Bank.cash)
#
#
# b = Bank()
# print(b.cash)
# b.available_cash()
#
# print()
# a = AndhraBank()
# print(a.cash)
# a.available_cash()
# print()
# s = StateBank()
# print(s.cash)
# s.available_cash()

"""Multiple Inheritance"""


# class Father(object):
#     def height(self):
#         print('Height is 6.0 feet')
#
#
# class Mother(object):
#     def colour(self):
#         print("Colour is brown")
#
#
# class Child(Father, Mother, object):
#     pass
#
#
# c = Child()
# c.colour()
# c.height()

"""when the child class has init contructor in it"""


# class A(object):
#     def __init__(self):
#         self.a = "a"
#         print(self.a)
#
# class B(object):
#     def __init__(self):
#         self.b = "b"
#         print(self.b)
#
#
#
# class C(A, B):
#     def __init__(self):
#         self.c = "c"
#         print(self.c)
#         super().__init__()


# c = C()
# Problem is only A's instance is called but not B's.

# class C(B, A):
#     def __init__(self):
#         self.c = "c"
#         print(self.c)
#         super().__init__()

# now the class B's instance is called
# c = C()

"""class C connot access all the super class's 
instances anytime to make use all the instance variable of bas class 
we have to use super().__init__() in every class """

# class A(object):
#     def __init__(self):
#         self.a = 'a'
#         print(self.a)
#         super().__init__()

# class B(object):
#     def __init__(self):
#         self.b = 'b'
#         print(self.b)
#         super().__init__()
#
# class C(A, B, object):
#     def __init__(self):
#         self.c = "c"
#         print(self.c)
#         super().__init__()
#
# c = C()

# print(B.mro())

"""MRO - several classes"""


# class A(object):
#     def method(self):
#         print("A class method")
#         super().method()
#
#
# class B(object):
#     def method(self):
#         print("B class method")
#         super().method()
#
#
# class C(object):
#     def method(self):
#         print("C class method")
#
#
# class X(A, B):
#     def method(self):
#         print("X class method")
#         super().method()
#
#
# class Y(B, C):
#     def method(self):
#         print("Y class method")
#         super().method()
#
#
# class P(X, Y, C):
#     def method(self):
#         print("P class method")
#         super().method()
#
#
# p = P()
# p.method()
# print(P.mro())