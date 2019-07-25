'''
gen 100 random nums 1-1000
get only divisible by 3,6 but not 9
'''

import random as rn

num = []

for i in range(100):
    num.append(rn.randint(1,1000))

for number in num:
    if num % 6 == 0 and num % 9 != 0:
        print(number)