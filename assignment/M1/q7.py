'''7.	Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number.'''

num = input("Enter a number :")
intnum = int(num)

while intnum //10 > 0 :
    res = 0
    for i in num:
        res += int(i)
    num = str(res)
    intnum = res
print(f"The number is {intnum}")