#!/usr/bin/env python3
from utils.DHCP import *
from utils.FireWall import *
from utils.Interface import *
import subprocess
import re

class Main :

    interfaces = Interface()
    #downloading necessary package
    if interfaces.ostype.nomdist[0]=='centos':
        subprocess.run('yum -y install dhcp-server',shell=True)
        subprocess.run('yum install iptables-services -y', shell = True)
    else:
        subprocess.run('apt-get install isc-dhcp-server -y',shell=True)
        subprocess.run('echo iptables-persistent iptables-persistent/autosave_v4 boolean true | sudo debconf-set-selections',shell = True)
        subprocess.run('echo iptables-persistent iptables-persistent/autosave_v6 boolean true | sudo debconf-set-selections',shell = True)
        subprocess.run('apt-get install iptables-persistent -y',shell = True)

#INTERFACE
    #request the address and netsmak for the first interface
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    naddress = input("Entrez la première address \n")
    while not(re.search(regex, naddress)):
        naddress = input("Entrez une addresse valide \n")
    interfaces.address.append(naddress)
    if interfaces.ostype.nomdist[0]=='ubuntu':
        netmask = input("Entrez le masque de sous réseau au format CIDR (ex: 24) \n")
        interfaces.netmask.append(netmask)
    else:
        netmask = input("Entrez le masque de sous réseau \n")
        interfaces.netmask.append(netmask)
    cont = input("Entrer une autre addresse ? o pour oui, n pour non \n")
    #if 'o' request address for other interfaces if 'n' skip
    while ( not(cont == 'n') and not(cont == 'o')):
        cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
    while cont == 'o':
        naddress = input("Entrez l'addresse suivante \n")
        while not(re.search(regex, naddress)):
            naddress = input("Entrez une addresse valide \n")
        interfaces.address.append(naddress)
        if interfaces.ostype.nomdist[0]=='ubuntu':
            netmask = input("Entrez le masque de sous réseau au format CIDR (ex: 24) \n")
            interfaces.netmask.append(netmask)
        else:
            netmask = input("Entrez le masque de sous réseau \n")
            interfaces.netmask.append(netmask)
        cont = input("Entrer une autre addresse ? o pour oui, n pour non \n")
        while (not (cont == 'n') and not (cont == 'o')) :
            cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
    interfaces.renameInterface(interfaces.listMac)
    interfaces.configInterface(interfaces.listMac,interfaces.address)
#DHCP
    #if 'o' starts the dhcp configuration if 'n' skip
    cont = input("Voulez vous configurez un serveur dhcp ?(max 3) o pour oui, n pour non \n")
    while (not ( cont == 'n') and not (cont == 'o')) :
        cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
    i=0
    if cont =='o':
        dhcp = DHCP()
        shutil.copy("utils/dhcpd.conf", "/etc/dhcp/")
    while cont =='o' and i<3:
        #request options for the dhcp
        dhcp.subnet= input("sur quelle réseau doit etre le dhcp ? \n")
        dhcp.netmask= input("quel est le masque du réseau ? \n")
        address = input("quelle est la première addresse de la range ? \n")
        dhcp.drange.append(address)
        address = input("quelle est la dernière addresse de la range ? \n")
        dhcp.drange.append(address)
        dhcp.gateway= input("quelle est la passerelle ? \n")
        dhcp.configDHCP(dhcp.subnet,dhcp.drange,dhcp.gateway)
        cont = input("Voulez vous configurez un autre serveur dhcp ? o pour oui, n pour non \n")
        while (not ( cont == 'n') and not (cont == 'o')) :
            cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
        i+=1
	
#PAREFEU
    #if 'o' starts the firewall configuration if 'n' skip
    cont = input("Voulez vous configurez un parefeu ? o pour oui, n pour non \n")
    while (not (cont == 'n') and not (cont == 'o')) : 
        cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
    if cont == 'o' :
        parefeu = FireWall(interfaces.nom)
        parefeu.interface = interfaces.address
        parefeu.initFichier(parefeu.interface)
        parefeu.standardConfig()
        #if 'o' request for port to open if 'n' skip
        cont = input("Voulez vous ouvrir certain port ? o pour oui, n pour non \n")
        while (not (cont == 'n') and not (cont == 'o')) : 
            cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
        while cont == 'o' :
            #request wich port to open
            port = input("quel est le port à ouvrir ? \n")
            parefeu.openPort.append(port)
            protocol= input("quel est le protocol du port entré ? \n")
            parefeu.protocol.append(protocol)
            cont = input("Ouvrir un autre Port ? o pour oui, n pour non \n")
            while (not (cont == 'n') and not (cont == 'o')) : 
                cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
    parefeu.OpenPort(parefeu.openPort,parefeu.protocol)
    parefeu.endConfig()
    parefeu.launchFirewall()
    #reboot the system
    cont = input("Le système va redémarrer veuillez appuyer sur entrée pour continuer \n")
    subprocess.run('reboot',shell=True)