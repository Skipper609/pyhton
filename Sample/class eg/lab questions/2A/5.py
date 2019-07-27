num = int(input("Enter the number:"))

for i in range(1,num+1):
    res = ""
    for j in range(num - i):
        res += "-"
    res += str(int("1"*i) ** 2)
    for j in range(num - i):
        res += "-"
    print(res)
