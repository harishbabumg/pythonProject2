# # First class 18012022 - print function, End function, Separate function.
#
a = "raju balu anju"
b = "hai welcome"
c = "bmtc ksrtc"
#
# print(a)
# print(b)
# print(c)
# print()
# print("a")  # if we use "" before and after 'a' system prints only 'a'.
# print("b")  # if we use "" before and after 'b' system prints only 'b'.
# print("c")  # if we use "" before and after 'c' system prints only 'c'.
#
# # End: used to append(add at the end)
#
# print(a)
# print(b)
# print(c)
#
# #  we can use the value directly, or we can use the variable instead.
#
# print("raju balu anju", end=' %% ')
# print("hai welcome", end=' && ')
# print("bmtc ksrtc")  # prints raju balu anju @@ hai welcome !! bmtc ksrtc
#
# print(a, end=' %% ')
# print(b, end=' && ')
# print(c)  # prints raju balu anju %% hai welcome && bmtc ksrtc
#
# print("raju balu anju", "\t\t\t\t\thai welcome", "\n\nbmtc ksrtc")
# #  \n - next line and \t - next tab.
#
# # Separate: adds specified string in between the values
#
# print(a, b, sep=" %% ")  # prints - raju balu anju %% hai welcome
# print(a, b, c, sep=" ^^ ")  # prints raju balu anju ^^ hai welcome ^^ bmtc ksrtc
# print()
#
# #  input() function -  this functions takes a value from the keyboard and returns it as string. At runtime.
#
# """
# string = input('Enter your name: ')  # after this in the output terminal we have enter our name.
# print(string)
# x = int(input('Enter your age: '))
# print(x)
# y = float(input('Enter any number(decimal type) of your choice: '))
# print(y)
# print()
#
# # Integers
#
# a1 = 10
# a2 = int(10)
# print(a1 == a2)
#
# # Operators
#
# # addition
# add = 3 + 2
# print(add) #prints 5
#
# # subtraction
# subt = 3-2
# print(subt)
#
# #  Multiplication
# mul = 3*2
# print(mul)  #  Prints

