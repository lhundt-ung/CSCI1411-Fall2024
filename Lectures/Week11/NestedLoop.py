import time

portList = [21,22,25,80,110]

#Nested Loops
for x in range(1,255):
    time.sleep(.2)
    print("===============================")
    for port in portList:
        print("[+] Checking 192.168.1." + str(x),":",port)