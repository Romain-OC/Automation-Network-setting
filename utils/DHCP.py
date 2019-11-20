#!/usr/bin/env python3
import shutil
import fileinput

class DHCP:

    def __init__(self):

        self.subnet = ""
        self.drange = list()
        self.gateway = ""
        self.nbdhcp = 0

    #replace the comment in the dhcp file by the requested value 
    def configDHCP(self,subnet,drange,gateway):
        filename = '/etc/dhcp/dhcpd.conf'
        tempoption = {
                '#subnet '+str(self.nbdhcp)+' netmask 255.255.255.0 {':'subnet '+self.subnet+' netmask 255.255.255.0 {',
                '  #option routers '+str(self.nbdhcp)+'' : '\toption routers '+self.gateway+ ';',
                '  #range '+str(self.nbdhcp)+';':'\trange '+self.drange[self.nbdhcp]+' '+self.drange[self.nbdhcp+1]+';'
                }
        for line in fileinput.input(filename,inplace = True):
            line = line.rstrip('\r\n')
            print(tempoption.get(line,line))
        del tempoption
        self.nbdhcp = self.nbdhcp + 2
