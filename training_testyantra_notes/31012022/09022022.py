path = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\training_testyantra_notes\31012022\reading_files\sample.txt"
path_ = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\training_testyantra_notes\31012022\reading_files\access-log.txt"

from collections import Counter

# with open(path) as file:
#     for line in file:
#         print(line)
#
# with open(path) as file:
#     for line in file:
#         res = len(str(line).split())
#         print(res, end=" ")




# with open(path) as file:
#     count = 0
#     for line in file:
#         d = line.split()
#         for word in d:
#             count += 1
# print(count)
#
# # or
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         count += len(words)
#     print(count)

# with open(path) as file:
#     for line in file:
#         res = reversed(list(file))
#         print(list(res))

""" WAP to count the number of spaces in the given file"""

# with open(path) as file:
#     count = 0
#     for line in file:
#         res = str(line)
#         for i in res:
#             if i == " ":
#                 count += 1
#     print(count, end=" ")

# [OR]

# with open(path) as file:
#     count = 0
#     for line in file:
#         spaces = line.count(" ")
#         count += spaces
#     print(count)

### wap to count the number of words that are starting with vowels

# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0].lower() in "aeiou":
#                 count += 1
#     print(count)

# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0] in "aeiouAEIOU":
#                 count += 1
#     print(count)


## WAP to create a dictionary of word and its count pair in the given file
#
# from collections import defaultdict
# d = defaultdict(int)

# with open(path) as file:
#         for line in file:
#             for word in line.split():
#                 d[word] = d[word] + 1
#         print(d)

# with open(path) as file:
#     for line in file:
#         d = {}
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if word not in d:
#                     d[word] = 1
#                 else:
#                     d[word] += 1
#     print(d)

#  WAP to abstract all the ip addresses from access log.text file

# with open(path_) as file:
#     for line in file:
#         sente = line.split()
#         print(sente[0], end=" ", sep="-->")

# or

# with open(path_) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             list_ = line.split()
#             l.append(list_[0])
#     print(l)            # classnotes

# ip_ = Counter(l)
# print(ip_)
# print(ip_)
# print(ip_.most_common())
# print(ip_.most_common(1)  # gives first common element


#  WAP to create a dictionary of ip addresses and their count

# from collections import defaultdict
#
# with open(path_) as file:
#     d = defaultdict(int)
#     for line in file:
#         for line_ in line.split():
#             d[(line_[0])] += 1
#     print(d)
#
# # OR   incomplete program need corrections
#
# ip_ = Counter(l)


#  WAP to print nth line in the file
# n = 3
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no == n:
#             print(line)
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         count = 1
#         if count == n:
#             print(line)
#             break
#  islice

from itertools import islice
# n = 3
# with open(path) as file:
#     res = islice(file, n-1, n)
#     print(list(res))


#  WAP to print first n lines of the files
# n = 3
# with open(path) as file:
#     res = islice(file, 0, n)
#     print(list(res))
#
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no <= n:
#             print(line)

# WAP to print last n lines

n = 5
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     res = islice(file, count-n, count)
#     # print(list(res))

# [or]
# using deque(iterable, [number])
# from collections import deque
# with open(path) as file:
#     lines = deque(file, n)
#     print(list(list(lines)))

##################################################################################
f_path = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\training_testyantra_notes\31012022\reading_files\f_path"
# WAP to copy the content of the sample.txt into different file

# with open(path, "r") as file_read, open(f_path, "w") as file_write:
#         for line in file_read:
#             file_write.write(line)
