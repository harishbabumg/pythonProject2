#  ###LOOPPING THROUGH DICTIONARY#############
### write a program to print the keys in a dictionary"""

"""d = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e": 5}

# using dictionary[key]
for key in d:
    print(key, end=" ")  # a b c d e
print()
# d,keys()
for key in d.keys():
    print(key, end=" ") # a b c d e
print()
# d.items()
for key, value in d.items():
    print(key, end=" ") # a b c d e
print()"""
### write a program to print only a values from the dictionary"""

# using dictionary[key]

"""d = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e": 5}
for key in d:
    print(d[key], end=" ")  # prints 1 2 3 4 5
print()
# using get() method
for key in d:
    print(d.get(key), end=" ") # prints 1 2 3 4 5
print()
# d.values()
for value in d.values():
    print(value, end=" ") # prints 1 2 3 4 5
print()
# d.items()
for key, value in d.items():
    print(value, end=" ")  # suggested to use this method"""
#print()
# write a program to print the items in a dictionary along with their indices
"""d = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e": 5}

# applying enumerate on dictionary variable

for item in enumerate(d):
     print(item, end=" ")
print()

# enumerate(d.items()):
for index,(key, value) in enumerate (d.items()):
    print(index, key, value, end=" ", sep=" - ") """
#print()

# write a program to create a dictionary of character and it's count

"""string = "Hello world"

# using count method

d = {}
for char in set(string):
    d[char] = string.count(char)
print(d)"""

# without inbuilt method
"""s = "Hello"
d = {}

for i in set(s):
    count = 0
    for j in s:
        if i == j:
            count += 1
    d[i] = count
print(d)"""
# #########################
"""s = "Hello"
d = {}
for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
print(d)"""

#  write a program to create a dictionary with word and it's count pair

# using inbuilt method
sentence = "python is a language, python programming is easy"
d = {}
# using count()
list_ = sentence.split(" ")
for word in list_:
    d[word] = list_.count(word)
print(d)
#print()

# without using inbuilt method
"""sentence = "python is a language, python programming is easy"
list_ = sentence.split()
d = {}
for word in list_:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)"""
#print()

# using defaultdict()

"""from collections import defaultdict

sentence = "python is a language, python programming is easy"
dd = defaultdict(int)
list_ = sentence.split()

for word in list_:
    dd[word] += 1
print(dd)
print()"""
# write a program to create a dictionary with word and it's length pair
"""sentence = "python is a language, python programming is easy"
list_ = sentence.split()
d = {}
for word in list_:
    d[word] = len(word)
print(d)
print()"""
# write a program to create a dictionary with word and it's length pair only if the word is of even length
"""sentence = "python is a language, python programming is easy"
list_ = sentence.split()
d = {}
for word in list_:
    if len(word) % 2 == 0:
        d[word] = len(word)
print(d)
print()"""
# write a program to create a dictionary with word and it's length pair only if the word is starting with vowel
"""sentence = "python is a language, python programming is easy"
list_ = sentence.split()
d = {}
for word in list_:
    if word[0] in "AEIOUaeiou":
        d[word] = len(word)
print(d)
print()
list_ = sentence.split()
d = {}
for word in list_:
    if word[0].lower() in "aeiou":
        d[word] = len(word)
print(d)
print()"""
# write a program to create a dictionary with it's word and it's count only if the word is not repeated
"""sentence = "python is a language, python programming is easy"
list_ = sentence.split()
d = {}
for word in list_:
    if list_.count(word) == 1:  # if we want repeated values ('list_.count(word) > 1')
        d[word] = list_.count(word)
print(d)"""

# write a program to reverse the values in the dictionary if the value is of type string
"""d = {"a" : "hello", "b": 100, "C": 10.2, "d": "world"}
for key, value in d.items():
    if isinstance(value, str):
        d[key] = value[::-1]
print(d)"""

# write a program to get all duplicate items and number of times the item is repeated in the list
"""names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
d = {}
for name in names:
    count = names.count(name)
    if count > 1:
        d[name] = count
print(d)"""

# write a program to get the following output
"""sentence = "hello world welcome to pyhton programming hi there"
op = {"h": ["hello", "hi"], "w":["world", "welcome"], "t": ["to", "there"], "p": ["python", "programming"]}
d = {}
#using ....in book"
list_  = sentence.split()
for word in list_:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] +=[word]
        #d[word[0]].append(word)
print(d)

#using defaultdict
from collections import defaultdict
dd = defaultdict(list)
for word in list_:
    dd[word[0]] += [word]
    # or we can use dd[word[0]].append(word)
print(dd)"""

# write a program to create a dictionary with element and it's index pair in the given list
"""names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# normal dictionary
d = {}
for index, item in enumerate(names):
    if item not in d:
        d[item] = [index]
    else:
        d[item] += [item]
print(d)
        
# defaultdict method

from collections import defaultdict
dd = defaultdict(list)
for index, item in enumerate(names):
    dd[item] += [index]
print(dd)

# write a program to flip the key and value

d = {"a": 1, "b": 2, "c": 3}
d1 = {}
for key in d:
    value = d[key]
    d1[value] = key
print(d1)

# using d.items()
d2 = {}
for key, value in d.items():
    d2[value] = key
print(d2)"""
































































     
