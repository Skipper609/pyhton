'''3.	Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers. '''

import math

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0 :
            return False
    return True

num1 = int(input("Enter the number A : "))
num2 = int(input("Enter the number B : "))

for i in range(num1, num2 + 1):
    if is_prime(i):
        print(i,end = " ")
