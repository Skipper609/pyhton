import openpyxl
wb = openpyxl.load_workbook("Result.xlsx")
sheet = wb.active
grade = {'S+': 10, 'S':9,'A':8,'B':7,'C':6,'D':5,'E':4,'F':0}
a = [7,8,12,13]
for row in sheet.iter_rows(min_row= 3,min_col=2,max_col=13):
    if row:
        data = [c.value for c in row]
        stu_p_info = data[:2]
        subs = [data[5:7],data[-2:]]
        ci_into_gi = sum(map(lambda x: x[0]*grade[x[1]],subs))
        ci = sum(map(lambda x: x[0],subs))
        si = ci_into_gi / ci
        print(stu_p_info,si)