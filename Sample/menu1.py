
lst = []

def add(ele):
    lst.append(ele)

def pop():
    if len(lst) > 0:
        ele = lst.pop()
        print(f"{ele} is removed")
    else:
        print("List is empty")

def search(ele):
    if ele in lst:
        print(f"Element {ele} found at {lst.index(ele)}")
    else:
        print("Element is not in list")

def display():
    if len(lst) == 0:
        print("List is empty")
    else:
        for i in lst:
            print(i,end = " ")
        print()

while True:
    print("1>Add  2>Delete  3>Search  4>Display  5>Exit")
    ch = int(input("Enter the choice :"))
    if ch == 1:
        num = int(input("Enter the element to add"))
        add(num)
    elif ch == 2:
        pop()
    elif ch == 3:
        num = int(input("Enter the element to be searched :"))
        search(num)
    elif ch == 4:
        display()
    else:
        break