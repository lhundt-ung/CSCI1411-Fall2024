file = open("access.log", "r")

nasaList = []

for line in file:
    if "nasa" in line:
        print(line)
        nasaList.append(line)

file.close()

print (nasaList)
print(len(nasaList))


