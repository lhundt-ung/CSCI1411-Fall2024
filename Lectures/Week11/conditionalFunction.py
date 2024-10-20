allowedPorts = [25,80,443]

def firewall(firewall_state):
    if firewall_state == True:
        print("Go on in")
    else:
        print("Access Denied: Cannot enter")

def traffic(port):
    allowed = False
    for portNumber in allowedPorts:
        if portNumber == port:
            allowed = True    
    return allowed

firewall(traffic(30))
firewall(traffic(25))
firewall(traffic(443))    

