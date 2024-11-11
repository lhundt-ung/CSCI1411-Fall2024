import random

#Random number between 1-9
print(random.randrange(1,10))

#Grab a random value out a list
commonPorts = ["25","80","443","3389","22"]
print(random.choices(commonPorts))