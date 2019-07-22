'''program to check given number is palindrome or not'''

num = input("Enter the Number")
rev = num[::-1]
if num == rev:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
num = int(num)
temp = num
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp = temp // 10
if num == rev:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
