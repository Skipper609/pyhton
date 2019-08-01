import csv
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
try:
    with open("db.csv") as file:
        data = csv.reader(file)
        for d in data:
            sheet.append(d)
        wb.save("Student.xlsx")
except Exception as e:
    print(e)
    