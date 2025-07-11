import socket

SRV_ADDRESS="0.0.0.0"
SRV_PORT=int(input("Inserisci la porta su cui vuoi ascoltare: "))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((SRV_ADDRESS,SRV_PORT))
s.listen(1)
print ("Server inizializzato! In ascolto sulla porta ", SRV_PORT,"\nIn attesa di connesione...")
connection, address= s.accept()
print ("Il client si è connesso con il seguente indirizzo: ",address)
connection.close()