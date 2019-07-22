'''8.	Write a program to accept 2 numbers “m” and “n” from the user; determine the value of mn without using predefined functions.'''

m = int(input("Enter the value of M :"))
n = int(input("Enter the value of N :"))

res = 1
for i in range(n):
    res *= m
print(f"The resultant is {res}")
