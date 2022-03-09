# class Parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print(f"Executing Parent Google {self.value}")
#
#     def apple(self):
#         print("Executing Parent Apple")
#         self.google()
#
# # Child class having a separate method
#
#
# class Child1(Parent):
#     def demo(self):
#         print("executing demo")
#
# #
# # c = Child1(10)
# # c.google()
# # c.apple()
# # c.demo()
# # c.spam()
#
# # overriding/Modifying the Parent class in Child class
#
#
# class Child2(Parent):
#     def hello_word(selfself):
#         print("hello_world")
#
#     def google(self):
#         print(f"Executing Child2 Google {self.value}")
#
#
# # d = Child2(10)
# # d.hello_word()
# # d.google()
# # # d.spam
# # print(Child2.__mro__)  # method resolution order 1st in Child2 -> parent-> object checking for attribute
# # d.apple()  # print the google in child2 rather than in parent
#
#
# # Child adding extra functionality and re-using the original functionality of the parent class
#
# class Child3(Parent):
#     def google(self):
#         print("Executing Child3 Google!!!")
#         super().google()
#
#
# # e = Child3(10)
# # #
# # print(Child3.__mro__)
# # e.google()
# # e.apple()
#
#
# #  Child class having an extra attribute
#
# class Child4(Parent):
#     def __init__(self, value, name):
#         self.name = name
#         super().__init__(value)
#
#
# # f = Child4(10, "Sandeep")
# # print(f.__dict__)
# # print(f.value)
#
# #  child inheriting from multiple parents
#
#
# class Facebook:  #  stanalone class
#     def spam(self):
#         print("Executing Facebook Spam")
#
#
# class Child5(Parent, Facebook):  # two parents 'parent and facebook'
#     pass
#
# #
# # g = Child5(10)
# # g.spam()
# # g.apple()
# # g.google()
#
#
# """Multi-Level inheritance"""
#
#
# class A:
#     def demo(self):
#         print("Class A Demo")
#
#
# class B(A):
#     def demo(self):
#         print("Class B Demo")
#         super().demo()
#
#
# class C(B):
#     def demo(self):
#         print("Class C Demo")
#         super().demo()
#
#
# c = C()
# c.demo()
# print(C.__mro__)
#

#  Multiple inheritance
#
# class Parent:
#     def demo(self):
#         print("Class Parent, Demo")
#
#
# class Demo(Parent):
#     def demo(self):
#         print("Class Child1, Demo")
#         super().demo()
#
#
# class Spam(Parent):
#     def demo(self):
#         print("Class Child2, Demo")
#         super().demo()
#
#
# class Child(Spam, Demo):
#     pass
#
#
# c = Child()
# c.demo()
# print(Child.__mro__)
#
# #  super() will not call the parent immediately rather check available parent(here, it is Demo)
# # after Spam -> Demo -> Parent -> Object

