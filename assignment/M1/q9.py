'''9.	Write a program to accept a five-digit number, increment each digit by 1 and then display the new number formed. Note that digit 9 gets incremented to 0.'''

num = input("Enter the number :")

res = ""
for i in num:
    res += str((int(i)+1)%10)

print(res)