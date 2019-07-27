
class Stack:

    def __init__(self):
        self.st = []
    
    def push(self, ele):
        self.st.append(ele)
    def pop(self):
        if not self.is_empty():
            ele = self.st.pop()
            print(f"The popped element is {ele}")
        else:
            print("Stack is empty")
    def search(self, ele):
        if not self.is_empty():
            for index,val in enumerate(self.st):
                if val == ele:
                    return index
            else:
                return -1
    def show(self):
        if not self.is_empty():
            for i in self.st:
                print(i)
        else:
            print("Stack is empty")
    def is_empty(self):
        return True if len(self.st) == 0 else False

if __name__ == "__main__":
    sta = Stack()
    while True:
        print("1>Push   2>Pop   3>Search   4>Display   5>Exit")
        try:
            ch = int(input("Enter your choice :"))
            if ch == 1:
                ele = input("Enter the element to be pushed : ")
                sta.push(ele)
            elif ch == 2:
                sta.pop()
            elif ch == 3:
                ele = input("Enter the element to be searched :")
                index = sta.search(ele)
                if index != -1:
                    print(f"Element {ele} is present in the index {index}")
                else:
                    print(f"Element {ele} is not present in the Stack")
            elif ch == 4:
                sta.show()
            elif ch == 5:
                exit()
            else:
                raise ValueError
        except (ValueError, KeyError):
            print("Enter the options within 1 to 5")

    