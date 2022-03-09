path = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\files_directory\txt_log_files\reading_files\sample.txt"
path_ = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\files_directory\txt_log_files\football.txt"

# WAP to find the length of each line in the text file

# with open(path, "r") as file:
#     for line in file:
#         if line.strip():
#             res = (len(line) - 1)
#             print(res, end=" ")
            # res1 = str(res)
            # print()
            # print(type(res), end=" ")
#
#  [OR]
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         l = line.split()
#         print((F"line no. {count}", f"total no. words {len(l)}"))

# write a program to read countries from football.txt

# with open(path_, encoding="UTF-8") as file:
#     for line in file:
#         if line.strip():
#             country = line.split("\t")
#             print(country[1])


# WAP to find most occurrence and least occurrences of the words

# from collections import defaultdict, Counter
# d = defaultdict(int)
#
#
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             words = line.split()
#             for word in words:
#                 d[word] += 1
# print(d)
# d = Counter(d)
# most, *rest, least = d.most_common()
# print(most, least)

#################################################################################################
# import csv
#
# with open("example.csv", "w") as csv_:
#     write_obj = csv.writer(csv_)
#     write_obj.writerow(["x", "y", "z"])
#     write_obj.writerow([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
#
# with open("example.csv", "w") as csv_writer:
#     dictwriter_obj = csv.DictWriter(csv_writer, ["x", "y", "z"])
#     dictwriter_obj.writeheader()
#     dictwriter_obj.writerow({"x": 10, "y": 20, "z": 30})
######################################################################

# WAP to read all the names of the employees in employee.csv file
e_path = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\files_directory\csv_files\employees.csv"

import csv
#
# with open (e_path) as csv_file:
#     r_obj = csv.reader(csv_file)
#
#     for row in r_obj:
#         print(row[0])

# WAP to print only the names with salaries >70000

# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     print(header)
#     for row in r_obj:
#         if int(row[3]) > 70000:
#             print(row[0])
#

# WAP to group male and female employee

# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     d = {"male": []}, {"female": []}
#     for row in r_obj:
#         if row[1] == "male":
#             d["male"] += [row[0]]
#         else:
#             d["female"] + [row[0]]

from collections import defaultdict
# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     dd = defaultdict(list)
#
#     for row in r_obj:
#         dd[row[1]] += [row[0]]
# print(dd)

# WAP to group employees based on their team

# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     dd = defaultdict(list)
#
#     for row in r_obj:
#         dd[row[2]] += [row[0]]
# print(dd)
#
# d = {}
# for row in r_obj:
#     if row[2] not in d:
#         d[row[2]] = [row[0]]
#     else:
#         d[row[2]] += [row[0]]

# WAP to sort shares in text.csv file based on the share prices

path_1 = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\files_directory\csv_files\test.csv"

# with open(path_1) as file:
#     read_obj = csv.DictReader(file)
#     l = list(read_obj)
#     res = sorted(l, key=lambda d: float(d["price"]))
#     print(list(res))

# Write a program to add all the shares in test.csv file
with open(path_1) as file:
    read_obj = csv.reader(file)
    shares = 0
    next(read_obj)
    for row in read_obj:
        shares += int(row[1])
    print(shares)
