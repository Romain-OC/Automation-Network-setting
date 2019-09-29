
Class Main :
	interfaces = new Interface()
	dhcp = new DHCP()
	address = raw_input("Entrez la première address")
	interfaces.address.append(address)
	continue = raw_input("Entrer une autre addresse ? o pour oui, n pour non")
	While continue!='n':
		address = raw_input("Entrez l'addresse suivante")
		interfaces.address.append(address)
		continue = raw_input("Entrer une autre addresse ? o pour oui, n pour non")
		While continue!= 'n' & continue != 'o' : 
			continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
interfaces.renameInterface()
interfaces.configInterface()

	continue = raw_input("Voulez vous configurez un dhcp ? o pour oui, n pour non")
	While continue!= 'n' & continue != 'o' : 
				continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
	if continue = o :
		dhcp.subnet= raw_input("sur quelle réseau doit etre le dhcp ?")
		temp = raw_input("quelle est la première addresse de la plage ? ")
		dhcp.range.append(temp)
		temp = raw_input("quelle est la dernière addresse de la plage ? ")
		dhcp.range.append(temp)
		Self.gateway= raw_input("quelle est la passerelle ?")
