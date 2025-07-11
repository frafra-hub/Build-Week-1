from scapy.all import *

def lista (packet):
    print (packet.summary())

while True:
    print("Inizio della cattura dei pacchetti...")
    sniff(prn=lista, store=0, timeout=10)
    break
print ("Rilevamento terminato")


