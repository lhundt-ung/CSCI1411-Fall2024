
class Packet(object):

    def __init__(self,src,dst,port):
        """Return a Packet object with the following attributes"""
        self.src= src
        self.dst = dst
        self.port = port
        self.data = None