# # Division
# Div = 3/2
# print(Div) #prints 1.5
#
# # Floor division
#
# fldiv = 3//2
# print(fldiv) # prints the answer as '1', 3/2 = 1.5 hence it follows 1.5>1.
#
# # Exponent
# expo = 2**3 # 2 to the power of 3 2*2*2 = 8
# print(expo)
#
# # Modulus
#
# mod = 5 % 3
# print(mod) # gives only the remainder.
#
# # divmod
#
# div1 = 5
# div2 = 3
# print(divmod(div1, div2))  # gives in (quotient (div1 // div2), remainder (div1 % div2) 5/3 = Quo-1 Rr-2.
#
# #abs
#
# abbs = -6565
#
# print(abs(abbs))  # the output always be in positive.
#
# #Round off
#
# rou = 2.362656485688112505
# rou1 = 5.53565862001256245
# print(round(rou))  # rounds off to nearest value +/- to 0.5. 2.3 is near to 2.0 hence will print 2
# print(round(rou1))  # 5.5 is nearest to 6 hence prints it prints 6
# print(round(-12.26565467))
#
# # round off to 'n'th' decimal point
# print(round(rou, 3))  # rounds off the number to 3rd decimal point
#
# import math
#
# mathss = 1.2334324343
# mathss1 = 5.65652
# print(math.trunc(mathss))  # it removes all the numbers present after decimal. prints 1
# print(math.trunc(mathss1))  # it removes all the numbers present after decimal. prints 5
#
# # complex number
# comp = 1+2j
# comp1 = 2-2j
# print(comp1 - comp)  # prints (1-4j)
#
# cmp = 1
# cmp2 = 2
# print(complex(cmp, cmp2))  # it considers 1 as real number and 2 as imaginary part.
#
# # Booleans
#
# bool1 = 10
# print(bool(bool1))  # gives True as bool1 is not default value
# bool2 = 0
# print(bool(bool2))  # gives False as default value of boolean is 0
#
# bool3 = bool1>bool2
# print(type(bool3))  # bool1>bool2 is also considered as boolean type
#
# #type casting
#
# typcas = 10 # converts one data type to another
# print(float(typcas))  # prints in form of float as 10.0
# typcass1 = 12.564
# print(int(typcass1))  # prints only the number present before the decimal point.
# typcass2 = 50
# print(complex(typcass2))  # prints (50+0j)
# print(bool(typcass2))  # prints True
#
# #  Default value give boolean as false
# print(bool(0))
# print(bool(0.0))
# print(bool(0+0j))  # all the values will give False.
#
# #  isinstance - returns True if the specified object is of the specified type, otherwise it gives false.
isin = 23
# print(isinstance(isin, int))  # 23 is integer hence it gives True
# print(isinstance(isin, float))  # 23 is not a float hence it gives False
# print(isinstance(isin, bool))  # 23 is not a Bool hence it gives False
# print(isinstance(isin, (bool, float, str, complex)))
# print(isinstance(isin, (bool, float, str, complex, int)))
# #  if object belongs to anyone of the datatype then it gives True
# print(isinstance(isin, (bool, float, str, complex, int)))  # as int is present, system gave True.
#
# #  length - finds the number of character in the string
# print()
lengg = "Namaskara"
# print(len(lengg))  # prints the number '9' as there are 9 characters.
# print(len("Namaskara")) # gives the same result as the above
#
# # string constructor
# print(str("Namaskara Bengaluru"))
# sttor = 12356546
# print(type(sttor))
# print(str(sttor))
# print(type(sttor))  # variable cannot be overridden and still gives type <type>
# res_ = str(sttor)
# print(type(res_))  # now it gives type <str>
#
# #  Zero length string or an empty string
# print("")
# print(str())  # Prints empty string see the output.
# print("3")
# print()
# # Indexing of string - process extracting a single character at a time.
# indestr = "Tumakuru"
# print(len(indestr))
# print(indestr[0])  # prints the 0'th character of the above string
# print(indestr[-1])  # prints last'th character of the above string
# print(indestr[-8])  # 0'th character = - length of the string.
# print(indestr[7])  # prints last character of the above string
# print()
# #  Slicing of a string - Process of extracting single/group of character/s at a time.
slofstr = "Namma_bhashe_kannada"
# print(slofstr)
# print(len(slofstr))  # prints 20
# print()
# print(slofstr[0::])  # prints as it is. [Start index: End index: Step value]
# print(slofstr[0:20:1])  # starts from 2nd character
# print(slofstr[0:200:1])  # it considers only the characters present.
# print(slofstr[::-1])  # prints in reverse order - adannak ehsahb ammaN
# print(slofstr[-1:4:-1])
# print()
# #  Raw string - they don't treat backslash as a part
# rwstr = "Madhugiri betta"
# print(rwstr)
# print("Madhugiri be\tta")  # normally output include tab
# print(r"Madhugiri be\tta")  # output neglects \t
# print()
#
# #  string formatting
# #  Formatting with placeholder
# placehold = "Namaste my name is %s."%"HB"
# print(placehold)  # prints - Namaste my name is HB
# placehold1 = "Namaste my name is %s and I am %d years old" %("HB", 26) # s,d - doubt
# print(placehold1)
# placehold2 = "The value is %0.4f" %(3.141592)  # 0.4 means to 4th decimal point 0.4 - ?doubt
# print(placehold2)
# print()
#
# #  Format() string method -formatting done by calling format() method
# forstring = "Hi my name is {} and I am {} years old" .format("HB", 26)
# print(forstring)  # prints Hi my name is HB and I am 26 years old
# forstring2 = "Hi my name is {1} and I am {0} years old".format(26, "HB")
# print(forstring2)  # 26 in 0th index and HB is in 1st index
# forstring3 = "Hi my name is {name} amd I am {age} years old".format(age=26, name="HB")
# print(forstring3)  # print as specified at the end
#
# #  Formatted string literals (f-string) - can use outside variables directly
#0
# fstraa1 = 24
# fstraa2 = "day"
# fstraamessage = f"There are {fstraa1} hours in a {fstraa2}"
# print(fstraamessage)  # values used in the above message
# fstraamessage1 = f"one {fstraa2} has {fstraa1 * 60} minutes"
# print(fstraamessage1)
# print()
#
# # lower() & upper()
# print("NaMaskara BeNgaLUrU".lower())  # prints all letter in lower case
# print("NaMaskara BeNgaLUrU".upper())  # prints all letter in upper case
# print()
#
# #  count()
# acount0 = "Hello world, Hello universe"
# print(acount0.count('l')) # counts no. of 'l' present in the above string
# print(acount0.count('Hello', 0,-1))  # counts occurrence of 'Hello' from o to last(-1) index
# print()
#
# #  find() and rfind()
# messfind = "Bhoothayyana maga ayyu"
# print(messfind.find("y"))  # prints the index of first 'y' from LHS. 7
# print(messfind.rfind('y'))  # prints the index of the 'y' from RHS. 20
# print(messfind.find("maga"))  # 'maga' starts from index 13 from LHS
# print(messfind.rfind("maga")) # 'maga' starts from index 13 from RHS
# print(messfind.find('m'))  # index of 'm' is at 13
# print(messfind.find('deva'))  # when we try to find the characters which isn't present it prints -1.
# print()
# messfind1 = "Today is beautiful day"
# print(len(messfind1))
# print(messfind1.find("day"))  # at index 2 'day' starts from LHS considers the first occurrence of the word.
# print("Today is beautiful day".rfind("day"))  # 'day' is at 19th index calculates from RHS
# print(messfind1.find("day, 0, 5"))  # it searches the word 'day in between oth index and 5th index.
# print(messfind1.find("day", 0, 22))  # the 1st occurrence of 'day' is at 2nd index if not found returns -1.
# print()
#
# #  index and rindex - similar to find
# print(messfind1)
# print(messfind1.index('is'))  # 'is' starts from 6th index
# print(messfind1.rindex('is'))  # 'is' starts from 6th index
# print(messfind1.index('o', 0, 5))  # op '1', searches the word 'day in between oth index and 5th index from LHS
# print(messfind1.rindex('y', 0, 22))  # op '21',searches character in between o'th index and 22'th index from LHS
# #  print(messfind1.index("night"))  # results in value as "night" is not present in string
# print()
#
# #  replace() - replaces specified phrase with another
# # print("Shivamogga".replace("i", "z"))  # replaces 'i' with 'z'.
# # print("I am from Tumakuru".replace("Tumakuru", "Madhugiri"))  # replaces Tumakuru with Madhugiri
# # print("MALAYALAM".replace("p", "Z", 1))  # no error was thrown even with input which is not existed
# # print("MALAYALAM".replace("A", "z", 3))  # # replace 'A' with 'Z' for 3*'A's present in string.
# # print("MALAYALAM".replace("A", "z", 4))  # replace 'A' with 'Z' for 4*'A's present in string.
#
# #  startswith - returns True if the string starts with the specified value
# string_ = "Namaskara Bengaluru"
# print(string_.startswith("Bengaluru"))  # prints False
# print(string_.startswith("Namaskara"))  # prints True
#
# # endswith - returns True if the string ends with the specified value
# print(string_.endswith("Bengaluru"))  # prints True
# print(string_.endswith("Namaskara"))  # prints False