#  CLASS DECORATORS


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling, {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


def logging(some_class):
    for func_name, func_address in some_class.__dict__.items():
        for key, value in some_class.__dict__.items():
            if callable(value):
                setattr(some_class, "key", log(value))  # __init__ = log(__init__) -->gives add = log(add)
            return some_class
    #
#
# @logging  # Arithmatic = logging(Arithmatic
# # class Arithmatic:
    @log
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @log
    def add(self):
        return self.a + self.b

    @log
    def sub(self):
        return self.a - self.b

    @log
    def mul(self):
        return self.a * self.b

# mul = log(mul) -> decorator


# a = Arithmatic(1, 2)
# a.add()
# a.sub()
# a.mul()
# print(a.a)
# print(a.b)
#
# aa = Arithmatic(1, 2)
# print(aa.a)
#
# print(getattr(aa, "a"))
# print(getattr(aa, "b"))
#
# aa.a = 100
# print(aa.a)
#
# setattr(aa, "a", 120)
# print(aa.a)
# # print(callable(add))
# print(callable(a))
# print(callable(len))  # it is callable
#
# print(Arithmatic.__dict__)  #  all class variable and class will be stored in class dict.

# ak = Arithmatic
# print(ak)
# print(Arithmatic)
# print(Arithmatic.__dict__)
# print(ak.__dict__)

# ab = Arithmatic(1, 8)
# print(ab)
# print(ab.add())


#   0-EXAMPLE


# def attach(cls):
#     cls.name = "HB"
#     return cls


# @attach
# class Demo:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

    # def add(self):
    #     return self.a + self.b


# dd = Demo(1, 5)
# print(dd.name)

#  1-EXAMPLE


#  Back to inheritance


class BankAccount:
    interest_rate = 0.04
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount should be greater than zero")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            raise ValueError("Insufficient Funds")

    def roi(self):
        interest_amount = self.balance * self.__class__.interest_rate
        self.balance += interest_amount


# class SBAccount(BankAccount):
#     interest_rate = 0.05
#     def withdraw(self, amount):
#         if amount > 10000:
#             raise ValueError("Cannot withdraw more than 1000")
#         super().withdraw(amount)


# s = SBAccount("HB", 20000)
# print(s)
# s.deposit(10000)
# print(s.balance)
# s.withdraw(10000)
# print(s.balance)
# s.withdraw(11000)


# class Demo:
#     a = 10  # class variable
#     def demo(self):
#         print("demo", self.__class__.a)
#
#
# class Child(Demo):
#     # def demo(self):
#     #     print("Child Demo")
#     a = 100  # redefining variable
#
# c = Child()
# c.demo()
# print(c.__class__)
# print(s.balance)

class SalaryAccount(BankAccount):
    def __init__(self, name):
        self.is_first_month_salary = True
        self.max_draft_amount = 10000
        super().__init__(name, 0.00)

    def deposit(self, amount):
        if self.is_first_month_salary:
            self.is_first_month_salary = False
            super().deposit(amount + 1000)
        else:
            super().deposit(amount)

    def overdraft(self, amount):
        if amount <= self.max_draft_amount:
            # self.balance += amount
            super().deposit(amount)  # handover the amount deposit method of parent class
            self.max_draft_amount -= amount
        else:
            raise ValueError(f"Maximum available draft amount is {self.max_draft_amount}")

# s = SalaryAccount("steve")
# print(s)
# print(s.__dict__)
#
# s.deposit(50000)
# print(s.__dict__)  # 1st month salary
#
# s.deposit(50000)
# print(s.__dict__)  # 2nd month salary


# s1 = SalaryAccount("bill")
# s2 = SalaryAccount("HB")
# print(s1.__dict__)
# print(s2.__dict__)

# s1.deposit(50000)
# s2.deposit(50000)
# print(s1.__dict__)
# print(s2.__dict__)
# s1.overdraft(8000)
# s2.overdraft(5000)
# print(s1.__dict__)
# print(s2.__dict__)

# print(s1.overdraft(3000))
# print(s1.__dict__)
# print(s2.overdraft(2000))
# print(s2.__dict__)

# class SeniorCitizenAccount(BankAccount):
#     interest_rate = 0.06
#     def withdraw(self, amount):
#         if amount > 20000:
#             raise ValueError("Cannot withdraw more than 20K ")
#         super().withdraw(amount)
#
# s11 = SeniorCitizenAccount("HB_Senior", 2500000)
# s11.withdraw(15000)
# # s11.withdraw(25000)
# print(s11.__dict__)
#
#
# class SukanyaSamruddhiAccount(BankAccount):
#     def __init__(self, name, balance):
#         if balance < 1000:
#             raise ValueError()
#         super().__init__(name, balance)
#
#     def deposit(self, amount):
#         if amount < 1000:
#             raise ValueError("Minimum amount to deposit should more than 1000")
#         super().deposit(amount)
#
#     def withdraw(self, amount):
#         raise Exception(f"Withdrawal of amount is not allowed for this (Su. Sam. Acc.) account")
#
#
# girl = SukanyaSamruddhiAccount("Div", 1000)
# # girl.deposit(900)  # Error
# girl.deposit(1000)
# print(girl.__dict__)
#
#

#  Multilevel Inheritance

# class PenaltyAccount:
#     penalty_amount = 0
#     def withdraw(self, amount):
#         self.balance -= self.__class__.penalty_amount
#         super().withdraw(amount)
#
#
# class PensionAccount(PenaltyAccount, BankAccount):
#     penalty_amount = 200
#
#
# class MaxTransactionlimit(PenaltyAccount, BankAccount):
#     penalty_amount = 1000
#
#
# e1 = MaxTransactionlimit("HB_m", 10000)
# e1.withdraw(1000)
# print(e1.balance)
#
#
# p1 = PensionAccount("HB_p", 10000)
# p1.withdraw(9000)
# print(p1.balance)



