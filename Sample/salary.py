salary = int(input("Enter salary :"))

if salary<0:
    salary = -salary
salary+= salary*.1

print("New Salary is ",salary)
