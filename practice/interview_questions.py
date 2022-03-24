from itertools import chain
from itertools import islice
from collections import deque
from collections import defaultdict
import re

path = r"C:\Users\haris\PycharmProjects\pythonProject2\files_directory\txt_log_files\reading_files\sample.txt"
path_33 = r"C:\Users\haris\PycharmProjects\pythonProject2\files_directory\txt_log_files\reading_files\interview.log"
"""1. Write a program to find the length of the string without using inbuilt function (len)"""


# def _len(iterable):
#     _count = 0
#     for item in iterable:
#         _count += 1
#     return _count
#
#
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
#
#
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
# list_ = convert_to_list('steve')
# print(list_)

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

"""8. Write program to convert upper case to lower case and vice-versa without 
using inbuilt method."""


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
#
#
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
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a+b)
#
# # Using chain
# s = chain(a, b)     # Returns an iterator
# print(list(s))

"""11. Write program to read a random line in a file. (ex. 50, 65, 78th line)"""

#
# def read_random_line_1(lineno):
#     with open(path) as file:
#         line = islice(file, lineno, lineno+1)
#         return list(line)
#
#
# print(read_random_line_1(9))

# Alternate Solution


# def read_random_line_2(lineno):
#     file = open(path)
#     for index, line in enumerate(file, start=1):
#         if index == lineno:
#             return line
#
#
# print(read_random_line_2(10))

"""12. Write program to read a random lines in a file. 
(ex. I want read all lines 10th to 15th line)"""


# def read_n_lines(start_line, end_line):
#     with open(path) as file:
#         s = islice(file, start_line, end_line)
#         for line in s:
#             print(line)


# read_n_lines(0, 3)


# def read_n_lines_1(start_line, end_line):
#     with open(path) as file:
#         for lineno, line in enumerate(file):
#             if start_line <= lineno <= end_line:
#                 print(line)
# #
#
# read_n_lines_1(0, 3)

# if read_n_lines_1(0, 3) == read_n_lines(1, 3):
#     print(True) # doubt

"""13 Program to print last "N" lines of a file."""


# def last_n_lines(n):
#     line_count = 0
#     with open(path) as file:
#         for line in file:
#             line_count += 1
#             file.seek(0)
#             lines = islice(file, line_count - n, None)
#             return list(lines)
# last_n_lines(5)


# from collections import deque
# recommended

# def tt(liail(n):
# #     with open(path) as file:
# #         d = deque(file, n)             # only last 'n' lines will be loaded to the deque
# #         return d
# #
# #
# # last_10_lines = tail(10)     # returns last 10 lines of the file
# # for line in last_10_lines:
# #     prinne)

"""14. Write a program to check if the given 
string is Palindrome or not without using reversed method."""


# def is_palindrome(iterable):
#     rev_iter = iterable[::-1]
#     if iterable == rev_iter:
#         return True
#     else:
#         return False
#
# #
# print(is_palindrome('racecar'))
# print(is_palindrome('malayalam'))
# print(is_palindrome('hello'))

"""15 Write a program to search for a character in a 
given string and return the corresponding index."""


# def search_character(string, key):
#     for index, char, in enumerate(string):
#         if char == key:
#             print(f'Character {char} is at index {index}')
#

# search_character('hello world', 'l')
# search_character('hello world', 'd')

"""16 Write a program to get the below output"""

# sentence = "hello world welcome to python programming hi there"
"""d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']"""

# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#     d[word[0]].append(word)
#     # d[word[0]] += [word]
# print(d)

"""17 Write a to replace all the characters with - 
if the character occurs more than once in a string
my_string = 'hellohai' # O/P should be '-e--o-ai'"""

my_string = 'hellohai'
#
# new_string = ''.join(['-' if my_string.count(c) > 1 else c for c in my_string])
# print(new_string)

# def coun(any_string):
#     for char in any_string:
#         if any_string.count(char) > 1:
#             print("-", end="")
#         else:
#             print(char, end="")

