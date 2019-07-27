prime = [ 2, 3, 5, 7]

num = input("Enter the number:")

res = len(list(filter(lambda a : int(a) in prime, num )))
print(f"The no.of Prime digit in {num} is :{res}")
res = 0

# for i in num:
#     if int(i) in prime:
#         res += 1
# print(f"The no.of Prime digit in {num} is :{res}")
