"""Q1.set comprehension to create a set of squares from 1 to 10"""""
# res = set()
# for i in range(1, 11):
#     res.add(i ** 2)
# print(res)
#
# res = {i ** 2 for i in range(1, 11)}
# print(res)

"""Q2 write a set comprehension to create a set of tuples of item and it's index """
# list_ = ["Java", "Python", 10, 1.4, True, "C++", "Ruby"]
# res = {item for item in enumerate(list_)}
# print(res)

"""Q3 to creat a set of tuples with item and its length pair"""
# files =("Amazon", "Flipkart", "Walmart", "Gmail", "Yahoo")
# set_ = {(item, len(item)) for item in files}
# print(set_)

"""Q4 write a program to traverse through set and print each element"""
# set_ = ["python", "dad", "hai", "malayam","madam", "mom"]
# res = {item for item in set_}
# print(set_)

"""Q5 Write a program to print elements in the set in reversed order"""
# set_ = ["python", "dad", "hai", "malayam","madam", "mom"]
# res = {item for item in set_[::-1]}
# we cannot reverse it using reversed class as it accepts only sequences

"""Q6 write a program to remove the given element from the set"""
set_ = {"python", "dad", "hai", "malayam","madam", "mom"}
ele = "hai"
res = {item for item in set_.popitem(ele)}
print(res)