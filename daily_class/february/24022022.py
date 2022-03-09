
"""
ENCAPSULATION
Definition - Wrapping up a data and function into a single entity
In JAVA,
public - data and functions can be accessed by any function in any class
Protected - data and function can be accessed by any class or class inherited
Private- accessed by only class and func where it is declared
high data protection
In PYTHON,
everything is Public
"""
#
#
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def demo(self):
#         self.name = "HB"
#
#
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
#
# print(p1.a)
# print(p1.b)
# # print(p1.c)  # Error
# print(p1.__dict__)
# p1.c = 10  # wrong practice
# print(p1.__dict__)
#
# print(p2.__dict__)
# print(p1.demo())
# print(p1.__dict__)
# p2.demo()
# print(p2.__dict__)


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def circumference(self):
#         return 2 * 3.14 * self.radius
#
#
# c1 = Circle(5)
# c2 = Circle(4)
# c3 = Circle(3)
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
# print(Circle.__dict__)
#
# c = Circle(2)
# print(c.circumference())
# c = Circle('2')  # in str [corrupted data]
# # print(c.circumference())  # Error
# c.radius = []  # no error even with bad data
# print(c.circumference())  # TypeError: can't multiply sequence by non-int of type 'float'

'''hence to take clean data we need'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # GETTER METHOD
    @property
    def radius(self):
        return self._radius  # private variables (shouldn't be accessed/used)

    # SETTER METHOD
    @radius.setter
    def radius(self, value):
        print(f"setting the radius to {value}")
        if value <= 0:
            raise ValueError("Radius should be a positive values")
        if not isinstance(value, (float, int)):
            raise TypeError("radius should be a number")
        self._radius = value

    @radius.deleter
    def radius(self):
        raise AttributeError("You cannot delete an attribute")

    def circumference(self):
        return 2 * 3.14 * self.radius


'''Underscore attributes represents it's internal use, getters/setters are used to validate the user input'''

c1 = Circle("")
print(c1.radius)
# print(c1.circumference())
# del c1.radius

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    @property
    def fname(self):
        print("Getting")
        return self._fname

    @fname.setter
    def fname(self, value):
        print("Setting")
        if not isinstance(value, str):
            raise TypeError()

        if len(value) > 5:
            raise ValueError("fname should be less than 5 character")
        self._fname = value

    @property
    def age (self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 10 or value > 60:
            raise ValueError()
        self._age = value


p = Person("HB", "MG", 25)
print(p.fname)
p.fname
p.lname
p.age





