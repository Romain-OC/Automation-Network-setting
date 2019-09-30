class Main :

#INTERFACE
	interfaces = new Interface()
	dhcp = new DHCP()
	parefeu= new FireWall()
	address = raw_input("Entrez la première address")
	interfaces.address.append(address)
	continue = raw_input("Entrer une autre addresse ? o pour oui, n pour non")
	While continue!= 'n' & continue != 'o' : 
			continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	While continue!='n':
		address = raw_input("Entrez l'addresse suivante")
		interfaces.address.append(address)
		continue = raw_input("Entrer une autre addresse ? o pour oui, n pour non")
		While continue!= 'n' & continue != 'o' : 
			continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	renameInterface(interfaces.listMac[])
	configInterface(interfaces.listMac[],interfaces.address[])

#DHCP
	continue = raw_input("Voulez vous configurez un dhcp ? o pour oui, n pour non")
	While continue!= 'n' & continue != 'o' : 
				continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	if continue = o :
		dhcp.subnet= raw_input("sur quelle réseau doit etre le dhcp ?")
		temp = raw_input("quelle est la première addresse de la range ? ")
		dhcp.range.append(temp)
		temp = raw_input("quelle est la dernière addresse de la range ? ")
		dhcp.range.append(temp)
		Self.gateway= raw_input("quelle est la passerelle ?")
	configDHCP(dhcp.subnet,dhcp.range,dhcp.gateway)
	
#PAREFEU
	continue = raw_input("Voulez vous configurez un parefeu ? o pour oui, n pour non")
	While continue!= 'n' & continue != 'o' : 
				continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	if continue = o :
		parefeu.interface = interfaces.address
		initFichier(parefeu.interface[])
		standardConfig()
		continue = raw_input("Voulez vous ouvrir certain port ? o pour oui, n pour non")
		While continue!= 'n' & continue != 'o' : 
				continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
		if continue = o :
		temp= raw_input("quel est le port à ouvrir ? ")
		parefeu.openPort.append(temp)
		temp= raw_input("quel est le protocol du port entré ? ")
		parefeu.protocol.append(temp)
		continue = raw_input("Ouvrir un autre Port ? o pour oui, n pour non")
		While continue!= 'n' & continue != 'o' : 
				continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
		While continue!='n':
			temp= raw_input("quel est le port à ouvrir ? ")
		parefeu.openPort.append(temp)
		temp= raw_input("quel est le protocol du port entré ? ")
		parefeu.protocol.append(temp)
		continue = raw_input("Ouvrir un autre Port ? o pour oui, n pour non")
		While continue!= 'n' & continue != 'o' : 
				continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
		Openport(parefeu.openPort[],parefeu.protocol[])
		endConfig()