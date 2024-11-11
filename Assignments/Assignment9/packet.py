
class Packet(object):
    """A simple object to simulate network packets 

    Attributes:
        src: A string representing the source address
        dst: A string representing the destination address
        port: A string representing the port number
        data: An open data type to store data contained in the packet
    """

    def __init__(self,src,dst,port):
        """Return a packet object with the following attributes"""
        self.src= src
        self.dst = dst
        self.port = port
        self.data = None


