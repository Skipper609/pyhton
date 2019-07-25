
for i in range(9):
    four_x = 12 + i
    if four_x % 4 == 0:
        x = four_x // 4
        if x >= i:
            print(f"{x}{i}{x-i}{x+x-i}")