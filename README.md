## Automation-Network-setting
# _Documentation utilisateur :_

Supported OS (Debian 9,Ubuntu,CentOS)

Requirement : distro module for python3

# Français :

Ce projet à pour but d’automatiser les tâches de configuration des interfaces réseaux ainsi que la mise en place d’un pare-feu à l’aide d’iptables.

## Configuration des Interfaces :

Au lancement le programme va renommer les interfaces réseaux avec l’ancienne appellation « ethx »
Il vous sera demandé de rentrer les adresses IP voulu pour les interfaces dans l’ordre eth0, eth1 etc...
Ensuite les fichiers de configuration (/etc/network/interfaces, /etc/netplan/01-netcfg.yaml, /etc/sysconfig/network-scripts/ifcfg-eth) seront générés automatiquement en fonction de votre système d’exploitation avec les adresses IP données 

## Configurationdu DHCP:

Il vous sera ensuite demandé si vous voulez configurer un DHCP.

Vous aurez à rentrer 4 informations :
* Le réseau sur lequel le DHCP va donner des adresses 
* La première adresse de la plage
* La dernière adresse de la plage
* La passerelle
 
## Configuration du Pare-feu :

Enfin il vous sera demandé si vous voulez configurer un pare-feu.
Vous pourrez choisir quels port vous voulez ouvrir

# English :

The purpose of this project is to automate network interfaces configuration tasks and the installation of a firewall using iptables.

## Configuration interfaces :

At launch the program will rename the network interfaces with the old name "ethx".
You will be asked to enter the IP addresses required for the interfaces in the order eth0, eth1 etc....
Then the configuration files (/etc/network/interfaces, /etc/netplan/01-netcfg.yaml, /etc/sysconfig/network-scripts/ifcfg-eth) will be automatically generated according to your operating system with the IP addresses 

## DHCP configuration:

You will then be asked if you want to configure a DHCP.

You will have to enter 4 information:
* The network on which the DHCP will give addresses 
* The first address of the range
* The last address of the range
* The gateway
 
## Firewall configuration :

Finally, you will be asked if you want to configure a firewall.
You will be able to choose which ports you want to open
