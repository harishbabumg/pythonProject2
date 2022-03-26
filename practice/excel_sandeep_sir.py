import xlrd
path = r"C:\Users\haris\OneDrive\Desktop"
workbook = xlrd.open_workbook(path)
worksheet = workbook.sheet_by_name("loginpage")
rows = worksheet.get_rows()
headers = next(rows)

#