'''1. Write a program to accept a number and determine whether it is prime or not'''

import math

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(num))):
            if num % i ==0:
                return False
        return True
