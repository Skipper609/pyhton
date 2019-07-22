'''To find series of factorial of numbers'''

def factorial(N):
    fact = 1
    if N > 0:
        for i in range(2, N+1):
            fact *= i
    return fact

N = int(input("Enter a number to find its factorial :"))
num = 0
for i in range(1, N+1):
    num += 1 / factorial(i)
print(f"{num} is the answer")
