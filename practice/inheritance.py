
# class One:
#     a = 10
#
#     def __init__(self, b):
#         self.b = b
#
#     def fun(self):
#         print("fun is here")
#
#
# class Two(One):
#     c = 20
#
#     def __init__(self, b, d):
#         super().__init__(b)
#         self.d = d
#
#     def fun2(self):
#         print("fun2 in here")
#
#
# s = One(5)
# t = Two(2, 3)
#
# print(s.b)
# print(t.d)
#
# #


class School:
    clgid = "001"

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(School):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno


class Employee(School):
    def __init__(self, name, age, empid):
        super().__init__(name, age)
        self.empid = empid


std = Student("HB", 26, 404)
emp = Employee("Ashok", 40, 10)
# print(std.clgid)
# print(std.rollno)
# print(emp.empid)

# print(std.__dict__)
# print(emp.__dict__)
