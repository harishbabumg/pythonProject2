# Write a program to print a tuple of character and its ascii value in the given string.
# s = "hello world"
# write a program to check whether the given number is prime or not.
#a = 5
# if a % 2 == 1:
# 3) write a program to print the sum of all the digits present in the string.
# a = "12Alpha78python"
# total_sum = 0
# for item in a:
#     if item.isdigit():
#         total_sum += int(item)
# print(total_sum)
# #  [or]
# total_sum = 0
# for item in a:
#     if '0' <= item <= '9':
#         total_sum = total_sum + int(item)
# print(total_sum)

# 4) write a program to print all the consonants present in the list
#
# a = "ascdytweoiencaosijcmashpiiiwgvuhsa"
# b = 0
# for item in a:
#     if item.lower() not in "aeiou":
#         b += 1
#         print(item, end=" ")
# print()
# print(b, end=" ")

#  [or]

# s = "hai12 hello952 python#@$"
# count = 0 # initialising it to zero
# for char in s:
#     if char.isalpha():
#         if char not in "aeiouAEIOU":
#             count += 1
#            print(char, end=" ")
# print()
# print(count)

# 5) write a program to print a tupple of index, and it's character in the string
# s = "Hari"
# for i in range(len(s)):
#     print((s[i] , i), end=" ")

#  write a program to reverse a string using three ways.
# s = "ABCDE"
# for i in s[::-1]:
#     print(i, end=" ")
# print()
# for i in reversed(s):
#     print(i, end=" ")
# print()
# for i in range(len(s)-1, -1, -1):
#     print(s[i], end=" ")
# print()
#  write a program to extract only special characters from a string
# string_ = "Bhuthayya$$Appayya&&Devayya**Rudrayya"
# for item in string_:
#     if item.isalpha():
#         pass
#     else:
#         print(item, end=" ")  # $ $ & & * *

# write a program to check a given character if it is present return its index
# stringg = "Shankar_Guru"
# a = input("enter a character:")
# for item in stringg:
#     if stringg.find(a) in stringg:
#         print("yes it contains")
#     else:
#         print("character not found")
#       using range
# s = "Hai hello"
# char = "w"
# for i in range(len(s)):
#     if char == s[i]:
#         print(f"{char} is present at index {s[i]}")
#     else:
#         print(f"{s[i]} is not there")
