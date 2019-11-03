#!/usr/bin/env python3
import fileinput
import subprocess
class FireWall:

	def __init__(self,listInterface):
		self.interface = listInterface
		self.openPort=list()
		self.protocol=list()

	def initFichier(self,interface):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		firewall.write("#!/bin/bash\n")
		firewall.write("IPT=/sbin/iptables\n")
		firewall.write("WAN="+self.interface[0]+"\n")
		if self.interface[1]!=None:
			firewall.write("LAN="+self.interface[1]+"\n")
		firewall.write("firewall_start(){\n \n")
		firewall.close()

	def standardConfig(self):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		firewall.write("$IPT -A INPUT -i $WAN -m state --state ESTABLISHED,RELATED -j ACCEPT \n")
		firewall.write("$IPT -A INPUT -i lo -j ACCEPT \n")
		firewall.write("$IPT -P INPUT DROP \n")
		firewall.write("$IPT -P FORWARD DROP")

	def OpenPort(self,openPort,protocol):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		i = 0
		while i<(len(openPort)-1):
			firewall.write("$IPT -A INPUT -p "+protocol[i]+" --dport "+openPort[i]+" -j ACCEPT \n")
			i+=1
		firewall.close

	def endConfig(self):
		firewall = open("/usr/local/sbin/firewall.sh", "a")
		firewall.write("} \n \n")	
		firewall.write("firewall_stop(){ \n$IPT -F \n$IPT -t nat -F \n$IPT -P INPUT ACCEPT \n$IPT -P FORWARD ACCEPT \n} \n")
		firewall.write("firewall_restart(){ \nfirewall_stop \nsleep 2 \nfirewall_start \n}")
		firewall.write("case $1 in \n\t\t'start') \n\t\t\tfirewall_start \n\t\t\t;; \n\t\t'stop') \n\t\t\tfirewall_stop \n\t\t\t;; \n\t\t'restart') \n\t\t\tfirewall_restart \n\t\t\t;; \n*) \n\t\t\techo usage: -bash {start|stop|restart} \nesac")
		firewall.close
	
	def launchFirewall(self):
		executable = subprocess.run('chmod +x /usr/local/sbin/firewall.sh',shell = True)
		temp = {
			'\t\t#start firewall': 'post-up /usr/local/sbin/firewall.sh start',
			'\t\t#start firewall': 'pre-down /usr/local/sbin/firewall.sh stop'
		}
		for line in fileinput.input('/etc/network/interfaces',inplace = True):
			line = line.rstrip('\r\n')
			print(temp.get(line, line))