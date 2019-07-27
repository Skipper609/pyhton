'''To print all the prime numbers between the upper bound and lower bound'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
lower = int(input("Enter the lower bound :"))
upper = int(input("Enter the upper bound :"))
for i in list(filter(is_prime,[j for j in range(lower, upper + 1)])):
    print(i, end = " ,")
