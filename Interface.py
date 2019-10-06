import shutil
import subprocess
from P6 import DetectOS


class Interface:

   def _init_(self):

      self.nom = "eth"
      self.address = list()
      self.macAddress = subprocess.check_output('ip a |grep ether |cut -d' ' -f6', shell = True)
      self.listMac = Self.macAddresss.split('\n')
      self.chemin = chemin()
      self.ostype = DetectOS()
   
   #def __getNom__(self, nom):
   
   #def __getAddress__(self, address, int id):
      #return Self._address[id]

   #def __setNom__(self, nom,val_nom):

   #def __setAddress__(self, address,val_address):

   def chemin(self,ostype.nom):
      switcher = {
         debian : Self.chemin= "/etc/network/interfaces"
         break;
         ubuntu : Self.chemin= "/etc/netplan/01-netcfg.yaml"
         break;
         centos : Self.chemin= "/etc/sysconfig/network-scripts/"
         break;
         default: Self.chemin= "la méthode ne détecte pas l'OS"
   }

   def renameInterface(listMac):

      mon_fichier = open("/etc/udev/rules.d/70-persistent-net.rules", "a")
      i = 0
      while i<(len(listMac)-1):
         mon_fichier.write("SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*",ATTR{address}=="+self.listMac(i)+",ATTR{dev_id}=="0x0", ATTR{type}=="1",KERNEL=="eth*", NAME=""eth"+i+"\n")
         i+=1
      mon_fichier.close()

   def configInterface(listMac,address):
      if chemin == "/etc/network/interfaces"
      filePath = shutil.copy('interfaces', '/etc/network/')
      mon_fichier = open(chemin,"a")
      i=0
      while i<(len(listMac)-1):
         chaine = "#allow-hotplug eth"+i
         
         # on boucle sur les lignes du fichier1 original
         for ligne in mon_fichier :

               if chaine in ligne :

                  ligne = "allow-hotplug eth"+i
                  mon_fichier.write(ligne)
         
         chaine = "#iface eth"+i+" inet dhcp"

         for ligne in mon_fichier :

               if chaine in ligne :

                  ligne = "iface eth"+i+" inet static"
                  mon_fichier.write(ligne)

         chaine = "#address eth"+i

         for ligne in mon_fichier :

               if chaine in ligne :

                  ligne = "address "+Self.address[i]
                  mon_fichier.write(ligne)

         chaine = "#netmask eth"+i

         for ligne in mon_fichier :

               if chaine in ligne :

                  ligne = "netmask 255.255.255.0"
                  mon_fichier.write(ligne)
      mon_fichier.close()

      else if chemin == "Ubuntu"
      filePath = shutil.copy('01-netcfg.yaml', '/etc/netplan/')
         mon_fichier = open(chemin,"a")
      i=0
      while i<(len(listMac)-1):
         chaine = "#enp1s0f0:"
         
         # on boucle sur les lignes du fichier1 original
         for ligne in mon_fichier :

               if chaine in ligne :

                  ligne = "eth"+i+":"
                  mon_fichier.write(ligne)
         
         chaine = "#dhcp4: yes"

         for ligne in mon_fichier :

               if chaine in ligne :

                  ligne = "dhcp4: yes"
                  mon_fichier.write(ligne)

         chaine = "#addresses: []"

         for ligne in mon_fichier :

               if chaine in ligne :

                  ligne = "#addresses: ["+Self.address[i]+"/24]"
                  mon_fichier.write(ligne)
      mon_fichier.close()
      #else if chemin == "CentOS"