# split() - splits string at specified seperator and returns as list
string__ = "bennu hatthidha byiraagi"
# print(string__.split('s'))  # prints 'string__' itself ['bennu hatthidha byiraagi']
# print(string__.split(' '))  # prints ['bennu', 'hatthidha', 'byiraagi'] splited at 'space'
# print(string__.split())  # prints ['bennu', 'hatthidha', 'byiraagi'] splited at 'space'
# print(string__.split("t"))  # ['bennu ha', '', 'hidha byiraagi']
# print(string__.split("b"))  # ['', 'ennu hatthidha ', 'yiraagi']
# print(string__.split(" ", 1))  # splits at first space only
# print(string__.split("a", 1))  # splits at first 'a'

# Join() - Joins the elements of an iterable using the string specified (accepts only string)
# data = "Hai"
# print(data.join(["hello", "world"]))  # helloHaiworld
# message = "Swagatha"
# print(message.join(["hello", "world"]))  # helloSwagathaworld
# print('_'.join(message))  #  S_w_a_g_a_t_h_a
# print('_'.join("S_w_a_g_a_t_h_a"))  # S___w___a___g___a___t___h___a
# print('*'.join(message))  # S*w*a*g*a*t*h*a
# print(" ".join(message))  # S w a g a t h a

# strip(), lstrip(), rstrip() - removes leading and trailing characters

strin_ = "@@##$$HBMG$$##@@"
# print(strin_.strip("@@"))  # ##$$HBMG$$## string.strip() removes on both side
# print(strin_.strip("##"))  # @@##$$HBMG$$##@@ doesnot remove inbetween characters
# print(strin_.lstrip('@@'))  # ##$$HBMG$$##@@ removes only left
# print(strin_.rstrip('@@'))  # @@##$$HBMG$$## only right
#
# string1 = "singanahalli pakka ramohalli"
# print(string1.strip("ramohalli"))  # singanahalli pakka
# print(string1.strip("singanahalli"))  #  pakka ramo
# print(string1.lstrip("ramohalli"))  # singanahalli pakka ramohalli
# print(string1.rstrip("ramohalli")) # singanahalli pakka

#  isalnum()
# a = "1232"
# b = "a!2"
# c = "asa1dsd"
# d = "addaf"
# e = "       "
# print(a.isalnum())
# print(b.isalnum())
# print(c.isalpha())
# print(d.islower())
# print(d.isupper())
# print(a.isnumeric())
# print(a.isdigit())
# print(e.isspace())

#           LIST
# indexing
# a = [[1,2], 3, 4]
# print(a[0][1])
# print(a[2])

# slicing of set [start value : end value : step value]
# a = [10, "hello", "Balu", "Raju", 1254, True]
# print(a[0: 2])  # prints only first two value
# print(a[::])  #  by default it prints [10, 'hello', 'Balu', 'Raju', 1254, True]
# print(a[0: len(a): 1])  #  by default it prints [10, 'hello', 'Balu', 'Raju', 1254, True]
# print(a[(-len(a)): (1+len(a)): 1])  # prints [10, 'hello', 'Balu', 'Raju', 1254, True]
# print(a[::-1])  # reverse

