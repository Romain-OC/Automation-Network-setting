#!/usr/bin/env python3
import shutil
class DHCP:

	def _init_(self):

		self.subnet = "" 
		self.range = []
		self.gateway = ""

	#def __getSubnet__(self, subnet):
		#return None

	#def __getRange__(self, range,id):
		#return self._range[id]

	#def __getGateway__(self, gateway):
		#return self._gateway

	#def __setSubnet__(self, subnet,val_subnet):
		#self._subnet=val_subnet
	
 	#def __setRange__(self, range,val_range):
		
	#def __setGateway__(self, gateway,val_gateway):

	def configDHCP(self,Subnet,range,gateway) :
		shutil.copy('dhcpd.conf', '/etc/dhcp/')
		mon_fichier = open(":etc/dhcp/dhcpd.conf","a")
		
		chaine = "#option routers ;"
		
		if chaine in ligne :

					ligne = "option routers "+gateway+" ;"
					mon_fichier.write(ligne)
		
		chaine = "#subnet 1 ;"
		
		if chaine in ligne :

					ligne = "subnet "+self.subnet+" netmask 255.255.255.0 {"
					mon_fichier.write(ligne)

		chaine = "#range 1;"
		
		if chaine in ligne :

					ligne = "range "+self.range[0]+" "+self.range[1]+";"
					mon_fichier.write(ligne)
		mon_fichier.close()