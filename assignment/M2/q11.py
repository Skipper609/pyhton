Cricket = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton = [ "PKM", "ALN", "NV", "KM","RMV"]

plays_all = list(filter(lambda x: x in Football and x in Badminton,Cricket))
plays_one = list(filter(lambda x: x not in Football and x not in Badminton,Cricket))
plays_one.extend(list(filter(lambda x: x not in Cricket and x not in Badminton,Football)))
plays_one.extend(list(filter(lambda x: x not in Football and x not in Cricket,Badminton)))

print(f"The people who play all the three games are {plays_all}")
print(f"The people who play only one of the three games are {plays_one}")


