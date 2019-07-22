'''4.	Write a program to accept a number n from the user; then display the sum of the following series:
1/23 + 1/33 + 1/43 + …… + 1/n3
'''

def find_one_by_ncube(num):
    res = 0

    for i in range(2, num+1):
        res += 1/(i**3)
    
    return res

num = int(input("Enter a number :"))
res = find_one_by_ncube(num)
print("The result is ",res)
