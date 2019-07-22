'''2.	Write a program to accept a number n from the user; then display the sum of the following series:
                            1 + 1/2 + 1/3 + ……. + 1/n
'''

def find_one_by_n(num):
    res = 0

    for i in range(1,num+1):
        res += 1/i
    
    return res

num = int(input("Enter a number :"))
res = find_one_by_n(num)
print("The result is ",res)
