''''''
inp_num = input("Enter a number :")
res = ""
for i in inp_num:
    res += str((int(i) + 1) % 10)
print(f"The resultent for the input {inp_num} is {res}")

