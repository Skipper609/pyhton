'''generate 20 random numbers in range 1-50 and put it in the list
find max,min
put them in another list and print them
'''
import random as rn

num = []
for i in range(20):
    num.append(rn.randint(50))

min_max=[min(num),max(num)]
print(num)
print(min_max)