# def coa(any_string):
#     res = ["-" if any_string.count(char) > 1 else char for char in any_string]
#     print("".join(res))

# coa(my_string)
# coun(my_string)

"""18 write a decorator that returns only positive values of subtraction"""


# def positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper

# @positive
# @positive
# def sub(a, b):
#     return a - b


# print(sub(-50, -150))

"""19 How to get the count of number of instances of a class 
that is being created."""

# class Login:
#    login_count = 0    # Class Variable that keeps count of login counts
#    def __init__(self):
#        Login.login_count += 1
#
# a1 = Login()
# print(Login.login_count)
# b1 = Login()
# print(Login.login_count)
# c1 = Login()
# print(Login.login_count)

"""20 Write a function which takes a list of strings and integers.
If the item is a string it should print as is and if 
the item is integer of float it should reverse it."""

# def spam(items):
#     for item in items:
#         if isinstance(item, str):   # Check if the item is an instance of String
#             print(item)
#         else:
#             temp = str(item)    # Typecast Integer to String
#             print(temp[::-1])   # Reverse the String"""

# spam(['apple', 'yahoo', '1234', 100, 123.76, '26.23'])

"""21 Write a class named Simple and it should have iteration capability."""

# class Simple:
#     def __init__(self, items):
#         self._items = items
#
#     def __iter__(self):
#         return iter(self._items)

# d = Simple([1,2,3])
# print(type(d))

# for item in d:
#     print(item, end='')

"""22 Write a Custom class which can access the values of 
dictionaries using d['a'] and d.a"""


# class MyDict:
#     def __init__(self, d):
#         self._dict = d
#
#     def __getitem__(self, item):
#         return self._dict[item]
#
#     def __getattr__(self, name):
#         return self._dict[name]

    # __getattr__ method is called only
    # for missing attributes.(i.e. if you try to
    # access an attribute which is not in instance dict)


# d = MyDict({'a': 1, 'b': 2})
# print(d.a)
# print(d.b)
# print(d['a'])
# print(d['b'])

"""23 Write a python program to get the below output"""
# sentence = "Hi How are you"
"""o/p should be "iH woH era uoy"""

# words = sentence.split()
# reversed_words = [word[::-1] for word in words]
# print(reversed_words)

"""24 Write a python program to get the below output"""
#
# sentence = "Hi How are you"
# """o/p should be "ouy era woH iH"""
# reversed_words = [word[::-1 ]for word in reversed(sentence.split())]
# print(" ".join(reversed_words))

"""25 Write a lambda function to add two numbers (a, b)"""

# add = lambda a, b: a + b
# print(add(1, 2))
# print(add("a", "c"))

"""26 What is the output of the following"""

# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])
# print((a, b))

"""27 How to remove duplicates from the list without using inbuilt functions"""

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# res = []
# for item in items:
#     if item not in res:
#         res.append(item)
#     else:
#         pass
# print(res)

# method HB
# res_ = set(items)
# print(list(res_))

"""28 Find the longest word in the sentence"""

# method HB
# sentence = "Hello world. Welcome HBSHHJABGHZABGXHAXX to Python"
# res = sentence.split()
# for item in res:
#     res.sort(key=len)
# print(res[-1])

#  text
# sentence = "Hello world. Welcome to Python"
# words = sentence.split()
# d = {word: len(word) for word in words}
# print(max(d.items(), key= lambda item: item[-1]))

# or

# sentence = "hello world welcome to programming"
# words = sentence.split()
# max_len = 0
# max_word = ''
#
# for word in words:
#     if len(word) > max_len:
#         max_len = len(word)
#         max_word = word
# print(max_len, max_word)
# or

# sentence = "hello world welcome to programming"
# print(max(sentence.split(), key=len))

"""29 write a program to reverse the values in 
the dictionary if the value is of type String"""

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# dd = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         dd[key] = value[::-1]
#     else:
#         dd[key] = value
# print(dd)
#
#
# rev = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(rev)

"""30 write a program to get 1234"""

