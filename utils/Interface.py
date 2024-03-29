﻿#!/usr/bin/env python3
import fileinput
import shutil
import subprocess
from utils.DetectOS import *


class Interface:

    def __init__(self):

        self.nom = list()
        self.address = list()
        self.netmask = list()
        self.gateway = ""
        self.macAddress = subprocess.run('ip a |grep ether |cut -d\' \' -f6', shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        self.mac = self.macAddress.stdout
        self.listMac = self.mac.decode().split("\n")
        self.chemin = ""
        self.ostype = DetectOS()
    #define the path of the interface configuration file considering the OS
    def pathfile(self,n):
        switcher = {
            'debian':"/etc/network/interfaces",
            'ubuntu':"/etc/netplan/01-netcfg.yaml",
            'centos':"/etc/sysconfig/network-scripts/"
        }
        return switcher.get(n,"la méthode ne détecte pas l'OS" ) 
    #rename interfaces with their previous designation "ethx"
    def renameInterface(self,listMac):
        mon_fichier = open("/etc/udev/rules.d/70-persistent-net.rules", "a")
        i = 0
        while i<(len(listMac)-1):
            mon_fichier.write("SUBSYSTEM==\"net\", ACTION==\"add\", DRIVERS==\"?*\",ATTR{address}==\""+self.listMac[i]+"\",ATTR{dev_id}==\"0x0\", ATTR{type}==\"1\",KERNEL==\"eth*\", NAME=\"eth"+str(i)+"\" \n")
            self.nom.append("eth"+str(i))
            i+=1
        mon_fichier.close()
        if self.ostype.nomdist[0]=='debian' or self.ostype.nomdist[0]=='ubuntu':
            temp = {
                    'GRUB_CMDLINE_LINUX=\"\"':'GRUB_CMDLINE_LINUX=\"net.ifnames=0 biosdevname=0\"'
                }
            for line in fileinput.input('/etc/default/grub',inplace=True):
                line = line.rstrip('\r\n')
                print(temp.get(line,line))
            subprocess.run('grub-mkconfig -o /boot/grub/grub.cfg',shell=True)
        if self.ostype.nomdist[0]=='centos':
            temp = {
                    'GRUB_CMDLINE_LINUX=\"crashkernel=auto resume=/dev/mapper/cl-swap rd.lvm.lv=cl/root rd.lvm.lv=cl/swap rhgb quiet\"':'GRUB_CMDLINE_LINUX=\"crashkernel=auto resume=/dev/mapper/cl-swap rd.lvm.lv=cl/root rd.lvm.lv=cl/swap net.ifnames=0 rhgb quiet\"'
                }
            for line in fileinput.input('/etc/default/grub',inplace=True):
                line = line.rstrip('\r\n')
                print(temp.get(line,line))
            subprocess.run('grub2-mkconfig -o /boot/grub2/grub2.cfg',shell=True)
    #set up the interfaces configuration files depending on the OS
    def configInterface(self,listMac,address):
        self.chemin= self.pathfile(self.ostype.nomdist[0])
        #Debian
        if self.chemin == '/etc/network/interfaces':
            shutil.copy('utils/interfaces','/etc/network/')
            i=0
            while i<(len(self.address)):
                temp = {
                        "#allow-hotplug eth"+str(i): "allow-hotplug eth"+str(i),
                        "#iface eth"+str(i)+" inet dhcp": "iface eth"+str(i)+" inet static",
                        "\t#address eth"+str(i): "\taddress "+self.address[i],
                        "\t#netmask eth"+str(i): "\tnetmask "+self.netmask[i],
                        "\t#gateway eth"+str(i): "\tgateway "+self.gateway
                        }
                for line in fileinput.input('/etc/network/interfaces',inplace=True):
                    line = line.rstrip('\r\n')
                    print(temp.get(line, line))
                i+=1
        #Ubuntu
        elif self.chemin == "/etc/netplan/01-netcfg.yaml":
            shutil.copy('utils/01-netcfg.yaml', '/etc/netplan/')
            i=0
            while i<(len(self.address)):
                temp = {
                        "        #eth"+str(i)+":": "        eth"+str(i)+":",
                        "            #addresses:[]"+str(i): "            addresses: ["+self.address[i]+"/"+self.netmask[i]+"]",
                        "            #gateway:"+str(i):"            gateway: "+self.gateway
                        }
                for line in fileinput.input('/etc/netplan/01-netcfg.yaml',inplace=True):
                    line = line.rstrip('\r\n')
                    print(temp.get(line, line))
                i+=1
            subprocess.run('netplan apply',shell = True)
        #CentOS
        elif self.chemin == "/etc/sysconfig/network-scripts/":
            i=0
            while i<(len(self.address)):
                shutil.copy('utils/ifcfg-eth0', '/etc/sysconfig/network-scripts/ifcfg-eth'+str(i))
                temp = {
                        "#DEVICE=eth0": "DEVICE=eth"+str(i),
                        "#ONBOOT=yes": "ONBOOT=yes",
                        "#NAME=lan": "NAME=lan"+str(i),
                        "#MAC":"MAC="+self.listMac[i],
                        "#BOOTPROTO=none":"BOOTPROTO=none",
                        "#NETMASK=":"NETMASK="+self.netmask[i],
                        "#IPADDR=":"IPADDR="+self.address[i],
                        "#GATEWAY=":"GATEWAY="+self.gateway
                        }
                for line in fileinput.input('/etc/sysconfig/network-scripts/ifcfg-eth'+str(i),inplace=True):
                    line = line.rstrip('\r\n')
                    print(temp.get(line, line))
                i+=1
