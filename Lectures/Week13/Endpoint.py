
class Endpoint(object):
    """An endpoint is any device connected to a network. Endpoints have the
    following properties:

    Attributes:
        name: A string representing the endpoint name
        status: A boolean representing if the endpoint is up or down
        ip: A string representing the endpoint IP Address
        os: A string representing the endpoint operating system
        ports_open: A list of TCP ports open
    """

    def __init__(self, name, ip):
        """Return an endpoint object with the following attributes"""
        self.name = name
        self.status = False
        self.ip = ip
        self.os = "Unknown"
        self.ports_open = []

    def get_status(self):
        """Return the current status of endpoint """
        #< Code to check if endpoint is up>
        print(self.status)
        return self.status

    def set_status(self,status):
        """Return the current status of endpoint """
        #< Code to check if endpoint is up>
        if True == True:
            self.status = True
        else:
            self.status = False
        return self.status
    
 
    # Changes the way the object is printed instead of memory location
    def __str__(self):
        return "Endpoint:"+self.name
  
    # Changes the way the object is printed in a list or dictionary
    def __repr__(self):
        return "Endpoint:"+self.name
  

    def check_ports_open(self):
        """Find open ports and return the ports that are open"""
        #< Code to check what ports are open>
        #self.ports_open = [22,80,443]
        if self.ports_open:
            print(self.ports_open)
            return self.ports_open
        else:
            print("No Ports were found open")
            return self.ports_open


'''
#### TESTING AREA ####
# Initialize an object
pc1 = Endpoint("myPC", "192.168.1.101")
print(type(pc1))


print(pc1.name,"-", pc1.ip)
pc1.get_status()
'''
