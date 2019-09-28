
Class Main :
	interfaces = new Interface()
	address = raw_input("Entrez la première address")
	interfaces.address.append(address)
	While continue!='n':
		address = raw_input("Entrez l'addresse suivante")
		interfaces.address.append(address)
		continue = raw_input("Entrer une autre addresse ? o pour oui, n pour non")
			While continue!= 'n' & continue != 'o' : 
				continue = raw_input("veuiller entrer une valeur correcte. o pour oui, n pour non")
interfaces.renameInterface()
interfaces.configInterface()

