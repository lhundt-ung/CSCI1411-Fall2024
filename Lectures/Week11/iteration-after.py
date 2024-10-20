# Automatically iterate through a iteratable object
# tuple of file permissions
permissions=("read","modify","write")

print("Number of loops:", len(permissions))

#Variable to track number of loops
x = 0

for permission in permissions:
    x += 1 #Same as x = x + 1, x++ not allowed in python
    print("Loop:",x, "- Permission:", permission)


