from functools import reduce

num = [ i**2 for i in range(1,10)]
print(reduce(lambda a,b: a+b,filter(lambda a : a % 2 == 0,num)))