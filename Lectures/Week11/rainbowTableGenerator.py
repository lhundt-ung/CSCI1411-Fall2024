import string
import crypt

# Create Rainbow Table Example
# 1. Print all combinations from aaa-zzz
# 2a. Store in a dictionary object as hash:password combo --> {'wVJUqimh646':'aaa'}
# 2b. How many combinations should expect to see? 
lowercaseLetters = string.ascii_lowercase
salt = "HX"
hashDict = {}

#print(lowercaseLetters[0])

for a in range(0,26):
    #print(lowercaseLetters[a])
    for b in range(0,26):
        #print(lowercaseLetters[a] + lowercaseLetters[b])
        for c in range(0,26):
            #print(lowercaseLetters[a] + lowercaseLetters[b] + lowercaseLetters[c])
            pw = lowercaseLetters[a] + lowercaseLetters[b] + lowercaseLetters[c]
            hash = crypt.crypt(pw,salt)
            hashDict[hash] = pw

print(len(hashDict))
print(hashDict)

# 3. Iterate through dictionary object and write keys and values to a rainbow file
#Example rainbox.txt:
# aaa,t9W1HQLMasY
# aab,mgIUVcfWzGo 
# ...

#Your code here
file = open('rainbow.txt','w')

for pw,value in hashDict.items():
    file.writelines(pw + "," + value + "\n")

file.close()




# 4. How many combinations would we have for two letter salts?
#17,576

# 5. What would the rainbow file size be?
#300KB

# 6. What would the rainbow file size be 
# using lowercase and Uppercase combinations?
#52^3 = 140,608
#2,400KB


