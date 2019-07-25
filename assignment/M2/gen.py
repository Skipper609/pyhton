

for i in range(9):
    x = 12 + i 
    if x % 4 == 0 :
        x = x // 4
        if x >= i:
            print(f"{x} {i} {x-i} {x+x-i}")
