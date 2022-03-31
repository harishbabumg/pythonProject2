
class Emp(object):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.id}, {self.name}, {self.salary}")