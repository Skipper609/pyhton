'''Program to check if a given number is prime or not'''

def is_prime(n):
    '''This will return true if N prime'''
    if n < 2:
        return False
    for i in range(2, n// 2 + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Enter the value of N :"))
count = 0
num = 2
while count < N:
    if is_prime(num):
        print(num,end = ' ')
        count +=1
    num +=1
