import xlrd

f_path = r"C:\Users\haris\OneDrive\Desktop\Book1.xlsx"

# opening the workbook
xl_obj = xlrd.open_workbook(f_path)

# opening the spreadsheet and getting its handle
xl_sheet = xl_obj.sheet_by_name("Marks_sheet")

# getting all the rows in the sheet as generator object
data = xl_sheet.get_rows()

# traversing through each row
# for row in data:
#     print(row)

data = xl_sheet.get_rows()

# traversing through each row and getting
for row in data:
    print(row[0].value, row[1].value)
