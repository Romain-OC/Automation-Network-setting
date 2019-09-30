Class FireWall

def _init_(self,listInterface):
	self.interface = list()
	self.typeFW = standard
	self.openPort=list()
	self.protocol=list()

def initFichier(interface):
	firewall = open("/usr/local/sbin/firewall.sh", "a")
	firewall.write("#!/bin/bash\n")
	firewall.write("IPT=/sbin/iptables\n")
	firewall.write("WAN="+self.interface[0]"\n")
	if self.interface[1]!=null:
		firewall.write("LAN="+self.interface[1]"\n")
	firewall.write("firewall_start(){\n \n")
	firewall.close()

def standardConfig():
	firewall = open("/usr/local/sbin/firewall.sh", "a")
	firewall.write("$IPT -A INPUT -i $WAN -m state --state ESTABLISHED,RELATED -j ACCEPT \n")
	firewall.write("$IPT -A INPUT -i lo -j ACCEPT \n")
	firewall.write("$IPT -P INPUT DROP \n")
	firewall.write("$IPT -P FORWARD DROP")

def OpenPort(openPort[],protocol[]):
	firewall = open("/usr/local/sbin/firewall.sh", "a")
	i = 0
	while i<(len(openPort)-1):
		firewall.write("$IPT -A INPUT -p "+protocol[i]+" --dport "+openPort[i]+" -j ACCEPT \n")
		i+=1
	firewall.close

def endConfig():
	firewall = open("/usr/local/sbin/firewall.sh", "a")
	firewall.write("} \n \n")	
	firewall.write("firewall_stop(){ \n$IPT -F \n$IPT -t nat -F \n$IPT -P INPUT ACCEPT \n$IPT -P FORWARD ACCEPT \n} \n")
	firewall.write("firewall_restart(){ \nfirewall_stop \nsleep 2 \nfirewall_start \n}")
	firewall.write("case $1 in \n\t\t'start') \n\t\t\tfirewall_start \n\t\t\t;; \n\t\t'stop') \n\t\t\tfirewall_stop \n\t\t\t;; \n\t\t'restart') \n\t\t\tfirewall_restart \n\t\t\t;; \n*) \n\t\t\techo "usage: -bash {start|stop|restart}" \nesac")


