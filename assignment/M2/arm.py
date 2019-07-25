
def amstrong(num):
    num_1 = num
    res = 0
    while num != 0:
        r = num % 10
        res = res + r ** 3
        num = num // 3

    return num_1 == res

inp = int(input("Enter a number :"))
if amstrong(inp):
    print(f"{inp} is an amstrong number")
else:
    print(f"{inp} is not an amstrong number")

#x y x-y x+x-y