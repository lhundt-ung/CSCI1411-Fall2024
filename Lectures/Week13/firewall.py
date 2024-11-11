import packet

class Firewall(object):
    """A simple firewall object. Firewalls have the
    following properties:

    Attributes:
        name: A string representing the firewall name
        rules: A list containing inbound firewall rules
    """

    def __init__(self, name):
        """Return a firewall object with the following attributes"""
        self.name = name
        self.rules = []

    def addRule(self,src,dst,port,action):
        id = self.getLastRuleID()
        rule = {"id":id,"src":src,"dst":dst,"port":port,"action":action}
        self.rules.append(rule)

    def getLastRuleID(self):
        if self.rules:
            id = self.rules[-1]["id"] + 1
        else:
            id = 0
        return id
    
    def inspectPacket(self,packet):
        action = self.findRuleMatch(packet)
        #print(action)
        if action == "Block":
            print(packet.src, "to", packet.dst,"is blocked")
            return "Block"    
        elif action == "Allow":
            print(packet.src, "to", packet.dst,"is allowed")
            return "Allow"
        else:
            print(packet.src, "to", packet.dst,"is allowed due to no rule")
            return "Allow"

    def findRuleMatch(self,packet):
        #print("Packet",type(packet.src),type(packet.dst),type(str(packet.port)))
        for rule in self.rules:
            #print("Rule",type(rule["src"]),type(rule["dst"]),type(rule["port"]))
            if packet.src == rule["src"] and packet.dst == rule["dst"] and str(packet.port) == rule["port"]:
                return rule["action"]
            else:
                continue
               
    


