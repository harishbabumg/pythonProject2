from time import  sleep
# def attach(func):
#     func.count = 0
#     return func
#
# @attach
# def add(a, b):
#     add.count += 1
#     return a+b
#
# print(add(1,2))
# print(add(1,2))
# # print(add(1,2))
# # print(add(1,2))
# # print(add(1,2))
# print(add.count)
#

#
# # closure variables
# def add(a, b):
#     name = "HB"
# #
#     def wrapper():
#         print(name)
#         return a+b
#     return wrapper
# #
# a = add(1,2)
# # print(a())

# # to know what is variable
# print(a.__closure__[0].cell_contents)
# print(a.__closure__[1].cell_contents)
# print(a.__closure__[2].cell_contents)

#
# def delay(seconds, func):
# #     """This function executes a callback function after a delay of 'seconds' e,g delay(10, add)
# #     >> add(1,2)
# #     >> 3
# #     the add function will be executed only after a delay of 10 seconds"""
#     sleep(seconds)
#     return func()
#
# #
# delay(3, add(1, 2))
#
# a = add(1, 2)
# print(a)



#
#
#
#
#
# """NEW TOPIC OOPS"""
#
#
class Employee:

    def __init__(self, fname, lname, salary):  #  constructor - this saves data hence init is used  this is instance class
        self.f_name = fname
        self.l_name = lname  # fname,lname,pay are called local variable
        self.salary = salary  # here self.pay is called instance variable

    def pay_hike(self, percent_hike):
        hike_amount = self.salary * percent_hike
        self.salary = self.salary + hike_amount
        return self.salary

    def email(self):  # this is instance method
        return f"{self.f_name}.{self.l_name}@company.com"


emp = Employee("steve", "jobs", 1000)
emp1 = Employee("Bill", "Gates", 2000)

print(type(emp))

print(emp.f_name)

print(emp1.l_name)

print(emp)

print(dir(emp))
print(dir(emp1))

print(emp.__dict__)  # this is called instance dictionary
print(emp1.__dict__)  # due to init this dictionary has been created

print(emp.__dict__["f_name"])
print(emp1.__dict__["f_name"])

# # for changing the name
# emp.__dict__["f_name"] = "STEVE"
# print(emp.__dict__["f_name"])
#
# print(Employee.email(emp))
# print(Employee.email(emp1))
#
# print(emp.email())  # this gives same output as print(Employee.email(emp))
# print(emp1.email())
#
# print(emp.pay_hike(0.1))
# print(emp1.pay_hike(0.2))
# print(emp1.__dict__)
# print(emp1.salary)


#      NEW CLAS
# class Calculator:
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
#     def sub(self):
#         return self.a - self.b
#
# print(dir(Calculator))
#
# c1 = Calculator(10, 20)
# c1 = Calculator(a=10, b=20)
# c2 = Calculator(20, 40)
# c3 = Calculator(100, 200)
# c4 = Calculator()
#
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
# print(c1.add())
# print(c2.sub())
# print(c3.mul())
# print(c4.mul())

#  Class Point
#
# class Point:
#     def __init__(self, a, b):
#         self.a = a  # self.a and self.b are instance variables
#         self.b = b
#
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy
#
#     def spam(self, a, b):
#         return a+b  # a and b are local variables
#
# p1 = Point(1,2)
# p2 = Point(10,20)
#
# print(p1.move(1, 2))

# print(p1.a)
# print(p1.b)
# print(p1.__dict__)
# print(p2.__dict__)
#
# class Player:
#     def __slots__(self, x, y):
#         self.x = x
#         self.y = y
#         self.health = 100
#
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def attack(self, pts):
#         self.health -= pts
#
# p1 = Player(1, 2)
# p2 = Player(3, 4)
# p3 = Player(5, 6)



#




# class Employee:
#     def __init__(self, fname, lname, pay, *args, **kwargs):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#         self.args = args
#         self.kwargs = kwargs

# e1 = Employee("steve", "Jobs", 1000, 'python', 26, '2200 valley view line')
#
# print(e1.__dict__)
