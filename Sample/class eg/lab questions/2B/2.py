
def find_sum(lst):
    return sum(lst)

inp = [int(i) for i in input("Enter the series of numbers seperated by spaces :").split()]
sm = find_sum(inp)
print(f"The sum for the list {inp} is {sm}")