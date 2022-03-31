from abc import ABC, abstractmethod
import math
from abc import *

# Program to create abstract class and sub classes which implement the abstract method of the abstract class

# class Myclass(ABC):
#     @abstractmethod
#     def calculate(self, x):
#         pass
#
#
# class Sub1(Myclass):
#     def calculate(self, x):
#         print(f"Square value = {x*x}")
#
# class Sub2(Myclass):
#     def calculate(self, x):
#         print(f"Square root is {math.sqrt(x)}")
#
# class Sub3(Myclass):
#     def calculate(self, x):
#         print(f"cube root is {x**3}")
#
# obj1 = Sub1()
# obj1.calculate(4)
#
# obj2 = Sub2()
# obj2.calculate(16)
#
# obj3 = Sub3()
# obj3.calculate(8)

"""Understanding with cars abstract class"""

# class Car(ABC):
#     def __init__(self, regno):
#         self.regno = regno
#
#
#     def openTank(self):
#         print(f"Fill the fuel in the tank, for the car with registration number: {self.regno}")
#
#     @abstractmethod
#     def steering(self):
#         pass
#
#     @abstractmethod
#     def braking(self):
#         pass
#
#     """Now creating the sub_classes to implement the abstract methods"""
#
# class Maruthi(Car):
#     def steering(self):
#         print("Maruthi uses manual steering")
#
#     def braking(self):
#         print("Maruthi uses hydraulic brakes, Apply brakes and stop the vehicle")
#
#
# m = Maruthi(1234)
# print(m.regno)
# m.openTank()
# m.steering()
# m.braking()
# print("-" * 20)
# class Santro(Car):
#     def steering(self):
#         print("Santro uses power steering to drive the car")
#     def braking(self):
#         print("Santro uses gas brakes to stop the vehicles")
#
# s = Santro(456)
# print(s.regno)
# s.openTank()
# s.steering()
# s.braking()

"""INTERFACES"""

# program to develop an interfaces

# from abc import *
#
# class Myclass(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class Oracle(Myclass):
#     def connect(self):
#         print("Connecting to oracle database...")
#     def disconnect(self):
#         print("Disconnecting from oracle database...")
#
#
# class Sybase(Myclass):
#     def connect(self):
#         print("Connecting to Sybase database...")
#     def disconnect(self):
#         print("Disconnecting from Sybase database...")

# class Database:
#     string = input('Enter database name: ')
#     class_name = globals()[string]
#     x = class_name()
#     x.connect()
#     x.disconnect()


# print(globals())

# o = Oracle()
# o.connect()
# o.disconnect()
#
# s = Sybase()
# s.connect()
# s.disconnect()


"""INTERFACE USING THE PRINTER EXAMPLE"""

# class Printer(ABC):
#     @abstractmethod
#     def printit(self, text):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class IBM(Printer):
#     def printit(self, text):
#         print(text)
#
#     def disconnect(self):
#         print("Printing completed on IBM printer")
#
# class Epson(Printer):
#     def printit(self, text):
#         print(text)
#
#     def disconnect(self):
#         print("Printing completed on Epson printer")
#
# path = r"C:\Users\haris\PycharmProjects\pythonProject2\practice\oops\Abstract_classes_and_interfaces\config"
# class usePrinter:
#     with open(path, "r") as file:
#         string = file.readline()
#         classname = globals()[string]
#         x = classname()
#
#         x.printit('Hello, this is sent to printer')
#         x.disconnect()