# t = ('1', '2', '3', '4')
# tt = "".join(t)
# print(tt)

"""31 How to get the elements that are in list b but not in list a"""

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
#
# for item in b:
#     if item not in a:
#         print(item)

# or

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# set_a = set(a)      # Convert the list to set
# set_b = set(b)
# print(set_b.difference(set_a))

"""32 A function takes variable number of positional arguments as input. 
How to check if the arguments that are passed are more than 5"""

# def vari(*args):
#     if len(args) > 5:
#         print("Number of args given are morethan 5")
#
# vari("as", "12", 10.1, "as", "HB", "True")

"""33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file."""
# Not working
# def text(word):
#     with open(path_33) as file:
#         for line in file:
#             res = line.split()
#             for item in res:
#                 words = []
#                 if item == word:
#                     words.append(item)
#         print(len(words))
#
# text("ERROR")

"""34 Write a function to reverse any iterable 
without using reverse function."""

# a = [1, 2, 3, 4, 5]
# _reversed = []
# for i in range(len(a)-1, -1,-1):
#     _reversed.append(a[i])

"""35 Write a function to print the below output."""

# """func("TRACXN", 0)  # Should print RCN"""
# """func("TRACXN", 1)  # Should print TAX"""

# def func(string, n):
#     if n == 0:
#         print(string[1::2])
#     if n == 1:
#         print(string[::2])
#
# func("TRACXN", 0)
# func("TRACXN", 1)

"""36 Sum all the numbers in the below string."""
# s = "Sony12India567Pvt2ltd"

# total = 0.00
# r = re.findall(r'[\d]',s)
# print(r)
#
# for char in r:
#     total += int(char)
# print(total)

# OR
# method HB
# res = []
# for char in s:
#     try:
#         if type(int(char)) == int:
#             res.append(int(char))
#     except ValueError:
#         pass
# print(sum(res))

"""37 Write a program to sum all the numbers in below string."""

# import re
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
#
# rr = re.findall(r'[\d]+', s)
# print(rr)
# total = 0
# for item in rr:
#     total += int(item)
# print(total)

"""38 Print all the numbers in the below list"""
# a = ['abc', '123', 'hello', '23', "3"]

# for item in a:
#     if item.isnumeric():
#         print(item)

# or

# method HB
# Doubt

# for char in a:
#     res = []
#     try:
#         # res = []
#         if type(int(char)) == int:
#             res.append(int(char))
#     except ValueError:
#             pass
#
# print(res)
"""39 Program to print the number of occurrences of 
characters in a String without using inbuilt functions."""
# s = 'helloworld'
# d = defaultdict(int)
# for char in s:
#     d[char] += 1
# print(d)

"""40 Program to print only the repeated characters and count of the same."""
# s = 'helloworld'
# d = defaultdict(int)
# for char in s:
#     if s.count(char) > 1:
#         d[char] += 1
# print(d)

"""41 Write a program to get alternate characters of a string in list format."""
# s = 'hello world welcome to python'

# method HB
# def alt_str(string):
#     res = []
#     res.append(string[::2])
#     print(res)

# alt_str(s)

# or

# res = [char for char in s[::2]]
# print(res)

"""42 Write a program to get square of list of number's using lambda function ."""
# a = [1, 2, 3, 4, 5]
# res = lambda item: (item ** 2)
# b = [res(ele) for ele in a]
# print(b)

"""43 Write a function that accepts two strings and 
returns True if the two strings are anagrams of each other."""

# def ana(string1, string2):
#     if sorted(string1.lower()) == sorted(string2.lower()):
#         print("both strings are Anagrams")
#     print("Both are not Anagrams")
# ana("eat", "at7")

"""44 Write a program to iterate through list 
and build a new list, only if the items of the list has even number of characters."""
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

# new_list = []
# for element in names:
#     if len(element) % 2 == 0:
#         new_list.append(element)
# print(new_list)
# # or
# new_list = [element for element in names if len(element) % 2 == 0]
# print(new_list)

