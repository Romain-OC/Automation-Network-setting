Class DHCP :

Def _init_(self) :

	Self.subnet = "" 
	Self.range = liste()
	Self.gateway = ""

def __getSubnet__(self, subnet):

def __getRange__(self, range):

def __getGateway__(self, gateway):

def __setSubnet__(self, subnet,val_subnet):

def __setRange__(self, range,val_range):

def __setGateway__(self, gateway,val_gateway):

def configDHCP(Subnet,range,gateway) :
	filePath = shutil.copy('dhcpd.conf', '/etc/dhcp/')
	mon_fichier = open(":etc/dhcp/dhcpd.conf","a")
	
	chaine = "#option routers ;"
	
	if chaine in ligne :

                ligne = "option routers "+gateway+" ;"
                 mon_fichier.write(ligne)
	
	chaine = "#subnet 1 ;"
	
	if chaine in ligne :

                ligne = "subnet "+Self.subnet+" netmask 255.255.255.0 {"
                 mon_fichier.write(ligne)

	chaine = "#range 1;"
	
	if chaine in ligne :

                ligne = "range "+Self.range[0]+" "+Self.range[1]+";"
                 mon_fichier.write(ligne)
	mon_fichier.close()