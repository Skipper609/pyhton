def searchLiniar(lst ,ele):
    for index,val in enumerate(lst):
        if ele == val :
            return index
    return -1

def bubblesort(lst):
    for i in range(len(lst)-1,0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1], lst[j]

def binarysearch(lst, key):
    l = 0
    h = len(lst)-1
    while l <= h:
        mid = (l + h)//2
        if lst[mid] == key:
            return mid
        elif key > lst[mid]:
            l = mid + 1
        else:
            h = mid - 1
    return -1
ele = 2
l = [1,2,3,4,5]

res = binarysearch(l, ele)
if res == -1:
    print(f"{ele} is not found")
else:
    print(f"{ele} is found at index:{res}")

