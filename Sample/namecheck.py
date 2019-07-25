
data = "Ahah,rajesh,suresh,armesh,amaresh,jayesh"

names = data.upper().split(",")

namelist = []
for name in names:
    if name.startswith("A") and name.endswith("H"):
        namelist.append(name)
namelist.sort()
print(namelist)