# merging two sets
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [[1,2], 45, 67]
# print(*l1, *l2, *l3)  # prints [1, 2, 3, 4, 5, 6, [1, 2], 45, 67]
# print(type(print(*l1, *l2, *l3))) # 1 2 3 4 5 6 [1, 2] 45 67 'and' <class 'NoneType'>
# a = ["hai", 1, "hello", 2]
# b = [1, 2, 3, 4]
# print(a + b)  # packing
# print([*a, *b])  # packing

#  append()
# a = [23, 45]
# b = [11, 66]
# print(a.append(b))  # output is none
# print(a)  # prints [23, 45, [11, 66]]
# print(b)  # prints [11, 66]

# a = [10, 30, "hai", "python", 49]
# print(a.append(2.4))  # None
# print(a)  # prints [10, 30, 'hai', 'python', 49, 2.4]
# print(a.append("hai"))  # None
# print(a)  # prints [10, 30, 'hai', 'python', 49, 2.4, 'hai']

# extend()
# a = [23, 45]
# b = [11, 66]
# print(a.extend(b))  # prints None
# print(a)  # [23, 45, 11, 66] note: without braces
# print(b)  # prints[11,66]

# a = [10, 30, "hai", "python", 4.9]
# # print(a.extend(2.4))  # TypeError: 'float' object is not iterable
# print(a.extend("hai"))  # None
# print(a)  # [10, 30, 'hai', 'python', 4.9, 'h', 'a', 'i']  note - each character of the string is added separately


# insert() syntax = list.insert(position index, element)
# a = [1,2]
# print(a.insert(1,2))  # prints None inserts 2 at 1st index position
# print(a)

# a = [10, 30, "hai", "python", 4.9]
# print(a.insert(0, "Namasthe"))  # None
# print(a)  # ['Namasthe', 10, 30, 'hai', 'python', 4.9] - Namasthe at 0th index

# a = [10, 30, "hai", "python", 4.9]
# print(a.insert(2, "Namasthe"))  # None
# print(a)  # [10, 30, 'Namasthe', 'hai', 'python', 4.9] - namasthe at 2nd index

#  removing the element from the list - remove(), pop(), del
# pop()
# lis__ = [0, 1, 2, 3, 4, 5]
# print(lis__.pop())  # prints 5 by default last element is removed
# print(lis__)  #

# lis__ = [0, 10, 20, 30, 40, 50]
# print(lis__.pop(2))  # prints 20 and the same will be removed from the lis__
# print(lis__)

# lis__ = [0, 10, 20, 30, 40, 50]
# print(lis__.pop(23))  # IndexError: pop index out of range
# print(lis__)

# remove()
# list__ = [10, 20, 30, 40 , 50]
# print(list__.remove(2000))  # ValueError: list.remove(x): x not in list

# list__ = [10, 20, 30, 40 , 50]
# print(list__.remove(20))  # prints None
# print(list__)  # prints [10, 30, 40, 50]

# del()

# list__ = [10, 20, 30, 40, 50]
# del list__[0] # deletes 0th item in the list
# print(list__)  # prints [20, 30, 40, 50]

# list__ = [10, 20, 30, 40, 50]
# del list__[2:4]  # deletes 2nd, 3rd item in the list
# print(list__)   # prints [10, 20, 50]

# list__ = [10, 20, 30, 40, 50]
# del list__[::-2]  # deletes alternate items in the list
# print(list__)  # prints [20, 40]

#  copy()_shallow_copy

# a = [1, 2, 3, 4, 5]
# b = a
# print(id(a) == id(b))  # prints True

# a1 = [1, 2, 3, 4, 5]
# b1 = a1.copy()
# print(id(a1) == id(b1))  # prints False

# a2 = [1, 2, 3, [0, 23]]
# b2 = a2.copy()
# print(id(a2) == id(b2))  # prints False

# print(id(a2[-1]) == id(b2[-1]))  # prints True

# prints True, even though we copy separately,
# the nested list[0,23] will not be saved in two different memories instead controller points towards
# the same memory, if we change the value in nested list of a2 then the change reflects in nested list of b2 as well,
# to overcome this we use deep copy.

# deepcopy()

# from copy import deepcopy
# a = [1,2,3, 300]
# b = [23,45,674]
# a = b
# print(id(a) == id(b))
#
# a1 = [1, 2, 3, 4, 5, ["Jai Sri Ram"]]
# b1 = deepcopy(a)
# print(id(a1) == id(b1))
# print(id(a1[-1]) == id(b1[-1]))  # here even nested set's value have different memory location,
# # if we change the nested values of 'a1' no impact will be made in nested values of 'b1 set
