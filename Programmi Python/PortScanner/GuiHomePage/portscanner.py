import socket
import threading
import queue

host = ""
start_port = 0
end_port = 1050
result_queue = queue.Queue()



#Funzione Scan di una singola porta
def scanner_port(host, port, result_queue):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #oggetto socket
    sock.settimeout(1) #timeout di un secondo

    result = sock.connect_ex((host, port)) #Se la connessione è riuscita è 0 s

    if result == 0:
        #print(f"La Porta {port} è APERTA")
        result_queue.put(port)
        
    sock.close()

    


#Scansione di un range di porte
def scan_ports(host, start_port, end_port, result_queue):
    threads = [] #Creazione di un dizionario vuoto 
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scanner_port, args=(host, port, result_queue))
        threads.append(thread)
        thread.start()

    #Attesa termine thread 
    for thread in threads:
        thread.join()

    

scan_ports(host, start_port, end_port, result_queue)

while not result_queue.empty():
    print(f"Porta {result_queue.get()} è aperta")


