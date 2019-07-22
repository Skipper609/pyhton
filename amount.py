
amount = int(input("Enter the amount: "))

if amount > 10000:
    discount = amount*.2
else:
    discount = amount*.05
net = amount - discount

print(f"Amount: {amount},Discount: {discount},New Amount: {net} ")
