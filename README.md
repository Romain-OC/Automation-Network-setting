# Automation-Network-setting
# _Documentation utilisateur :_

Supported OS (Debian 9,Ubuntu,CentOS)

Requierement : Distro module for python3

Ce projet à pour but d’automatiser les tâches de configuration des interfaces réseaux ainsi que la mise en place d’un pare-feu à l’aide d’iptables.

This project is made to automise network interface, dhcp and firewalls (iptables) configuration tasks

## Interfaces configuration :

Au lancement le programme va renommer les interfaces réseaux avec l’ancienne appellation « ethx »
Il vous sera demandé de rentrer les adresses IP voulu pour les interfaces dans l’ordre eth0, eth1 etc...
Ensuite les fichiers de configuration (/etc/network/interfaces, /etc/netplan/01-netcfg.yaml, /etc/sysconfig/network-scripts/ifcfg-eth) seront générés automatiquement en fonction de votre système d’exploitation avec les adresses IP données 

At launch the script will rename all network interfaces with their previous designation "ethx"
You will have to type the IP address wanted for your interfaces from eth0 to ethx
Then configuration files (/etc/network/interfaces, /etc/netplan/01-netcfg.yaml, /etc/sysconfig/network-scripts/ifcfg-eth) will be generated according to the current OS and IP address typed 

## DHCP configuration:

Il vous sera ensuite demandé si vous voulez configurer un DHCP.

Vous aurez à rentrer 4 informations :
* Le réseau sur lequel le DHCP va donner des adresses 
* La première adresse de la plage
* La dernière adresse de la plage
* La passerelle

Next you will be able to chose wether you want to configure a DHCP or not.

4 informations will be requested :
* The network on wich the dhcp will listen 
* The first address of the range
* last address of the range 
* The gateway
 
## Firewall configuration :

Enfin il vous sera demandé si vous voulez configurer un pare-feu.
Vous pourrez choisir quels port vous voulez ouvrir

Finally you will be able to configure a firewall.
You can choose wich port you want open
