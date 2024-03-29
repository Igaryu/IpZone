#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os, sqlite3

os.system("clear")

zone_in_file = open("zone.list","r")
ISOlst = zone_in_file.readlines()
zone_in_file.close()

for iso in range(0,len(ISOlst)):
	ISOlst[iso]=ISOlst[iso][:2]
	

Nazione=""

while (Nazione not in ISOlst) and Nazione!="zz":
	Nazione=input("Che nazione vuoi bloccare? [zz per uscire altrimenti codie ISO come it per italia] ").lower()
	
if Nazione=="zz": exit()


os.system("clear")


db = sqlite3.connect('IpZone.db')
cursor = db.cursor()
sqlCmd="select NetBloc from ip where ISOcode='"+Nazione+"';"
#input("Codice Nazione= "+Nazione+".")

RigheEstratte=cursor.execute(sqlCmd)
k=0
rulesFileIPT= open(Nazione+"-pure.iptables","w+")
rulesFileIPT.write("*filter\n:Block-"+Nazione.upper()+" - [0:0]\n\n")

input("Genero file ufw ed iptables; con paesi con alto numero di Netbloc può volerci qualche secondo.\nPremere [ INVIO ] per avviare... \n") 
for riga in RigheEstratte:
#	print riga[0]
	cmdIptalbesIPT="-A Block-"+Nazione.upper()+" -s "+ riga[0].strip('\n') + " -j DROP\n"
	rulesFileIPT.write(cmdIptalbesIPT)
	print(".", end='')
	k=k+1

# Concludi file per iptables restore
rulesFileIPT.write("COMMIT\n")

input("\n\nEstratte "+str(k)+" righe. Premere INVIO per concludere.")
rulesFileIPT.close()
db.close()



# -A ufw-user-input -s 1.0.32.0/23 -j DROP