"""45 Write a program to iterate through list and build a new dictionary, 
only if the items of the list has even number of characters."""
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

# new_dict = {ele: len(ele) for ele in names if len(ele) % 2 == 0}
# print(new_dict)

""" 46 Write a program which squares the numbers in a list using map object"""

# Squares of numbers using map
# map is used to map a function with a iterable
# a = [1, 2, 3, 4, 5]

# def squares(item):
#     return item ** 2

# Returns a map object, which happens to be an iterator.
# m = map(squares, a)
# print(list(m))

# To get the squares of numbers, feed the map object to for loop
# for item in m:
#     print(item, end=" ")
# print()
# Mapping lambda function to map object
# m = map((lambda item: item ** 2), a)
# print(list(m))

"""47 Count number of lines in a file without loading the file to the memory"""
# Counting number of lines in a file without loading the file to the memory
# with open(path) as f:
#     _count = 0
#     # Iterate over a file object and increment the _count
#     for line in f:
#         _count +=1
# print(f'No of Lines: {_count}')

"""48 Printing line and line no's"""
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line)

"""49 Write a Program to print 
the sum of entire list and sum of only internal list"""
# l = [[1,2,3],[4,5,6],[7,8,9]]
# nested_sum = []
# for element in l:
#     nested_sum.append(sum(element))
# print(nested_sum)
# total_sum = sum(nested_sum)
# print([total_sum])

# sum_internal = [sum(item) for item in l]
# Add the contents of entire list. (45)
# sum_iternal = [sum(item) for item in l]
# sum_whole_list = sum(sum_internal)
# print(sum_whole_list)
# print(sum_iternal)

# Using List Comprehension
# items = [[1,2,3],[4,5,6],[7,8,9]]
# total = sum([each_item for each_internal_list in items for each_item in each_internal_list])
# print(total)

"""50 Write a program to reverse the list as below"""
# words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']

# new = [item[::-1] for item in words[::-1]]
# print(list(new))

"""51 Write a program to update the tuple"""
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# # o/p (1, 2, 3, 4, 100, 200, 300)
# # t = t1 + t2
# t = (*t1, *t2)
# print(t)

"""52 Write a program to replace value present in nested dictionary."""
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# # Replace "nose" with "net"
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = "net"
# print(d)

"""
notes
for key, value in d.items():
    if isinstance(value, dict):
        d[key]['n'] = "net"
        d[key]["o"] = "owl"
        d[key]["1"] = {"000": "a", "00": "v"}
        d[key]["1"]["000"] = "changes"

print(d)
"""

"""53 Write a program to count the number of white spaces in a file."""
# white_spaces = 0
# with open(path) as file:
#     for line in file:
#         match = re.findall(r'\s', line)
#         if bool(match) == True:
#             white_spaces += len(match)
# print(white_spaces)
"""54 Grouping anagrams."""

# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# d = defaultdict(list)
# for word in words:
#     s = ''.join(sorted(word))
#     d[s].append(word)
# print(d)

# or
# doubt

# method HB
# new_list = []
# new_str = ""
# dd = defaultdict(list)
# for item in words:
#     a = sorted(item)
#     b = "".join(a)
#     new_list.append(b)
# for element in new_list:
#     if new_list.count(element) > 1:
#         dd[element].append(new_list)
# print(dd)

"""55 What is the difference between defaultdict and normal dictionary."""

"""
Defaultdict
-----------
1. When each key is encountered for the first time, 
it will not be there in the mapping.
2. So an entry is automatically created with 
default value (an empty list in case of defaultdict of list 
and zero in case of defaultdict int).
3. When keys are encountered again, 
the look-up proceeds normally as like a normal dictionary.
4. So, in defaultdict, creation of key, 
initialisation will happen simultaneously. 

Normal Dictionary
------------------
1. In case of normal dictionary, 
if the key does not exist, "KeyError" is raised. 
2. In order to work on the value, 
first the key needs to be created and initialised.
"""

"""56 Explain property decorator in python."""
