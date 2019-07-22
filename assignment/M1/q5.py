'''5.	Write a program to print the Fibonacci series up to the number 34. '''

num1 = 0
num2 = 1
print(num1,end = ' ')
print(num2,end = ' ')

while num1 < 34 :
    num1, num2 = num1 + num2 , num1
    print(num1 , end = ' ')
