# # Class Decorator
# #
# # class Log:
# #     def __init__(self, func):
# #         self.func = func
# #
# #     def __call__(self, *args, **kwargs):
# #         return self.func(*args, **kwargs)
# #
# #
# # @Log
# # def add(a, b):
# #     return a+b
# #
# #
# # @Log
# # def sub(a, b):
# #     return a-b
path = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\files_directory\csv_files\employees.csv"
#
# import csv
#
# #
# # with open(path) as file:
# #     rows = csv.reader(file)
# #     print(rows)
# #     for row in rows:
# #         print(row)
#
# # Dictionary reader
# with open(path) as file:
#     records = []
#     rows = csv.DictReader(file)
#     # print(rows)
#     for row in rows:
#         records.append(row)
#
#
# def read_csv():
#     with open(path) as file:
#         records = []
#         rows = csv.DictReader(file)
#         # print(rows)
#         for row in rows:
#             records.append(row)
#     return records
#
#
# # print(records)
#
# data = read_csv()
# #  I want to calculate the total pay that I am paying to employees
#
# # total_salary = 0.0
#
#
# # def total_salary(data):
# #     total = 0.00
# #     for item in data:
# #         total = total + float(item['pay'])
# #     return total
#
# # print(total_salary(data))
#
# #  how many male and female employees are there
#
# # by_gender = {"male": 6, "female": 4}
#
#
# # def get_emp_by_gender(data):
# #     from collections import defaultdict
# #     by_gender = defaultdict(int)
# #     for item in data:
# #         g = item['gender']
# #         by_gender[g] += 1
# #     return by_gender
#
#
# # print(get_emp_by_gender(data))
#
#
# # sort the employees based on the name, and pay
#
# # by_name = sorted(data, key=lambda item: item['name'])
# # by_pay = sorted(data, key=lambda item: item['pay'])
# #
# # for item in by_pay:
# #     print(item)
#
# # Unique teams in the file
#
# # teams = set(item['team'] for item in data)
# # print(teams)
#
#
# #  employees taking more than 5000 rs salary
#
# # more_5k = [item for item in data if float(item['pay']) > 90000]
# # for item in more_5k:
# #     print(item)
#



# import csv
#
# path = r"C:\Users\harishbabumg\PycharmProjects\pythonProject\files_directory\csv_files\vaccination_data.csv"
#
#
# def read_vacci():
#     with open(path) as file:
#         records = []
#         rows = csv.DictReader(file)
#         print(rows)
#         for row in rows:
#             temp = {"COUNTRY": row['WHO_REGION'], "DATE_UPDATED": row["DATE_UPDATED"], "vaccines": row["TOTAL_VACCINATIONS"]}
#             records.append(row)
#     return records
#
#
# data1 = read_vacci()
#
# total = 0
# for item in data1:
#     total += item["TOTAL_VACCINATIONS"]
#
# print(total)
import csv

def read_csv():
    with open(path) as file:
        records = []
        rows = csv.reader(file)
        # print(rows)
        for row in rows:
            records.append(row)
    return records
#

print(read_csv())