import xlrd
f_path = r"C:\Users\haris\OneDrive\Desktop\Book1.xlsx"
xl_obj = xlrd.open_workbook(f_path)
xl_sheet = xl_obj.sheet_by_name("project_status")
data = xl_sheet.get_rows()
header = next(data)

def ticket(data):
    for item in data:
        yield ("tt.amazon.com/"+f"{item[4].value}")
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
print(next(ticket(data)))
