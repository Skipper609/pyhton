'''summing till it becomes 1 digit number'''

num = int(input("Enter a number  :"))
numc = num
while num // 10 > 0:
    num = (num % 10) + (num //10)
print(f"The sum of digits of {numc} is {num}")
