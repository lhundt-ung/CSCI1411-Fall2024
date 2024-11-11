import packet

class Firewall(object):
    """A simple firewall object. Firewalls have the
    following properties:

    Attributes:
        name: A string representing the firewall name
        rules: A list containing inbound firewall rules
        totalPacketsAllowed: A counter for packets allowed
        totalPacketsBlocked: A counter for packets blocked
        verbose: Prints all allowed traffic
    """

    def __init__(self, name):
        """Return a firewall object with the following attributes"""
        self.name = name
        self.rules = []
        self.totalPacketsBlocked = 0
        self.totalPacketsAllowed = 0
        self.verbose = False

    # addRule method for adding new rules to the firewall
    # Example: myFirewall.addRule("192.168.1.100","192.168.1.101","25","Block")
    def addRule(self,src,dst,port,action):
        id = self.getLastRuleID()
        rule = {"id":id,"src":src,"dst":dst,"port":port,"action":action}
        self.rules.append(rule)

    def resetPacketCount(self):
        self.totalPacketsAllowed = 0
        self.totalPacketsBlocked = 0

    # getLastRuleID method used to generate unique id for each new rule
    def getLastRuleID(self):
        if self.rules:
            id = self.rules[-1]["id"] + 1
        else:
            id = 0
        return id
    
    # inspectPacket method inspects packet and compares to the current 
    # firewall rules list and prints out the action taken
    def inspectPacket(self,netPacket):
        action = self.findRuleMatch(netPacket)

        if action == "Block":
            if self.verbose == True:
                print("-",netPacket.src, "to", netPacket.dst,"using port",netPacket.port,"is blocked")  
            self.totalPacketsBlocked = self.totalPacketsBlocked + 1      
        elif action == "Allow":
            if self.verbose == True:
                print("+",netPacket.src, "to", netPacket.dst,"using port",netPacket.port,"is allowed.")
            self.totalPacketsAllowed = self.totalPacketsAllowed + 1
        else:
            if self.verbose == True:
                print("+",netPacket.src, "to", netPacket.dst,"using port",netPacket.port,"is allowed due to no rule.")
            self.totalPacketsAllowed = self.totalPacketsAllowed + 1

    # Called upon in inspectPacket method to perform the rule matching task
    # Below is where you can add your code to account for wildcard rules
    def findRuleMatch(self,netPacket):
        for rule in self.rules:
            if netPacket.src == rule["src"] and netPacket.dst == rule["dst"] and netPacket.port == rule["port"]:
                return rule["action"]
            #Your CODE HERE
   
            else:
                continue
               
    


