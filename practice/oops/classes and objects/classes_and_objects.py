
# class Student():
#     def __init__(self, name="", marks = 0, age = 0):
#         self.name = name
#         self.marks = marks
#         self.age = age
#
#     def display(self):
#         print(f"Hi, {repr(self.name)}")
#         print(f"Your marks is '{self.marks}'")
#         print(f"Your age is '{self.age}'")
#
#     def calculate(self):
#         if (self.marks) >= 600:
#             print("You got first grade")
#         elif (self.marks) >= 450:
#             print("You got second grade")
#         elif (self.marks) >= 350:
#             print("You got third class")
#         else:
#             print("You are failed")
# # #
# # #
# n = int(input("How many students ? "))
# i = 0
# while (i < n):
#     name = input("Enter name: ")
#     marks = int(input("Enter marks: "))
#     print("------------------------------------------------")
#     s = Student(name, marks)
#     s.display()
#     s.calculate()
#     i += 1
#     print("------------------------------------------------")
# #
# s1 = Student("Harish Babu M G", 600, 25)
# s1.display()

# accessor and mutator without the constructor

# class Student():
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setMarks(self, marks):
#         self.marks = marks
#
#     def getMarks(self):
#         return marks
#
#
# n = int(input("How many students are there? "))
# i = 0
# while (i<n):
#     s = Student()
#     name = input("Enter name: ")
#     s.setName(name)
#     marks = int(input("Enter marks: "))
#     s.setMarks(marks)
#     i = i + 1
#
#     print(f"Hi, {s.getName()}")

# class methods

# class Bird:
#     wings = 2 # variables
#
#     @classmethod
#     def fly(cls, name):
#         print(f"{name} flies with '{cls.wings}' wings")
#
# Bird.fly("Sparrow")

# static method

# class Myclass:
#     n = 0
#     def __init__(self):
#         Myclass.n = Myclass.n+1
#
#     @staticmethod
#     def noObjects():
#         print(f"No. of instances created: {Myclass.n}")
#
#
# a = Myclass()
# b = Myclass()
# aa = Myclass()
# ba = Myclass()
# Myclass.noObjects()  # No. of instances created: 2

# import math
# class Sample:
#     @staticmethod
#     def calculate(x):
#         result = math.sqrt(x)
#         return result
# num = float("49.00000005")
# res = Sample.calculate(num)
# print(f"The Square Root of {num} is {res}")

# BANK class
# import sys
# #
# class Bank(object):
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('Insufficient balance')
#         else:
#             self.balance -= amount
#         return self.balance
#
# name = input("Enter the customer name: ")
# new_customer = Bank(name)
# #
# while True:
#     print("Select any one of -> d - Deposit, w - Withdraw, e - Exit, b = Balance")
#     choice = input("Your choice: ")
#     if choice == "e" or choice == "E":
#         sys.exit()
#     elif choice == "d" or choice == "D":
#         amount = float(input("Enter the amount you want to deposit: "))
#         if amount <= 0:
#             print("<<<Amount cannot be less than or equal to ZERO>>>")
#             print("<<<Please enter the correct amount>>>")
#             continue
#         print("________________________________________________________________")
#         print(f"The balance after the deposit is {new_customer.deposit(amount)}")
#         print("________________________________________________________________")
#     elif choice == "w" or choice == "W":
#         amount = amount = float(input("Enter the amount you want to withdraw: "))
#         if amount <= 0:
#             print("<<<Amount cannot be less than or equal to ZERO>>>")
#             print("<<<Please enter the correct amountn>>>")
#             continue
#         print("________________________________________________________________")
#         print(f"the balance after the withdraw {new_customer.withdraw(amount)}")
#         print("________________________________________________________________")
#
#     elif choice == "b" or choice == "b":
#         print("________________________________________________________________")
#         print(f"The present balance {new_customer.balance}")
#         print("________________________________________________________________")
#     else:
#         print("'Select the valid option'")
#         continue

# Passing the one class attribute to another

# class Employee:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = int(salary)
#
#     def display(self):
#         print(f"ID ={self.id}")
#         print(f"name= {self.name}")
#         print(f"salary= {self.salary}")
#
# class Myclass:
#     @staticmethod
#     def mymethod(e):
#         e.salary += 1000
#         e.display()
# #
# #
# e = Employee("123", "HB", 26000)
# Myclass.mymethod(e)

# calculate power with help of static method

# class Myclass:
#     @staticmethod
#     def mymethod(x, n):
#         result = int(x) ** int(n)
#         print(f"{x} to the power of {n} is {result}")
#
# Myclass.mymethod(2, 3)

# class inside a class

# class Person:
#     def __init__(self):
#         self.name = "HB"
#         self.db = self.Dob()
#
#     def display(self):
#         print(f"Name = {self.name}")
#
#
#     class Dob:
#         def __init__(self):
#             self.dd = 23
#             self.mm = 8
#             self.yy = 1995
#
#         def display(self):
#             print(f"date of birth is {self.dd}/{self.mm}/{self.yy}")
#
#
# p = Person()
# x = p.Dob()
# print(p.Dob().dd)
# print(Person().Dob().display())
# p.display()
# x.display()

# same type similar program

# class Person:
#     def __init__(self):
#         self.name = "HB"
#     def display(self):
#         print(f"Name= {self.name}")
#     class Dob():
#         def __init__(self):
#             self.dd = 23
#             self.mm = 8
#             self.yyyy = 1995
#         def display(self):
#             print(f"DOB is {self.dd}/{self.mm}/{self.yyyy}")
# p = Person()
# # print(Person().name)
# # print(p.name)
# # p.display()
# # print(p.Dob().mm)
# p.Dob().display()
# Person().Dob().display()
