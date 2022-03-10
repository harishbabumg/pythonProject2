from itertools import chain
from itertools import islice
from collections import deque
from collections import defaultdict

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


# def read_random_line_1(lineno):
#     with open(path) as file:
#         line = islice(file, lineno, lineno+1)
#         return list(line)


# print(read_random_line_1(9))

# Alternate Solution


# def read_random_line_2(lineno):
#     file = open(path)
#     for index, line in enumerate(file, start=1):
#         if index == lineno:
#             return line


# print(read_random_line_2(10))

"""12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)"""


# def read_n_lines(start_line, end_line):
#     with open(path) as file:
#         s = islice(file, start_line, end_line)
#         for line in s:
#             print(line)


# read_n_lines(1, 3)


# def read_n_lines_1(start_line, end_line):
#     with open(path) as file:
#         for lineno, line in enumerate(file):
#             if start_line <= lineno <= end_line:
#                 print(line)


# read_n_lines_1(0, 3)

# if read_n_lines_1(0, 3) == read_n_lines(1, 3):
#     print(True)

"""13 Program to print last "N" lines of a file."""


# def last_n_lines(n):
#     line_count = 0
#     with open(path) as file:
#         for line in file:
#             line_count += 1
#             file.seek(0)
#             lines = islice(file, line_count-n, None)
#             return list(lines)


# from collections import deque


# def tail(n):
#     with open(path) as file:
#         d = deque(file, n)             # only last 'n' lines will be loaded to the deque
#         return d


# last_10_lines = tail(10)     # returns last 10 lines of the file
# for line in last_10_lines:
#     print(line)

"""14. Write a program to check if the given string is Palindrome or not without using reversed method."""


# def is_palindrome(iterable):
#     rev_iter = iterable[::-1]
#     if iterable == rev_iter:
#         return True
#     else:
#         return False
#
#
# print(is_palindrome('racecar'))
# print(is_palindrome('malayalam'))
# print(is_palindrome('hello'))

"""15 Write a program to search for a character in a given string and return the corresponding index."""


# def search_character(string, key):
#     for index, char, in enumerate(string):
#         if char == key:
#             print(f'Character {char} is at index {index}')
#
#
# search_character('hello world', 'w')
# search_character('hello world', 'd')

"""16 Write a program to get the below output"""

# sentence = "hello world welcome to python programming hi there"
"""d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']"""

# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#     d[word[0]].append(word)
# print(d)
