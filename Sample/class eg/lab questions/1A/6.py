from functools import reduce

inp_str = input("Enter a string : ")
vou = ['a', 'e', 'i', 'o', 'u' ]
res = reduce(lambda a,b : a + b, list(filter(lambda a: a.lower() not in vou, inp_str)))
print(f"Resultant string is {res}")

# res1 = ''
# for i in inp_str:
#     if i.lower not in vou:
#         res1 += i
# res1 = inp_str.replace
# print()