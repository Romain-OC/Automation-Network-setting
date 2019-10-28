#!/usr/bin/env python3
import fileinput
import shutil
import subprocess
from utils.DetectOS import *


class Interface:

    def __init__(self):

        self.nom = "eth"
        self.address = list()
        self.macAddress = subprocess.run('ip a |grep ether |cut -d\' \' -f6', shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        self.mac = self.macAddress.stdout
        self.listMac = self.mac.decode().split("\n")
        self.chemin = ""
        self.ostype = DetectOS()
   
    #def __getNom__(self, nom):
   
    #def __getAddress__(self, address, int id):
        #return Self._address[id]

    #def __setNom__(self, nom,val_nom):

    #def __setAddress__(self, address,val_address):

    def pathfile(self,n):
        switcher = {
            'debian':"/etc/network/interfaces",
            'ubuntu':"/etc/netplan/01-netcfg.yaml",
            'centos':"/etc/sysconfig/network-scripts/"
        }
        return switcher.get(n,"la méthode ne détecte pas l'OS" ) 

    def renameInterface(self,listMac):

        mon_fichier = open("/etc/udev/rules.d/70-persistent-net.rules", "a")
        i = 0
        while i<(len(listMac)-1):
            mon_fichier.write("SUBSYSTEM==\"net\", ACTION==\"add\", DRIVERS==\"?*\",ATTR{address}==\""+self.listMac[i]+"\",ATTR{dev_id}==\"0x0\", ATTR{type}==\"1\",KERNEL==\"eth*\", NAME=\"eth"+str(i)+"\" \n")
            self.address.append("eth"+str(i))
            i+=1
        mon_fichier.close()
        temp = {
                'GRUB_CMDLINE_LINUX=\"\"':'GRUB_CMDLINE_LINUX=\"net.ifnames=0 biosdevname=0\"'
            }
        for line in fileinput.input('/etc/default/grub',inplace=True):
            line = line.rstrip('\r\n')
            print(temp.get(line,line))
        subprocess.run('grub-mkconfig -o /boot/grub/grub.cfg',shell=True)


    def configInterface(self,listMac,address):
        self.chemin= self.pathfile(self.ostype.nomdist[0])
        if self.chemin == '/etc/network/interfaces':
            mon_fichier = shutil.copy('utils/interfaces','/etc/network/')
            i=0
            while i<(len(listMac)-1):
                #filename = '/etc/network/interfaces'
                temp = {
                        "#allow-hotplug eth"+str(i): "allow-hotplug eth"+str(i),
                        "#iface eth"+str(i)+" inet dhcp": "iface eth"+str(i)+" inet static",
                        "\t#address eth"+str(i): "\taddress "+self.address[i],
                        "\t#netmask eth"+str(i): "\tnetmask 255.255.255.0"
                        }
                for line in fileinput.input('/etc/network/interfaces',inplace=True):
                    line = line.rstrip('\r\n')
                    print(temp.get(line, line))
                i+=1
        elif self.chemin == "/etc/netplan/01-netcfg.yaml":
            shutil.copy('utils/01-netcfg.yaml', '/etc/netplan/')
            mon_fichier = open(self.chemin,"r+")
            i=0
            while i<(len(listMac)-1):
                chaine = "#enp1s0f0:"
            
                # on boucle sur les lignes du fichier1 original
                for ligne in mon_fichier :

                    if chaine in ligne :

                        ligne = "eth"+str(i)+":"
                        mon_fichier.write(ligne)
            
                chaine = "#dhcp4: yes"

                for ligne in mon_fichier :

                    if chaine in ligne :

                        ligne = "dhcp4: yes"
                        mon_fichier.write(ligne)

                chaine = "#addresses: []"

                for ligne in mon_fichier :

                    if chaine in ligne :

                        ligne = "#addresses: ["+self.address[i]+"/24]"
                        mon_fichier.write(ligne)
            mon_fichier.close()
        elif self.chemin == "/etc/sysconfig/network-scripts/":
            i=0
            while i<(len(listMac)-1):
                shutil.copy('ifcfg-eth', '/etc/sysconfig/network-scripts/ifcfg-eth'+str(i))
                mon_fichier = open('/etc/sysconfig/network-scripts/ifcfg-eth'+i,"r+")
                chaine = "#DEVICE=eth0"
                for ligne in mon_fichier :
                    if chaine in ligne :
                        ligne = "DEVICE=eth"+str(i)
                        mon_fichier.write(ligne)
                chaine = "#ONBOOT=yes"
                for ligne in mon_fichier :
                    if chaine in ligne :
                        ligne = "ONBOOT=yes"
                        mon_fichier.write(ligne)
                chaine = "#NAME=lan"
                for ligne in mon_fichier :
                    if chaine in ligne :
                        ligne = "NAME=lan"+str(i)
                        mon_fichier.write(ligne)
                chaine = "#MAC"
                for ligne in mon_fichier :
                    if chaine in ligne :
                        ligne = "MAC="+self.listMac[i]
                        mon_fichier.write(ligne)
            mon_fichier.close()
