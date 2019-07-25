name = ['PKM','ALN','PVR',"PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
count = dict()

for i in name:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count) 