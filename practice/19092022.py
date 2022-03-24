from itertools import zip_longest
from collections import defaultdict

# n = 6
# for i in range(2, n):
#     if n % i == 0:
#         print('not a prime number')
#         break
#     else:
#         print("is a prime number")
#         break
#
# a = ["A", "B", "C", "D", "E"]
# b = [1, 2, 3, 4, 5]
# z = zip(a, b)
# print(z)
# print(set(z))
# print(list(z))
# print(tuple(z))
# print(dict(z))

# a = ["A", "B", "C", "D", "E"]
# b = [1, 2, 3, 4, 5, 7, 10]
# zl = zip_longest(a, b)
# print(zl)
# print(list(zl))
# print(set(zl))
# print(tuple(zl))
# print(dict(zl))

# without using inbuilt method, counting the characters of a string

# s = "hello"
# d = defaultdict(int)
# # d = {}
#
# for i in s:
#     count = 0
#     for j in s:
#         if i == j:
#             count = count + 1
#     d[i] = count
#
# print(d)

# default dict
# s = "hello world"
# dd = defaultdict(int)
# d = {}
#
# for char in s:
#     dd[char] = dd[char] + 1
# print(dd)

# for char in s:
#     count = 0
#     if char in d:
#         d[char] += count
#     else:
#         d[char] = count
#     d[char] = count
# print(d)


""" sample """
# s = "hello world welcome there"
# list_ = s.split()
# d = {}
# for ele in list_:
#     if ele[0] not in d:
#         d[ele[0]] = [ele]
#     else:
#         d[ele[0]] += [ele]
# print(d)


# def add_(a, b, /, *, c, d):
#     print(a, b , c, d)
#
#
# add_(1, 2, c=3, d=4)


# def evens(end, start=0):
#     l = []
#     for i in range(start, end+1):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
#
# print(evens(10, 1))

# def primes(end, start=2):
#     res = []
#     for n in range(start, end+1):
#         if n > 1:
#             for i in range(2, n):
#                 if n % i == 0:
#                     break
#                 else:
#                     res.append(n)
#                     break
#         else:
#             return "Number should be greater than one"
#     return res
#
#
# print(primes(1, 1))

"""for number of fibonacci"""

# def fib(n):
#     a = 0
#     b = 1
#     if n == 0:
#         print('n must be greater than 0')
#     elif n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2, n):
#             print(a + b)
#             c = a + b
#             a = b
#             b = c
#
# fib(6)

def rec(n):
    for _ in range(0, n):


print(rec(1))