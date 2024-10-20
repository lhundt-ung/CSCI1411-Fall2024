#Conditional Examples

#No conditional
a = 2
a = a + 1
print(a)


#What's the value of a?
a = 2
if a == 2:
    a = a + 1
print(a)


a = 2
if a == 0:
    a = a + 1
a = a + 1
print(a)


a = 2
if a == 2:
    a = a + 1
if a == 2:
    a = a + 2
a = a + 1
print(a)
