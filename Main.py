#!/usr/bin/env python3
from utils.DHCP import *
from utils.FireWall import *
from utils.Interface import *

class Main :

#INTERFACE
	interfaces = Interface()
	dhcp = DHCP()
	parefeu = FireWall(interfaces.address)
	address = input("Entrez la première address")
	interfaces.address.append(address)
	cont = input("Entrer une autre addresse ? o pour oui, n pour non")
	while ( not(cont == 'n') and not(cont == 'o')):
		cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	while cont !='n':
		address = input("Entrez l'addresse suivante")
		interfaces.address.append(address)
		cont = input("Entrer une autre addresse ? o pour oui, n pour non")
		while cont!= 'n' & cont != 'o' : 
			cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	interfaces.renameInterface(interfaces.listMac)
	interfaces.configInterface(interfaces.listMac,interfaces.address)

#DHCP
	cont = input("Voulez vous configurez un dhcp ? o pour oui, n pour non")
	while cont != 'n' & cont != 'o' : 
		cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	if cont =='o' :
		dhcp.subnet= input("sur quelle réseau doit etre le dhcp ?")
		temp = input("quelle est la première addresse de la range ? ")
		dhcp.range.append(temp)
		temp = input("quelle est la dernière addresse de la range ? ")
		dhcp.range.append(temp)
		dhcp.gateway= input("quelle est la passerelle ?")
	dhcp.configDHCP(dhcp.subnet,dhcp.range,dhcp.gateway)
	
#PAREFEU
	cont = input("Voulez vous configurez un parefeu ? o pour oui, n pour non")
	while cont!= 'n' & cont != 'o' : 
		cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	if cont == 'o' :
		parefeu.interface = interfaces.address
		parefeu.initFichier(parefeu.interface)
		parefeu.standardConfig()
		cont = input("Voulez vous ouvrir certain port ? o pour oui, n pour non")
		while cont!= 'n' & cont != 'o' : 
			cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non")
		if cont == 'o' :
			temp = input("quel est le port à ouvrir ? ")
		parefeu.openPort.append(temp)
		temp= input("quel est le protocol du port entré ? ")
		parefeu.protocol.append(temp)
		cont = input("Ouvrir un autre Port ? o pour oui, n pour non")
		while cont!= 'n' & cont != 'o' : 
			cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non")
		while cont!='n':
			temp= input("quel est le port à ouvrir ? ")
		parefeu.openPort.append(temp)
		temp= input("quel est le protocol du port entré ? ")
		parefeu.protocol.append(temp)
		cont = input("Ouvrir un autre Port ? o pour oui, n pour non")
		while cont!= 'n' & cont != 'o' : 
			cont = input("veuiller entrer une valeur correcte. o pour oui, n pour non")
		parefeu.OpenPort(parefeu.openPort,parefeu.protocol)
		parefeu.endConfig()