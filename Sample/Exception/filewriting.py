try:
    with open("text.txt") as fin, open("U_data.txt",'w') as fout:
        lines = fin.readlines()
        lines = [l.upper() for l in lines]
        fout.writelines(lines)
except Exception as e:
    print(f"File not found {e}")