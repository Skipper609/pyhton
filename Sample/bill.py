unit = int(input("Enter the No. of Units :"))

if unit < 500:
    rate = 6
elif unit <1000:
    rate = 8
else:
    rate = 12
amount = unit * rate
if amount < 50:
    print("Bill amount is 50")
else:
    print("Bill amount is ",amount)
