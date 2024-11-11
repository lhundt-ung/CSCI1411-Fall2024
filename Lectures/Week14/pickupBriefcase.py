# Execute on pickup machine
# python3 pickupBriefcase.py sensitiveData.txt 10.0.2.15
import sys
from scapy.all import *

#conf.verb mutes scapys verbosity
conf.verb = 0

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
        message =str(p['Raw'].load.decode("utf-8"))
        print(message)

        #Stop sniffing packets once hidden message is found
        if 'Handoff' in str(message):
            f.write(message)
            f.close()
            print("Secret Message transmission complete!")
            keepGoing = False
        else:
            # Write data to text file as it comes in
            f.write(message)
            print("Data Received")