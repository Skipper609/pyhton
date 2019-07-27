
with open("que.txt") as f:
    questions = f.readlines()
    for que in questions:
        que = que.strip("\n")
        if "?" in que:
            print(f"The statement -< {que} >- is intorrogative")
        else:
            print(f"The statement -< {que} >- is assertive")