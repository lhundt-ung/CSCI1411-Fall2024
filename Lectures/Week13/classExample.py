from Endpoint import Endpoint

# Create objects
desktop1 = Endpoint("MyPC","192.168.1.101")
desktop2 = Endpoint("MomsLaptop","192.168.1.102")
fridge = Endpoint("Samsung","192.168.1.103")

#What will happen when you just print fridge?
print(fridge)


# Store objects in List, print the list. Also try set and Dict
# Notice anything Strange
homeNetwork = [desktop1,desktop2,fridge]
print(homeNetwork)
homeNetworkSet = (desktop1,desktop2,fridge)
print(homeNetworkSet)
homeNetworkDict = {"desktop1":desktop1,"desktop2":desktop2,"fridge":fridge}
print(homeNetworkDict)


#How would one add open ports (ports_open) to the second object stored in homeNetwork list? port numbers 
# 25,80
homeNetwork = [desktop1,desktop2,fridge]
print(homeNetwork[1].ports_open)
homeNetwork[1].ports_open = [25,80]
print(homeNetwork[1].ports_open)




#Iterate through homeNetwork list assign property os to "Windows 11"
homeNetwork = [desktop1,desktop2,fridge]
for device in homeNetwork:
    device.os = "Windows 11"
    print(device.name, ":", device.os)





#Iterate through homeNetwork and print endpoint's name, os, and ports open
# Example --> Name: MomsPC, Ports Open: [80,443] 
homeNetwork = [desktop1,desktop2,fridge]
for device in homeNetwork:
    print(device.name, "-", device.os, ":", device.ports_open)


