
try:
    with open("text.txt") as f:
        data = f.readlines()
        for line in data:
            print(line)
except Exception as e:
    print(e)

