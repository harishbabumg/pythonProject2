import xlrd

f_path = r"C:\Users\haris\OneDrive\Desktop\objects.xlsx"
# open excel

book = xlrd.open_workbook(f_path)

# opening sheet
sheet = book.sheet_by_name("Sheet1")


data = sheet.get_rows()

# skip the header
header = next(data)

# get each row

login_page = {}
for row in data:
    login_page[row[0].value] = (row[1].value, row[2].value)

print(login_page)
