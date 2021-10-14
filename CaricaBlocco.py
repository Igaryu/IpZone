#!/usr/bin/python 
# -*- coding: utf-8 -*-
import os
def cls():
        if os.name=='posix':
                os.system('clear')
        else:
                os.system('cls')

def Allarme(n):
    print((n * chr(7)))


cls()


iso=input("Digitare codice ISO del paese da bloccare [2 lettere: it=italia]: ")
FileName= iso+"-pure.iptables"
try:
	rulesFile= open(FileName,"r")
	rulesApply=rulesFile.readlines()
        rulesFile.close()
except:
	Allarme(3)
	print("Attenzione file richiesto non presente: hai eseguito precedentemente GeneraBlocco.py ?")
	input("Premi ENTER per usiucre.")
	exit(-1)

cmdName="/sbin/iptables-restore -n " + FileName
try:
	os.system(cmdName)
	print(("Caricato " + str(len(rulesApply)) +" regole dal blocco file "+FileName))
except:
	Allarme(3)
	print("Attenzione qualcosa non ha funzionato nel caricamento delle regole: verificare iptables!!!")
	input("Premi ENTER per uscire.")
	exit(-9)
