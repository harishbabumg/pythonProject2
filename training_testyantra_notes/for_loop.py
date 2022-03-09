# #  1 to
# # for num in range(1, 11):
# #     print(num)
# #   ####################################
# # #  10 to 1
# #
# # for num in range(10, 0, -1):
# #     print(num)
# #      #############################
#
# #   ''' from-1 to 10
#
# # for num in range(-1, -11, -1):
# #     print(num)
#
# #   '''from -10 to -1
#
# # for num in range(-10, 0, 1):
# #     print(num)
#
# # ''' even numbers from 1 to 10
#
# # for num in range(1, 11):
# #     if num % 2 == 0:
# #         print(num)
#
# # ''' odd nuber
#
#
# # ''' traversing through strings
# string = "python"
# # for item in range(0, len(string)):  # item = reference value, we can take any name as reference value.
# #     print(string[item])
#
# # for char in string:
# #     print(char)  # prints the same as above.
#
# #  """ end
# # for item in range(len(string)):
# #     print(string[item], end=" ")
# # print()
# # for char in string:
# #     print(char, end=" ")
# #
# # print()
#
#
# #  ''' traversing through tupple
# string_ = (1, 2, "HB")
#
# for item in range(0, len(string_)):
#     print(string_[item])
#     for item in range(0, len(string_[2])):
#         print(string_[2])
#
# # traversing through lists'''''''''
# list_ = [10, 20, 30, 40]
# #
# for ele in list_:
#     print(ele, end=" ")
# print()
# for index in range(len(list_)):
#     print(list_[index], end=" ")
# print()
#
# # #  ########traversing through sets ''''''
# set_ = {"hai", "hello", "how", "are", "you"}
# for ele in set_:
#     print(ele, end=" ")
#
# #   """"'Traversing through Dictionary"''
#
# d = {"one": 1, "two": 2, "three": 3}
# for key in d:
#     print(key, d[key], sep="-->")
#
# #  ##################Assignments to print index and element in a string
#
# s = "hello"
# for item in range(len(s)):
#     print(item, s[item])
# print()
#
 # enumerate
# s = ("hello")
# for item in enumerate(s):
#     # print(item)
#     print(item[0], "-->", item[1])

# ===========traversing a string in reversed order'''
# string = "Hai"
# for item in range(len(string)-1, -1, -1):
#     print(string[item], end=" ")
# print()
# for char in string[::-1]:
#     print(char, end=" ")
# print()
# for item in reversed(string):
#     print(item, end=" ")
# print()

#  write a program to count the number of characters present in the given string without using len function
# string = "Shankarguru"
# count = 0
# for item in string:
#     count += 1
# print(count)  # it should printed outside.
# print()
#
#  WAP to print even indexed characters in the string

# string__ = "Kavirathna_Kalidasa"
# for item in range(0, len(string__), 2):
#     print(string__[item], end=" ")
# print()
# for item in string__[::2]:
#     print(item, end=" ")

########WAP to print the digits present inside the string

s = "putani agent 123456789"
# for char in s:
#     if char.isdigit():
#       print(char, end=" ")
# print()
#
# for char in s:
#
#     if "0" <= char <= "9":
#         print(char, end=" ")
#
#      count the number of digits present in the strng
# count = 0
# for char in s:
#     if "0" <= char <= "9":
#         count +=1
# print(count)


