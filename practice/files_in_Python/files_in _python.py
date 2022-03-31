import csv
import xlrd
import urllib
import os
import sys
# f = open('myfile.txt', 'w')
# string = input("Enter text: ")
# f.write(string)
# f.close()
#
# f = open("myfile.txt", "r")
# n = f.read()
# print(n)

"""read characters from a file"""

# f = open("myfile.txt", "r")
# string = f.read()
# print(string)

# o/p->
# Hi, HB.
# This a sample file.

# f = open("myfile.txt", "r")
# string1 = f.read(4)
# print(string1)

# o/p-> Hi,  <only characters are printed>


"""Program to store a group of stings into a text file"""

# f = open("p3file.txt", "w")
# string = input("Press enter and Start writing below")
# #
# # #
# while string != "@":
#     string = input()
#     if (string != "@"):
#         f.write(string + "\n")
#     else:
#         f.close()
# f = open("p3file.txt", "r")
# print(f.read())
# print(f.readlines())
# print(f.read().splitlines())

"""append+"""

# f = open("p3file.txt", "a+")
#
# string = input("Press Enter and enter text to append:")
# while string != "@":
#     string = input()
#     if string != "@":
#         f.write(string + "\n")
# f.seek(0,0)
# print("The file contents are: ")
# string = f.read()
# print(string)
# f.close()

"""Knowing whether a file exists or not"""
# import os
# import sys
#
# fname = input("Enter file name: ")
# if os.path.isfile(fname):
#     f = open(fname, "r")
#
# else:
#     print(fname+ " does not exist")
#     sys.exit()
#
# string = f.read()
# print(string)
# f.close()


"""to count number of lines and words and character"""
# fname = input("Enter file name: ")
#
# if os.path.isfile(fname):
#     f = open(fname, "r")
# else:
#     print("file not exist")
#     sys.exit()
# cl = cw = cc = 0
#
# for line in f:
#     words = line.split()
#     cl = cl + 1
#     cw = cw + len(words)
#     cc = cw + len(line)
#
# print(f"No. of lines {cl}")
# print(f"No. of words {cw}")
# print(f"No. of characters {cc}")

"""With statement"""
# f = open("sam_with.txt", "w")
# string = input("Enter anything: ")
# f.write(string)
# f.seek(0,0)
# with open('sam_with.txt', 'r') as file:
#     for line in file:
#         print(line)

"""pickle in python"""

# class Emp(object):
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print("{:10d} {:10s} {:10.2f}".format(self.id, self.name, self.salary))

# e = Emp(12, "HB", 5000)
# print(e.name)
# e.display()
#
# """Above program will imported <from files_in_python import Emp>"""
# import pickle
# import Emp
# # pickling
# f = open("emp.dat", "wb")
# n = int(input("How many employees? "))
#
# for i in range(n):
#     print("-" * 50)
#     id = int(input("Enter id: "))
#     name = input("Enter name: ")
#     salary = input("Enter salary: ")
#     print("-"*50)
#     e = Emp.Emp(id, name, salary)
#     pickle.dump(e, f)
# f.close()

# unpickling

# f = open("emp.dat", "rb")
# print("Employee's details: ")
#
# while True:
#     try:
#         obj = pickle.load(f)
#         obj.display()
#     except EOFError:
#         print("End of file reached...")
#         break
# f.close()




"""seek() and tell() methods"""
# open("line.txt", "w")
# with open("line.txt", "r+b") as file:
#     file.write(b"Amazing Python")
#     file.seek(3)
#     print(file.read())
#     file.seek(0,0)
#     print(file.tell())
#     file.seek(-1, 2)
#     print(file.read())
#     print(file.tell())

"""OS Module"""

# to know the currently working directory

import os
current = os.getcwd()
# print(current)

# to create our own directory
# os.mkdir("mysub")
# os.mkdir("mysub/mysub2")
# current = os.getcwd()
# print(current)

# to create directory if not already existed



#  to change the current directory
# to remove a directory
# to remove the multiple directory

# to remove

"""working"""
# os.mkdir("mysub")  # creating a dir
# os.rmdir("mysub")  # removing a dir
# os.mkdir("mysub")  # creating a dir
# os.rmdir("mysub")  # removing a dir

"""creating a multiple dirs and deleting the same"""
# os.makedirs("mysub/mysub1/mysub3/mysub4")
# os.removedirs("mysub/mysub1/mysub3/mysub4")

"""change to another directory"""
# goto = os.chdir("mysub")
# current = os.getcwd()
# print(current)  # changes to mysub <befoee mysub should created>
#
"""to remane the directory"""
# os.chdir("HB_1")
# os.rename("mysub1", "HB_HB")
# current = os.getcwd()
# print(current)

"""display al the contents of the current directory"""

# s = os.getcwd()
# path = s
# for dirpath, dirnames, filenames in os.walk(path):
#     print(f"Current path: {dirpath}")
#     print(f"Directories: {dirnames}")
#     print(f"filenames: {filenames}")

"""running other programs from python programs"""
# print(os.system("dir"))
# print(os.system("dir *.py"))

