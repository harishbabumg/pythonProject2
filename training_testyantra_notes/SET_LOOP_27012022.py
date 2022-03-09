"""list_ = ["Java", "python", 10, True, 1.4, "C++", "ruby"]
res = []   
for item in list_:
    if isinstance(item, str):
        print(item[-1:0:-1], end=" ")
print(item)
print()
#  write a program to print the elements which are starting with vowels
files = ["Amazon", "flikart", "walmart", "gmail", "yahoo"]

for item in files:
    if item[0] in "aeiouAEIOU":
        print(item)
print()"""
"""#  write a program to print only extensions of the elements
files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
res = []

for char in files:
    res.append(char.split('.')[1])
print(res)

for file in files:  #  by ma'am
    a = file.split(".")
    print(a[-1])"""

#  write a program to print the file name if the file name is of odd length
files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]

"""for item in files:
    a = item.split(",")
    if len(a[0]) % 2 == 0:
        pass
    else:
        print(a[0])"""
print()         #both gives same output
"""for item in files:
    a = item.split(",")
    if len(a[0]) % 2 != 0:
        print(a[0])
    else:
        pass"""

#  WAP to return the index of the first occurrence of the given elements
numbers = [10, 40, 20, 80, 20, 40, 30]
num = 40
#  using index()"""
#  print(numbers.index(num))"""
print()
#  enumerate method"""
"""for index, item in enumerate(numbers):
    if item == num:
        print(f"{num} is present at the index {index}")
        break  # to stop the execution of any loop we use break.
print()
#  if don't use break
for index, item in enumerate(numbers):
    if item == num:
        print(index)  # results will be 1 and 5"""
print()
# Prime numbers"""
"""n = 15
for i in range(2, n):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")"""
# to generate prime number series

"""n = 2
for n in range(10):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)"""
print()
#  write a program to print all the elements other than given elements
"""numbers = [10, 40, 20, 80, 20, 40, 30]
n = 20

for num in numbers:
    if n == num:
        continue
    print(num)
print()"""
""" WAP to print all the palindromes in the given list"""
"""l = ["python", "dad", "hai", "malayalam", "madam", "mom"]
for i in l:
    if i == i[::-1]:
        print(i)"""
# SETSETSETSETSETSETSETSETSETSETSETSETSETSETSETSETSETSETSETSETSETSET

#  write a program to traverse through set and print each element

# set_ = {"python", "dad", "hai", "malayam","madam", "mom"}
# for item in set_:
#    print(item)

#  Write a program to print elements in the set in reversed order

"""we cannot reverse it using reversed class as it accepts only sequences"""
print()
#  write a program to remove the given element from the set
#set_ = {"python", "dad", "hai", "malayam","madam", "mom"}
#key = "hai"
#for ele in set_:
#    if ele == key:
#        set_.discard(key)  # RuntimeError: Set changed size during iteration
#        break
#print(set_)
#print()

# write a program to create a set with the list elements if the element is palindrome

#list_ =["python", "dad", "hai", "malayalam", "madam", "mom"]
#res = set()
#for i in list_:
#    if i == i[::-1]:
#        res.add(i)
#print(res)
print()

# ZIP-OBJECTS

"""s1 = "hai"
s2 = "hey"
s3 = "are"

# print(zip(s1, s2))
for item1, item2, item3 in zip(s1, s2, s3):
    print(item1, item2, item3, sep=" - ")"""


   




#  different lengths
# s = "hai"
# s1 = "hello"
#
# for i1, i2 in zip(s, s1):
#     print(i1, i2) # when 'zip'
# print()
# from itertools import zip_longest
# for i1, i2 in zip_longest(s, s1, fillvalue="not present"):
#     print(i1, i2)


















































