Class Interfaces :

import subprocess

Def _init_(self) :


Self.nom = "eth"
Self.address = 0.0.0.0
Self.macAddress = subprocess.check_output('ip a |grep ether |cut -d' ' -f6', shell = True) 
Self.listMac = Self.macAddresss.split('\n')

def __getNom__(self, nom):

def __getAddress__(self, address):

def __setNom__(self, nom,val_nom):

def __setAddress__(self, address,val_address):

def renameInterface():

	mon_fichier = open("/etc/udev/rules.d/70-persistent-net.rules", "a")
	i = 0
	while i<(len(listMac)-1):
		mon_fichier.write("SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*",ATTR{address}=="+self.listMac(i)+",ATTR{dev_id}=="0x0", ATTR{type}=="1",KERNEL=="eth*", NAME=""eth"+i+"\n")
		i+=1
	mon_fichier.close()