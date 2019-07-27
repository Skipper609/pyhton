''' write a program to find simple interest'''

principle = float(input("Enter the principle :"))
rate = float(input("Enter the rate of interest (p.a):"))/100
duration = float(input("Enter the duration :"))

interest = principle * rate * duration

print(f"The simple interest is {interest}")