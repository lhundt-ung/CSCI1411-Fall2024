import firewall as fw
import packet as p
import random

# Initialize Firewall object with some global variables
myFirewall = fw.Firewall("myFirewall")
commonPorts = ["25","80","443","3389","22"]
allowed = 0
blocked = 0

#Generate 100 random Firewall Rules
for i in range(0,100):
    src = "192.168.2." + str(random.randrange(1,10))
    dst = "192.168.1." + str(random.randrange(1,10))
    port = random.choices(commonPorts)
    block = random.randrange(0,2)
    if block == 0:
        block = "Allow"
    else:
        block = "Block"
    
    myFirewall.addRule(src,dst,port[0],block)

#print(myFirewall.rules)


# Simulate 10000 Network traffic packets sent through Firewall
numberOfPackets = 10000
for i in range(0,numberOfPackets):
    src = "192.168.2." + str(random.randrange(1,10))
    dst = "192.168.1." + str(random.randrange(1,10))
    port = random.choices(commonPorts)
    pkt = p.Packet(src,dst,port[0])
    result = myFirewall.inspectPacket(pkt)
    if result == "Allow":
        allowed+=1
    else:
        blocked+=1

print("Total Allowed: ",allowed)
print("Total Blocked: ",blocked)

