#Set Syntax and Properties
#Notice anything interesting?
setExample = {'Monday','Tuesday','Wednesday','Monday','Monday'}
L1 = ['Monday','Tuesday','Wednesday','Monday','Monday']

print(L1)
print(setExample)
#print(setExample[0])

#Add object to set
setExample.add("Saturday")
print(setExample)

#Add duplicate object to set
#Will we see two Mondays, one Monday or Error?
setExample.add("Monday")
print(setExample)

#Remove object
setExample.remove("Monday")
print(setExample)
