
"""1. Write a program to find the length of the string without using inbuilt function (len)"""


# def _len(iterable):
#     _count = 0
#     for item in iterable:
#         _count += 1
    # return _count


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
# string_ = convert_to_list('steve')
# print(string_)

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

"""8. Write program to convert upper case to lower case and vice-versa without using inbuilt method."""


def convert(any_string):
    l = []
    for c in any_string:
        temp = ord(c)   # Get the ASCII value of the character
        if int(temp) >= 97 and temp <= 122:
            l.append(chr(temp - 32))

        elif int(temp) >= 65 and temp <= 90:
            l.append(chr(temp+32))
    return ''.join(l)


d = convert('Hello WorlD')
print(d)

# Method HB

string_ = "Hello WorlD"
res = []
for char in string_:
    if 65 <= ord(char) <= 90:
        res.append(chr((ord(char)) + 32))
    elif 91 <= ord(char) <= 117:
        res.append(chr((ord(char)) - 32))
    else:
        pass

print("".join(res))
