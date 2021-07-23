from pyproxy.packet import Packet

class PacketHandler():
    def __init__(self,proxy):
        self.proxy = proxy

    def injectPacket(self,packet):
        self.proxy.sendPacket(packet)

    def hook(self,packet):
        return packet
