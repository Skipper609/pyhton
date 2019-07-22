'''6. write a program to take a number as a input and display its reverse'''

def reverse_num(num):
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    
    return rev

num = int(input("Enter the number :"))
print("The reverse is ",num)