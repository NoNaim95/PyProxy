#!/usr/bin/python3
import binascii
import struct
from pyproxy import Proxy
from pyproxy.packethandler import PacketHandler
from pyproxy.packet import Packet

class MyPacket(Packet):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.packetcount = struct.unpack_from("!H",self.data,6)[0]


    @classmethod
    def Packetoverload(cls, packet):
        return cls(packet.data,packet.srcaddr,packet.dstaddr)

class MyPacketHandler(PacketHandler):
    spinb = False
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def injectPacket(self,packet):
        self.proxy.sendPacket(packet)

    def hook(self,packet):
        if packet.srcaddr == self.proxy.client: # if the hooked packed was sent by the client
            if b"secret" in packet.data:
                packet = MyPacket.Packetoverload(packet)
                print("spotted secret in this packet:\n",binascii.hexlify(packet.data))
            if b"badword" in packet.data:
                return b"" # not letting that packet through (discarding it)
        return packet


proxy = Proxy("192.168.0.204",28763,4444)
proxy.route(packethandler=MyPacketHandler(proxy))

