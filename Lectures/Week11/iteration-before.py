# Manually iterate through a iteratable object

# [Dictionary, Tuple, or Dictionary] of file permissions
permissions = ("read", "modify", "write")

#Iterator Object
myit = iter(permissions)
print(type(myit))

# Iterate
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

