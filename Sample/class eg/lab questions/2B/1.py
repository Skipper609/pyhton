
def biggest(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    return num2 if num2 > num3 else num3  

def biggest2(num1, num2, num3):
    return num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 else num3
a, b, c = input("Enter 3 numbers :").split()
big = biggest2(int(a), int(b), int(c))
print(f"Biggest of {a} , {b} , {c} is {big}")
