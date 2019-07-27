from functools import reduce

'''factorial of a number'''
num = int(input("Enter a number :"))

fact = reduce(lambda a,b: a*b,[i for i in range(1,num+1)])

print(f"The factorial of {num} is {fact}")
