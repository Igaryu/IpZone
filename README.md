# IpZone
 
## Progetto per la creazione, generazione e caricamento di liste di blocco per interi paesi via IpTables
***
Il progetto nasce dall’esigenza di gestire, in maniera rapida, il blocco del traffico proveniente da interi paesi. I clienti, in generale, ricevono molti tentativi di accesso non regolari, da paesi con cui **non hanno nulla a che fare**, per cui è diventato comodo bloccare l’intero paese _tout court_ in tempi ragionevoli.

Avevo trovato un progetto simile sviluppato in BASH, ma i tempi di caricamento erano davvero **biblici** nel caso di paesi con alto numero di *netblock*. Ho riscritto la procedura in Python e sfruttando la capacità di iptables di caricare velocemente una serie piuttosto nutrita di regole via _iptalbes-restore_ ho sveltito decisamente il processo di caricamento, vero e proprio, delle regole.

La procedura permette, nella corretta sequenza, le seguenti operazioni: 

1. ScaricaZone.py: scarica il file aggiornato delle zone e dei netblock così da lavorare su dati _freschi_ per creare un database SqLite3 più veloce da gestire, nella fase successiva.
2. GeneraBlocco.py: chiede all’utente per quale nazione, via codice paese a due lettere, vuole generare il file delle regole: il file creato avrà il seguente schema: ??-pure-zone.dat con ?? sostituito dal codice paese, per cui nel caso della Cina, ad esempio il file si chiamerà: **cn-pure-zone.dat**
3. CaricaBlocco.py: legge il file, per il paese richiesto, e carica il blocco di regole per IpTables in modo veloce, usando _iptables-restore_ invece di migliaia di comandi _iptables -A_ (da qui la differenza enorme tra lo script BASH a cui mi sono ispirato, e la mia versione in Python).

Potrei creare un file _main.py_ per eseguire i vari script Python in sequenza, ma mi pare davvero non necessario: basta lanciare gli script, nella sequenza corretta, ossia quella riportata sopra, per ottenere il risultato voluto.

Buoni blocchi!!

J.C.
