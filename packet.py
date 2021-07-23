class Packet():
    def __init__(self,data,srcaddr=None,dstaddr=None):
        self.srcaddr = srcaddr
        self.dstaddr = dstaddr
        self.data = data
