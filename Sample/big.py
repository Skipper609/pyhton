num1 = int(input("Enter Num1 :"))
num2 = int(input("Enter Num2 :"))
num3 = int(input("Enter Num3 :"))

if num1 > num2 and num1 > num3:
    big = num1
elif num2 > num3:
    big = num2
else:
    big = num3
print(f"Biggest of {num1},{num2},{num3} is {big}")
