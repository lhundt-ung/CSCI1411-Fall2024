line = "victim: HX9LLTdc/jiDE: 503:100:Iama Victim:/home/victim:/bin/sh"

print(line.split(":"))
splitList = line.split(":")
pw = splitList[1].strip()
print(pw)

salt = pw[0:2]
hashedPW = pw[2:]

print(salt,hashedPW)


