# """ number of positional arguments"""
#
#
# def count(*args):
#     return len(args)
#
#
# print(count(1, 2, 3))
#
# print(count(1, 2, 3, 56, 455))
#
# def count(*args):
#     return int(len(args))
#
# print(count(1,213))

# def mes("hai everyone"):
#     return
# print(mes("hai everyone"))

# def prime(n=0):
#     for i in range(2, n):
#         if n % i == 0:
#             print(" not prime")
#             break
#     else:
#         print("prime")
# prime(5)

# def last_(n=0):
#     return int(str(n)[-1])
# print(last_(25))

# x = 0
#
# def perfect_square(num):
#     x = num ** 0.5
#     y = int(x)
#     if type(y) == int:
#         print("perf")
#     if type(y) == float:
#         print("imp")
#     else:
#         return "jhv"
#
# print(perfect_square(7))

# def perfect_square(num):
#     if type(int(num ** 0.5)) == int:
#         return "perfect"
#     elif type(int(num ** 0.5)) == float:
#         return "Imperfect"
#     else:
#         "Not a number"
        
# print(perfect_square(5))

#
# def perfect__square(num):
#     if len(str((num ** 0.5))) > 3:
#         return f"{num} not a perfect square"
#     else:
#         return f"{num} is a perfect square"
#
#
# print(perfect__square(144))


def perfect_square(num):
    if str(num ** 0.5)[-1] == str(0):
        return f"{num} is a perfect square"
    else:
        return f"{num} is not a perfect square"


print(perfect_square(15))
