'''10.	Write a program to print the following output pattern.
     1
    121
   12321
  1234321
 123454321
'''

n = 5

for i in range(1,n+1):

    res = ''
    for j in range(n-i):
        res += ' '
    for k in range(1,i+1):
        res += str(k)
    for k in range(i-1,0,-1):
        res += str(k)
    print(res)