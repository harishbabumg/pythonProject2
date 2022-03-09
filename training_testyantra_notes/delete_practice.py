# a = 0
# b = 1
# c = a + b
# d = b + c
#
# a = ((a+5**0.5)/2)**n
# b = ((a-5**0.5)/2)**n
# c = 5**0.5

# fibo = (a-b)/c
# def fibo_manual(n):
#     # Binet's formula
#     a = ((1 + 5 ** 0.5) / 2) ** n
#     b = ((1 - 5 ** 0.5) / 2) ** n
#     c = 5 ** 0.5
#     return (a - b) / c
# print(int(fibo_manual(1)))
# print(int(fibo_manual(2)))
# print(int(fibo_manual(3)))
# print(int(fibo_manual(4)))
# print(int(fibo_manual(5)))
# print(int(fibo_manual(6)))
# print(int(fibo_manual(7)))
# print(int(fibo_manual(8)))
# print(int(fibo_manual(9)))
# print(int(fibo_manual(10)))


# def fibo_manual(z):
    # while fibo_manual(n) > 2:


# with open(path) as file:
#     for line in file:
#         print(line)
# count = 0
# with open(path) as file:
#     for line in file:
#         count += 1

# reverse a string using recursive function

# def reverse_str(str1):
#     if str1 == "":
#         return ""
#     else:
#         return reverse_str(str1[1:]) + str1[0]
#
# print(reverse_str("Harish"))
##############
# def har_(start, end):
#     if start > end:
#         return
#     print(start, end=" ")
#     har_(start+1, end)
#
# har_(1, 25)
#  #######1 to 25
# def har_(a, b):
#     if a > b:
#         return
#     print(a)
#     har_(a + 1, b)
#
# har_(1, 25)

# 25 to 1

def cun_(a, b):
    if a < b:
        return
    print(a, end=" ")
    cun_(a - 1, b)


cun_(25, 1)

print()

# write a recursive function count_(1, 25)


def count_(start, end):
    if start > end:
        return
    print(start, end=" ")
    count_(start + 1, end)


count_(1, 25)
