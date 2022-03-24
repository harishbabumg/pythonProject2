import re
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
#
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
# # for item in result:
# #     print(item)
#
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











