#!/usr/bin/python 
# -*- coding: utf-8 -*-
import wget
import os, tempfile, shutil,sqlite3

# Variable definition:
# oldDir					Dir frome where app was executed
# ISOlst 					List of ISO countries codes
# tmpDir					Temporary directory created to do all stuff
# tmpFile					Handler for FileTemporaneo.txt file
# url						URL where download from gziped file
# gzFile					Name of downloaded gziped file
# cmdName					Command to execute as os.system()
# IsoTotZone					Handler for IstoTotFile.zone file
# db						SqLite3 database handler for IpZone.db database
# cursor					SqLite3 cursor for IpZone.db database
# sqlCmd					SqLite3 commands to execute in SqLite3 environment
# iso, k					For loop variables.
# isofile					Handler for national Netblock files. Ex: uz.zone
# wipInd					Local copy of fiedl in SqLite3 database 
# wISOcode					Local copy of fiedl in SqLite3 database
# wNetBloc					Local copy of fiedl in SqLite3 database
# wISOandIP					Local copy of fiedl in SqLite3 database
# tmpISOlst					List of NetBloc per nation file that we are analyzing
# zone_in_file					File from where read ISO country list




a=os.uname()
OS=a[0]

os.system("clear")
oldDir=os.getcwd()

zone_in_file = open("zone.list","r")
ISOlst = zone_in_file.readlines()

tmpDir = tempfile.mkdtemp(suffix='', prefix='JoeDir')
#shutil.copy("IpZoneVuoto.db",tmpDir+"/IpZone.db")


os.chdir(tmpDir)
tmpFile= open("FileTemporaneo.txt","w+")

print("\n\nScarico file totale zone: attendere un attimo ...") 
url = 'http://www.ipdeny.com/ipblocks/data/countries/all-zones.tar.gz'
#gzFile = wget.download(url)
gzFile ='/Users/giuseppecurto/MEGA/Lavoro/Python/IpZone/all-zones.tar.gz'
#gzFile=tmpDir+"/"+gzFile
if OS=="Darwin":
    cmdName='/usr/bin/tar xzf ' + gzFile
elif OS=="Linux":
    cmdName='/bin/tar xzf ' + gzFile
#else if OS="Windows":

print("\n\nDecomprimo file zone...")
os.system(cmdName)


isoTotZone=open("IsoTotFile.zone","w") 				#create or open IsoTotFile.zone

db = sqlite3.connect('IpZone.db')
cursor = db.cursor()
sqlCmd='CREATE TABLE "ip" (`ipInd` INTEGER NOT NULL UNIQUE, `ISOcode` INTEGER, `NetBloc` TEXT, `ISOandIP` TEXT, PRIMARY KEY(ipInd,ISOcode,NetBloc,ISOandIP));'
cursor.execute(sqlCmd)
db.commit()

				
for iso in range(0,len(ISOlst)):
	ISOlst[iso]=ISOlst[iso][:2]
wipInd=0				
for iso in range(0,len(ISOlst)):						#ciclo esterno
#	os.system("clear")
	print(("file in elaborazione: "+ISOlst[iso]))

	isofile = open(ISOlst[iso][:2]+".zone","r")
	tmpISOlst=isofile.readlines()
	wISOcode=""
	wNetBloc=""
	wISOandIP=""
	for k in range (0,len(tmpISOlst)):					#ciclo interno
		isoTotZone.write(ISOlst[iso] +" "+ tmpISOlst[k])
		wipInd=wipInd + 1
		wISOcode=ISOlst[iso]
		wNetBloc=tmpISOlst[k]
		wISOandIP=ISOlst[iso] +" - "+tmpISOlst[k]
		cursor.execute('''INSERT INTO ip(ipInd, ISOcode, NetBloc, ISOandIP) VALUES(?,?,?,?)''', (wipInd, wISOcode, wNetBloc, wISOandIP))
		
		
	db.commit()

zone_in_file.close() 
tmpFile.close()
isoTotZone.close()

input("Premi un tasto per cancellare tutto da "+tmpDir+" e chiudere!!")
db.close()
shutil.copy("IpZone.db",oldDir+"/IpZone.db")
os.chdir(oldDir)
shutil.rmtree(tmpDir, ignore_errors=True)
