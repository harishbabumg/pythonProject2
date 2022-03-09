# 31012022
"""Q1. Write a program to create a list of squares for the elements in the below list"""
# l = [1, 2, 3, 4, 5]
# # normal method
# res = []
# for i in l:
#     res.append(i ** 2)
# print(res)
#
# # comphrension method
# res = [i ** 2 for i in l]
# print(res)
#########################
# l = [1, 2, 3, 4, 5]
# op = [item for item in l]
# print(op)

"""Q2.write a program to create a list of tupples which is having index and it's corresponding in the lisr"""
# l = ["python", 10, 3.2, "selenium", "Java"]

#normal method
# l_index = []
# for item in enumerate(l):
#     l_index.append(item)
# print(l_index)

#comphrension method
# l_index = [(index, item) for index, item in enumerate(l)]
# print(l_index)
# # [OR]
# l_index = [item for item in enumerate(l)]
# print(l_index)

"""Q3. write a program to create a list of even numbers from the below list"""
# l= list(range(10))
# normal method
# evens = []
# for i in l:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)

# comprehension
# evens = [item for item in l if item % 2 == 0]
# print(evens)

"""Q4. Write a program to create a list of even and odd numbers separately"""
# l = list(range(10))
# evens = []
# odds = []
# for item in l:
#     if item % 2 == 0:
#         evens.append(item)
#     else:
#         odds.append(item)
# print(evens,odds)

# comprehension
# l = list(range(10))
# evens = [ i for i in l if i % 2 == 0]
# odd = [i for i in l if i % 2 != 0]

"""Q5 write a program to create a lost using the following list if the word is of even length store the word as it is 
if it is of odd length reverse the word and store it"""
l = ["python", "Node JS", "Selenium", "Java"]
#normal method
# res = []
# for item in l:
#     if len(item) % 2 == 0:
#         res.append(item)
#     else:
#         len(item) % 2 != 0
#         res.append(item[::-1])
# print(res)

# comprehension method
# res = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(res)

"""Q6 write a program to create a list from the following list if the elements are of type strings keep them as it is
else reverse it"""
l = ["Java", "Python", 10, True, 1.4, "C++", "Ruby"]
output = []
# normal method
# for item in l:
#     if not isinstance(item, str):
#         output.append(str(item)[::-1])
#     else:
#         output.append(item)
# print(output)

# comprehension
# output = [str(item)[::-1] if not isinstance(item, str) else item for item in l]
# print(output)

"""Q7 write a list comprehension to create a list with the strings starting with vowels"""
files = ["Amazon", "Apple", "Flikart", "Walmart", "Gmail", "Yahoo"]
output = [file for file in files if file[0].lower() in "aeiou"]
print(output)
