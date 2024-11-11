from Endpoint import Endpoint

class Server(Endpoint):
    
    def __init__(self, name, ip):
        """Return a Server object with the following attributes"""
        Endpoint.__init__(self, name, ip)
        self.service = "Unknown"

    # What's wrong?
    def printServer(self):
        print("Name:",self.name)
        print("+ IP:",self.ip)
        print("+ Services:",self.service)
        print("+ Ports Open:",self.ports_open)

    
def printListItems(listWServerObjs):
    for server in listWServerObjs:
        server.printServer()


##### TESTING #####

#Implement 3 objects of Server type
server1 = Server("DC1","10.0.0.55")
server1.service = "Domain Controller"
server1.ports_open = [53,389,636]

server2 = Server("FS15","10.0.0.56")
server2.service = "File Server"
server2.ports_open = [445]

server3 = Server("MEDIA1","10.0.0.57")
server3.service = "Media Server"
server3.ports_open = [445]

#Use new Function
server1.printServer()

# Object Type
print(type(server1))

# List Example
L1 = [server1,server2,server3]
printListItems(L1)


#L2 = ["server1","server2","server3"]
#printListItems(L2)



