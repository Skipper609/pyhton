
income = float(input("Enter the salary :"))

amount = 0
if income < 500000:
    amount = 0
elif income > 500000:
    if income > 1000000:
        amount = 500000*.1 + (income - 1000000)*.3
    else:
        amount = (income-500000)*.1
print(f"Income tax for {income} is {amount}")
