from itertools import chain
from itertools import islice
path = r"C:\Users\haris\PycharmProjects\pythonProject2\files_directory\txt_log_files\reading_files\sample.txt"
"""1. Write a program to find the length of the string without using inbuilt function (len)"""


# def _len(iterable):
#     _count = 0
#     for item in iterable:
#         _count += 1
    # return _count


# print(_len('Hello'))
# print(_len([1, 2, 3, 4]))
# print(_len({1, 2, 3}))
# print(_len((1, 2, 3, 4)))


"""2. Write a program to reverse a string without using any inbuilt functions."""


# def reverse(any_string):
#     temp = []
#     for i in range(len(any_string)-1, -1, -1):
#         temp.append(any_string[i])
#     return ''.join(temp)


# print(reverse('Hello world'))
# print(reverse('Python'))


"""3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe"."""
# s = 'Hello world'
# t = s.replace('world', 'universe')
# print(t)


"""4. How to convert a string to a list and vice-versa."""


# def convert_to_string(any_list):
#     return ''.join(any_list)
#
#
# string = convert_to_string(['steve', 'jobs'])
# print(string)
#
#
# def convert_to_list(any_string):
#     return any_string.split()
#
#
# string_ = convert_to_list('steve')
# print(string_)

"""5. Covert the string "Hello welcome to Python" to a comma separated string."""

# s = "Hello welcome to Python"
# temp = s.split()
# print(temp)
# t = ','.join(temp)
# print(t)

# s = "Hello welcome to Python"
# words = s.split()
# print(*words, sep=',')


"""6. Write a program to print alternate characters in a string."""

# s = 'hello world'
# print(s[::2])  # Using Slicing Syntax

"""7. Write a Program to print ascii values of the characters present in a string."""
# s = 'ಅಆಇಈಉಊ'
# for c in s:
#     print(ord(c))

"""8. Write program to convert upper case to lower case and vice-versa without using inbuilt method."""


# def convert(any_string):
#     l = []
#     for c in any_string:
#         temp = ord(c)   # Get the ASCII value of the character
#         if int(temp) >= 97 and temp <= 122:
#             l.append(chr(temp - 32))
#
#         elif int(temp) >= 65 and temp <= 90:
#             l.append(chr(temp+32))
#     return ''.join(l)


# d = convert('Hello WorlD')
# print(d)

# Method HB

# string_ = "Hello WorlD"
# res = []
# for char in string_:
#     if 65 <= ord(char) <= 90:
#         res.append(chr((ord(char)) + 32))
#     elif 91 <= ord(char) <= 117:
#         res.append(chr((ord(char)) - 32))
#     else:
#         res.append(char)
# res_new = "".join(res)
#
# print(res_new)

"""9. Write program to swap two numbers without using 3rd variable."""

# a = 10
# b = 20
# b, a = a, b
# print(a)
# print(b)

"""10. Write program to merge two different lists."""

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a+b)

# Using chain
# s = chain(a, b)     # Returns an iterator
# print(list(s))

"""11. Write program to read a random line in a file. (ex. 50, 65, 78th line)"""


# def read_random_line(lineno):
#     with open(path) as f:
#         line = islice(f, lineno, lineno+1)
#         return list(line)
#
#
# print(read_random_line(9))

# Alternate Solution


# def read_random_line(lineno):
#     f = open(path)
#     for index, line in enumerate(f, start=1):
#         if index == lineno:
#             return line
#
#
# print(read_random_line(10))

"""12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)"""


# def read_n_lines(start_line, end_line):
#     with open(path) as f:
#         s = islice(f, start_line, end_line)
#         for line in s:
#             print(line)
#
#
# read_n_lines(1, 15)

# Alternate Solution

# def read_n_lines(start_line, end_line):
#     with open('Data/access-log.txt') as enumerate(f, start=1):
#         if index in range(start_line, end_line):
#            print(line)

# read_n_lines(10, 15)
