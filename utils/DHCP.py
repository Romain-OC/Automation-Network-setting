#!/usr/bin/env python3
import shutil
import fileinput

class DHCP:

    def __init__(self):

        self.subnet = ""
        self.drange = list()
        self.gateway = ""

    def configDHCP(self,subnet,drange,gateway):
        mon_fichier = shutil.copy("utils/dhcpd.conf", "/etc/dhcp/")
        filename = '/etc/dhcp/dhcpd.conf'

        temp = {
                '#option routers ;':'option routers '+gateway+' ;',
                '#subnet 1 netmask 255.255.255.0 {':'subnet '+self.subnet+' netmask 255.255.255.0 {',
                '  #range 1;':'\trange '+self.drange[0]+' '+self.drange[1]+';'
                }
        for line in fileinput.input(filename,inplace = True):
            line = line.rstrip('\r\n')
            print(temp.get(line,line))
