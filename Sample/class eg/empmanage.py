from emp import Employee

#emp_1 = Employee(1, "Rajesh", "M.Tech", 56000, "CS")
#emp_2 = Employee(2, "Sujesh", "M.Tech", 46000, "IS")

lst_emp = []

def load_emp():
    with open("empdetails.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            data = data.strip("\n").split(",")
            empno = int(data[0])
            empname = data[1]
            emp_q = data[2]
            emp_sal = int(data[3])
            emp_dept = data[4]
            emp = Employee(empno, empname, emp_q, emp_sal, emp_dept)
            lst_emp.append(emp)
    print(f"The no.of Employees is {len(lst_emp)}")

def showDeptName():
    dpt_name = set(map(lambda x: x.dept_name, lst_emp))
    for name in dpt_name:
        print(name)

def showAllQualifications():
    print("All qualifications are:")
    qual = set(map(lambda x: x.qualification, lst_emp))
    for qu in qual:
        print(qu)

def maxSalary():
    ma = max(list(map(lambda x:x.salary,lst_emp)))

    peeps = list(filter(lambda x : x.salary == ma, lst_emp))
    for name in peeps:
        name.show_info()

def showEmpCountByDeptName():
    dept = dict()
    for guy in lst_emp:
        if guy.dept_name in dept:
            dept[guy.dept_name] += 1
        else:
            dept[guy.dept_name] = 1
    for i in dept:
        print(f"{i} - {dept[i]}")

def showTotalsalBydeptName():
    dept = dict()
    for guy in lst_emp:
        if guy.dept_name in dept:
            dept[guy.dept_name] += guy.salary
        else:
            dept[guy.dept_name] = guy.salary
    for i in dept:
        print(f"{i} - {dept[i]}")

def showEmpCountByQual():
    qual = dict()
    for guy in lst_emp:
        if guy.qualification in qual:
            qual[guy.qualification] += 1
        else:
            qual[guy.qualification] = 1
    for i in qual:
        print(f"{i} - {qual[i]}")

load_emp()
#showDeptName()
#showAllQualifications()
#maxSalary()
#showEmpCountByDeptName()
#showTotalsalBydeptName()
showEmpCountByQual()
