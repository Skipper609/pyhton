
lower = int(input("Enter the lower Bound : "))
upper = int(input("Enter the upper Bound : "))

for i in range(lower, upper + 1):
    if i % 9 == 0 and i % 5 != 0:
        print(i, end = ' ')
