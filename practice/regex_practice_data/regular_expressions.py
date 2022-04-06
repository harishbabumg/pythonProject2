import re
import time
import urllib
from urllib import request
path1 = r'C:\Users\haris\PycharmProjects\pythonProject2\practice\regex_practice_data\salaries_regex'
path2 = r'C:\Users\haris\PycharmProjects\pythonProject2\practice\regex_practice_data\newfile_regex'


# COMPILE, SEARCH, MATCH, FINDALL

# prog = re.compile( r'm\w\w')
# string = 'cat mat bat rat'
# result = prog.search(string)
# print(result.group())
#
# result = re.search(r'm\w\w', string)
# print(result)
# print(result.group())

# string1 = "operating system format"
# result = re.search(r'm\w\w', string1)
# print(result.group())

# string2 = 'man sum mop run'
# # #
# result = re.search(r'm\w\w', string2)
# print(result.group())  # searches only first element
#
# result_ = re.match(r'm\w\w', string2)
# print(result_.group())  # matches if string is in first occurrences only
#
# result1 = re.findall(r'm\w\w', string2)
# print(result1)  # findsall the strings

# SPLIT()
# string = 'This; is the: "python\'s world'
# result = re.split(r'\W+', string)
# print(result)  # split where there is no alphanumeric character

# SUBSTITUTE
# string = 'Kumbhamela will be conducted at Ahmedabad in India'
# res = re.sub(r'Ahmedabad', 'Allahabad', string)
# print(res)  # replaces 'Ahmedabad' with 'Allahabad'

# for retrieving all the words with 0 or more repetitions

# string = "An apple a day keeps the doctor away"
# result = re.findall(r'a[\w]*', string)
# print(result)  # even 'ay' in 'day' is printing which not required
# for item in result:
#     print(item)

# result = re.findall(r'\ba[\w]*\b', string)
# print(result)  # words starting with 'a' and having space before and after are printed

#  retrieve all the words with a numeric digit
# numeric digit represented by r'd[\w]*'

# string = 'The meeting will be conducted on 1st and 21st 2 of every month'
# result = re.findall(r'\d[\w]*', string)
# print(result)  # \d = starting with numeric digit, [\w]* meaning 0 or more words

# retrieving the words of specific length
# string = 'one two three four five six seven 8 9 10 eleven hj'
# result = re.findall(r'\b\w{5}\b', string)
# print(result)  # only 5 five character possessed strings are printed
r"""\b before and after to get words surrounded by spaces
\w{5} represent a word containing any alphanumeric characters repeated for 5 times
character in curly braces e.g. {m} represents repetition for 'm' times"""

# same program using search()
# string = 'one two three four five six seven 8 9 10 eleven hj'
# result = re.search(r'\b\w{5}\b', string)
# print(result)  # gives the Match object
# print(result.group())  # gives first word with five characters

# retrieving words with at least specified no of characters
# string = 'one two three four five six seven 8 9 10 eleven '
# result = re.findall(r'\b\w{4,}\b', string)
# print(result)

#  retrieving words with range of specified no of characters
# string = "one two three four five six seven 8 9 10 eleven "
# result = re.findall(r'\b\w{3,5}\b', string)
# print(result)

#  retrieving numeric digits
# string = "one two three four five six seven 8 9 10 eleven "
# result = re.findall(r'\b\d\b', string)
# print(result)  # \d is for only single digits

# string = "one two three four five six seven 8 9 10 eleven"
# result = re.findall(r'\b\d\d\b', string)
# print(result)  # \d\d gives double digits

#  retrieve the last word of string
# string = "one two three four five six seven 8 9 10 eleven"
# result = re.findall(r'e[\w]*\Z', string)
# print(result)

"""e -> represents the word should start from 'e'
[\w]* -> any characters after 'e'
\Z -> searching will be done from ending of the starting
"""

"""Quantifiers"""
# string = 'Harish Babu M G 7353946422'
# res = re.findall(r'\d+', string)
# print(res)

# for the same string non-numeric charaters can be extracted
# string = 'Harish Babu M G 7353946422'
# res = re.findall(r'\D', string)
# print(res)  # gives in list
# print("".join(res))  # by joining we get meaningful string

# OR

# string = 'Harish Babu M G 7353946422'
# res = re.search(r'\D+', string)
# print(res.group())

# extracting words by 'any two' characters

# string = 'anil anant arati akash akar arundhathi ankur abhijit ananya'
# result = re.findall(r'a[nk][\w]*', string)
# print(result)

# to extract the range of numbers in a string
# string = 'Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000'
# result = re.findall(r'\d{2}-\d{2}-\d{4}', string)
# print(result)  # 1-5-2001 was not extracted

# string = 'Vijay 20 1-5-2001, Rohit 25 22-10-1990, Sita 22 15-09-2000'
# result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', string)
# print(result)

# to check if the string is starting with a specified words
# string = "Hai Bengaluru"

# result = re.findall(r'^H', string)
# if result:
#     print("String is starting with H")
# else:
#     print(f"String is not starting with H")

# to check if the string is ending with a specified words
# string = "Namaskara Bengaluru, Fire brand"
# wr = "and"
# result = re.findall(r'Brand$', string, re.IGNORECASE)
# print(result)  # re.IGNORECASE -> ignores the case of an alphabet
# if result:
#     print(f"the string is ending with {repr(wr)}")
# else:
#     print(f"the string is not ending with {repr(wr)}")

"""
[ABC] -> represents anyone character A or B or C
[A-Z] -> represents in range of A to Z
"""

#  to retrieve only marks from the string
# string = "Rahul got 75 marks, Vikas got 55 marks, whereas Subbu got 98 marks."
# marks = re.findall(r'\d{2}', string)
# print(marks)
# extracting the names starting with capital letters only
# names = re.findall(r'[A-Z][a-z]*', string)
# print(names)

""" | means or, ex. am or pm"""
# string = "The meeting may be at 8am or 9am or 4pm or 5pm"
# res = re.findall(r'\dam|\dpm', string)
# print(res)

# regex on files
# extracting only mail-ids

# f = open('regex_practice_data/regex_practice', 'r')
# for line in f:
#     res = re.findall(r'\S+@\S+', line)
#     if len(res) > 0:
#         print(res)
# path1 = r'C:\Users\haris\PycharmProjects\pythonProject2\practice\regex_practice_data\salaries_regex'
# path2 = r'C:\Users\haris\PycharmProjects\pythonProject2\practice\regex_practice_data\newfile_regex'
# # reading and writing the file
# f1 = open(path1, 'r')
# f2 = open(path2, 'w')
# reading nd extracting from one file and
# writing the extracted ones to other files

# for line in f1:
#     res1 = re.search(r'\d{4}', line)
#     res2 = re.search(r'\d{4,}.\d{2}', line)
    # print(res1.group(), res2.group())
    # f2.write(res1.group() + "\t")
    # f2.write(res2.group() + "\n")


# reading the HTML file
# path_html = r'file:///C:\Users\haris\OneDrive\Desktop\python_class\html-20220308T105145Z-001\regex_practice.html'
# f = urllib.request.urlopen(path_html)
# text = f.read()
# string = text.decode()
# result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>', string)
# result1 = re.findall(r'<td>\w+</td>\s<td>(\w+)', string)
# result2 = re.findall(r'\s<td>(\d\d.\d\d)</td>', string)

# fin_res = list(zip(result1, result2))
# for item in fin_res:
#     print(item)


