lst = ['Story', 'Emergency', 'Qualify', 'Lie']

for word in lst:
    if word.endswith("y"):
        w = word[:-1] + 'ies'
    else:
        w = word + "s"
    print(f"{word} - {w}")