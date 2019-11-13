#!/usr/bin/env python3
import shutil
import fileinput

class DHCP:

    def __init__(self):

        self.subnet = ""
        self.drange = list()
        self.gateway = ""

    #replace the comment in the dhcp file by the requested value 
    def configDHCP(self,subnet,drange,gateway):
        mon_fichier = shutil.copy("utils/dhcpd.conf", "/etc/dhcp/")
        filename = '/etc/dhcp/dhcpd.conf'
        i = 0
        while i<(len(drange)/2):
            temp = {
                    '#subnet '+str(i)+' netmask 255.255.255.0 {':'subnet '+self.subnet+' netmask 255.255.255.0 {',
                    '  #option routers '+str(i)+'' : 'option gateway '+self.gateway+ ';',
                    '  #range '+str(i)+';':'\trange '+self.drange[i]+' '+self.drange[i+1]+';'
                    }
            for line in fileinput.input(filename,inplace = True):
                line = line.rstrip('\r\n')
                print(temp.get(line,line))
            i+=2
