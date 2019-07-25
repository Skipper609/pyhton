from functools import reduce

#name = input("Enter your name :")

#lst = ['a','e','i','o','u']

#print(len(list(filter(lambda x: x in lst,name))))
#names = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
#print(list(filter(lambda x: x.startswith("A"), map(lambda i: i.capitalize(),names))))

#lst = [1,2,3,4,5,6,7,8,9,10]
#res = reduce(lambda a,b : a+b,lst)
#print(res)

num = [ i**2 for i in range(1,11)]
print(reduce(lambda a,b: a+b,filter(lambda a : a % 2 == 0,num)))
