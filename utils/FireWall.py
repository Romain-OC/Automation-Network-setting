#!/usr/bin/env python3
import fileinput
import subprocess
from utils.DetectOS import *
class FireWall:

	def __init__(self,listInterface):
		self.interface = listInterface
		self.openPort=list()
		self.protocol=list()
		self.ostype = DetectOS()
	#write in the firewall script the first part of the scipt
	def initFichier(self,interface):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		firewall.write("#!/bin/bash\n")
		firewall.write("IPT=/sbin/iptables\n")
		firewall.write("WAN=eth0\n")
		if len(self.interface)>1:
			i=1
			while i<(len(self.interface)-1):
				firewall.write("LAN=eth"+str(i)+"\n")
		firewall.write("firewall_start(){\n \n")
		firewall.close()
	#write in the firewall script the standard rules of the firewall
	def standardConfig(self):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		firewall.write("$IPT -A INPUT -i $WAN -m state --state ESTABLISHED,RELATED -j ACCEPT \n")
		firewall.write("$IPT -A INPUT -i lo -j ACCEPT \n")
		firewall.write("$IPT -P INPUT DROP \n")
		firewall.write("$IPT -P FORWARD DROP\n")
	#write the rules to open port requested by the user
	def OpenPort(self,openPort,protocol):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		i = 0
		print(len(protocol))
		while i<(len(protocol)):
			firewall.write("$IPT -A INPUT -p "+protocol[i]+" -i $WAN --dport "+openPort[i]+" -j ACCEPT \n")
			i+=1
		firewall.close
	#write the end of the script
	def endConfig(self):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		firewall.write("} \n \n")	
		firewall.write("firewall_stop(){ \n$IPT -F \n$IPT -t nat -F \n$IPT -P INPUT ACCEPT \n$IPT -P FORWARD ACCEPT \n} \n")
		firewall.write("firewall_restart(){ \nfirewall_stop \nsleep 2 \nfirewall_start \n}\n")
		firewall.write("case $1 in \n\t\t'start') \n\t\t\tfirewall_start \n\t\t\t;; \n\t\t'stop') \n\t\t\tfirewall_stop \n\t\t\t;; \n\t\t'restart') \n\t\t\tfirewall_restart \n\t\t\t;; \n*) \n\t\t\techo usage: -bash {start|stop|restart} \nesac")
		firewall.close
	#make the firewall file , executable and configure the start and stop at boot of the OS
	def launchFirewall(self):
		if self.ostype.nomdist[0] == 'centos':
			subprocess.run('systemctl disable firewalld', shell = True)
			subprocess.run('systemctl enable iptables', shell = True)
			subprocess.run('service iptables save',shell = True)
		subprocess.run('chmod +x /usr/local/sbin/firewall.sh',shell = True)
		subprocess.run('/usr/local/sbin/firewall.sh stop',shell = True)
		subprocess.run('/usr/local/sbin/firewall.sh start',shell = True)
		if self.ostype.nomdist[0] != 'centos':
			subprocess.run('netfilter-persistent save',shell = True)