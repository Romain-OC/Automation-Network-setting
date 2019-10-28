#!/usr/bin/env python3
from utils.DHCP import *
from utils.FireWall import *
from utils.Interface import *

class Main :

#INTERFACE
    interfaces = Interface()
    address = input("Entrez la première address \n")
    interfaces.address.append(address)
    cont = input("Entrer une autre addresse ? o pour oui, n pour non \n")
    while ( not(cont == 'n') and not(cont == 'o')):
        cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
        while not (cont == 'n'):
            address = input("Entrez l'addresse suivante \n")
        interfaces.address.append(address)
        cont = input("Entrer une autre addresse ? o pour oui, n pour non \n")
        while (not (cont == 'n') and not (cont == 'o')) :
            cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
    interfaces.renameInterface(interfaces.listMac)
    interfaces.configInterface(interfaces.listMac,interfaces.address)
#DHCP
    dhcp = DHCP()
    cont = input("Voulez vous configurez un dhcp ? o pour oui, n pour non \n")
    while (not ( cont == 'n') and not (cont == 'o')) :
        cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
        if cont =='o':
            dhcp.subnet= input("sur quelle réseau doit etre le dhcp ? \n")
            temp = input("quelle est la première addresse de la range ? \n")
            dhcp.drange.append(temp)
            temp = input("quelle est la dernière addresse de la range ? \n")
            dhcp.drange.append(temp)
            dhcp.gateway= input("quelle est la passerelle ? \n")
            dhcp.configDHCP(dhcp.subnet,dhcp.drange,dhcp.gateway)
	
#PAREFEU

    parefeu = FireWall(interfaces.address)
    cont = input("Voulez vous configurez un parefeu ? o pour oui, n pour non \n")
    while (not (cont == 'n') and not (cont == 'o')) : 
        cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
    if cont == 'o' :
        parefeu.interface = interfaces.address
        parefeu.initFichier(parefeu.interface)
        parefeu.standardConfig()
        cont = input("Voulez vous ouvrir certain port ? o pour oui, n pour non \n")
        while (not (cont == 'n') and (cont == 'o')) : 
            cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
        while cont == 'o' :
            temp = input("quel est le port à ouvrir ? \n")
            parefeu.openPort.append(temp)
            temp= input("quel est le protocol du port entré ? \n")
            parefeu.protocol.append(temp)
            cont = input("Ouvrir un autre Port ? o pour oui, n pour non \n")
            while (not (cont == 'n') and not (cont == 'o')) : 
                cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non \n")
            while not (cont =='n'):
                temp= input("quel est le port à ouvrir ? \n")
                parefeu.openPort.append(temp)
                temp= input("quel est le protocol du port entré ? \n")
                parefeu.protocol.append(temp)
                cont = input("Ouvrir un autre Port ? o pour oui, n pour non \n")
    parefeu.OpenPort(parefeu.openPort,parefeu.protocol)
    parefeu.endConfig()
    subprocess.run('reboot',shell=True)