
# banking.py
# class BankAccount:
#     interest_rate = 0.05  # class variable
#
#     def __init__(self, name, balance=0):
#         #  Instance variables (each customer will get a fresh copy of name, balance and transactions)
#         self.name = name
#         self.balance = balance
#         self.transactions = []
#         self.transactions.append(f"******* initial amount deposited {balance}")
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         self.transactions.append(f"Amount deposited {amount}")
#
#     def withdraw(self, amount):
#             if amount > self.balance:
#                 raise ValueError("Insufficient funds")
#             self.balance = self.balance - amount
#             self.transactions.append(f"Amount withdraw {amount}")
#             return f"please collect the cash {amount}"
#
#     def transfer(self, to_account, amount):
#         if self.balance < amount:
#             raise ValueError("Insufficient Funds")
#         to_account.deposit(amount)
#         self.balance -= amount
#
#     def statement(self):
#         for transaction in self.transactions:
#             print(transaction)
#         print("*" * 25)
#         return f"Available balance in the {self.balance}"
#
#     def roi(self):
#         interest_amount = self.balance * BankAccount.interest_rate
#         self.balance += interest_amount
#         self.transactions.append(f"*********** Interest amount credited ****** {interest_amount}")
#
#
# c1 = BankAccount("sandeep", 1000)
# c2 = BankAccount("Steve", 2000)
# c3 = BankAccount("Bill")
#
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
#
# print(c1.balance)
# print(c2.balance)
# print(c3.balance)
#
# print(c1.deposit(1000))
# print(c1.__dict__)
#
# c1.deposit(5000)
# c2.deposit(1000)
# c3.deposit(1500)
# print(c3.__dict__)
#
# print(c1.balance)
# print(c2.balance)
# print(c3.balance)
#
# c1.withdraw(5000)
# print(c1.balance)
#
# #
#
# print(c1.__dict__)
# c1.deposit(10000)
# print(c1.balance)
# print(c1.transfer(c2, 1000))
# print(c2.balance)
# print(c1.balance)
# print(c1.transfer(c3, 5000))
# print(c3.balance)
# print(c1.balance)
# print(c3.balance)
#
#
# #
#
# print(c1.statement())
# print(c1.transactions)
# # print(c2.statement())
# # print(c3.statement())
#
#
# # print(roi())
# # BankAccount.__dict__
# # c1.__class__.__dict__
#
# class demo:
#     # shared across all the instance
#     count = 0
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         demo.count = demo.count + 1
#
#
# d1 = demo(1, 2)
# print(demo.count)
#
# d2 = demo(3, 4)
# print(demo.count)
#
# print(d1.__dict__)

#  SHOPPING CART shopping.py
#
# class ShoppingCart:
#     products = {"iphone": 5, "imac": 3, "ipad": 2, "iwatch": 4}
#     prices = {"iphone": 800, "imac": 4500, "ipad": 500, "iwatch": 3000}
#     def __init__(self):
#         self.cart = []
#
#     def add_item(self, name, quantity, price):
#         if name not in self.__class__.products:
#             raise Exception(f"{repr(name)} not available")
#         elif quantity <= self.__class__.products[name]:
#             self.cart.append({"name": name, "quantity": quantity, "price": self.__class__.prices[name]})  # check this
#             self.__class__.products[name] -= quantity
#         else:
#             raise ValueError("Product out of stock")
#
#     def total_cost(self):
#         # total = sum([item['quantity'] * item['price'] for item in self.cart])
#         # return total
#         total = 0.0
#         for item in self.cart:
#             total = total + (item['quantity'] + item['price'])
#         return total
#
#     def remove_item(self, name):
#         for item in self.cart:
#             if item["name"] == name:
#                 if item["quantity"] > 1:
#                     item["quantity"] -= 1
#                 else:
#                     self.cart.remove(item)
#
#
# c1 = ShoppingCart()
# c2 = ShoppingCart()
# c3 = ShoppingCart()
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
#
# print(c1.add_item("iphone", 1, 800))
# print(c1.__dict__)
#
# print(c1.add_item("imac", 1, 4500))
# print(c1.__dict__)
#
# print(c2.add_item("iwatch", 2, 3000))
# print(c2.__dict__)
#
# c1.add_item("iphone", 2, 800)
# c1.add_item("imac", 2, 5000)
# print(c1.__dict__)
#
# print(c1.total_cost())
#
# print(c1.cart)
# c1.remove_item("iphone")
# c1.remove_item("iphone")
# c1.remove_item("iphone")
# print(c1.cart)
#
# print(ShoppingCart.products)
# c2.add_item("iphone", 2, 800)
# print(ShoppingCart.products)
# # c3.add_item("samsung", 1, 500)  # Exception samsung is not present in "Products"
# # print(c3.add_item("iphone", 1, 800))  # Product out of stock

#  INHERITANCE

class Parent:
    def __init__(self, value):
        self.value = value

    def google(self):
        print(f"Executing Parent Google {self.value}")

    def apple(self):
        print("Executing Parent Apple")
        self.google()


p = Parent(10)

# print(p.value)
# p.google()
p.apple()


class Child1:
    def __init__(self, value):
        self.value = value

    def google(self):
        print(f"Executing Parent Google {self.value}")

    def apple(self):
        print("Executing Parent Apple")
        self.google()
