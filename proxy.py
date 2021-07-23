#!/usr/bin/python3
import socket
import packet
import packethandler


class Proxy():
    def __init__(self,remoteHost,remotePort,localport):
        self.localport = localport
        self.remoteHost = remoteHost
        self.remotePort = remotePort
        self.server = (remoteHost,remotePort)
        self.client = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("binding Proxy to Port: "+str(localport))
        self.socket.bind(("",localport))

    def sendPacket(self,packet):
        if packet:
            self.socket.sendto(packet.data,packet.dstaddr)

    def route(self,Packet=packet.Packet,packethandler=packethandler.PacketHandler):
        while True:
                packet = Packet(*self.socket.recvfrom(32768))
                if self.client is None or packet.srcaddr != self.server:
                    self.client = packet.srcaddr


                packet.dstaddr = self.server if packet.srcaddr==self.client else self.client


                if packethandler:
                    packet = packethandler.hook(packet)

                self.sendPacket(packet)
