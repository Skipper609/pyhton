
name = input("Enter the word :")

lst = ['a','e','i','o','u']

val = list(filter(lambda x: x in lst,name))
print(val,len(val))