Cricket = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton = [ "PKM", "ALN", "NV", "KM","RMV"]

lst = []
lst.extend(Cricket)

for i in Football:
    if i not in lst:
        lst.append(i)
for i in Badminton:
    if i not in lst:
        lst.append(i)

print(lst)