'''To Find the factorial of a number'''

N = int(input("Enter a number to find its factorial :"))
fact = 1
if N > 0:
    for i in range(2, N+1):
        fact *= i
    print(f"Factorial of {N} is {fact}")
else:
    print(f"Factorial of {N} doesnt exist")
