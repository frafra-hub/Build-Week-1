import tkinter
from tkinter import scrolledtext
from portscanner import scan_ports
import threading
import queue
import os
import subprocess




finestra = tkinter.Tk()
finestra.title("Port Scanner")
finestra.geometry("400x610")
finestra.configure(bg="#1e2460")

frame = tkinter.Frame(bg="#1e2460") #Container

#PathPrincipale
directory_attuale_GUI = os.path.dirname(os.path.abspath(__file__))




#Script

def scansiona(): #Bottone
    target_host = inserisci_Host.get()

    port1 = inserisci_portainizio.get()
    inizio_port = int(port1)

    port2 = inserisci_portafine.get()
    fine_port = int(port2)

    result_queue = queue.Queue()

    scan_ports(target_host, inizio_port, fine_port, result_queue)

    result_text.delete(1.0, tkinter.END)
    result_text.insert(tkinter.END, f"Porte aperte su {target_host}\n")

    while not result_queue.empty():
        port = result_queue.get()
        result_text.insert(tkinter.END, f"Porta {port} aperta\n")


def Home():
    finestra.destroy()
    Path_Home = os.path.join(directory_attuale_GUI, "eseguibile2.py")
    subprocess.run(["python", Path_Home])

    
scan_thread = threading.Thread(target=scansiona)
scan_thread.start()
    


##################################################

#Creazione degli widget
spazio_titolo = tkinter.Label(frame, text="Port Scanner", 
    bg="#1e2460",fg="white", font=("Arial", 25, "bold")
    )

spazio_Host = tkinter.Label(frame, text="Host IP ", 
    bg="#1e2460",fg="white", font=("Arial", 12, "bold")
    )
inserisci_Host = tkinter.Entry(frame)

spazio_portainizio = tkinter.Label(frame, text= "Port range", 
    bg="#1e2460", fg="white", font=("Arial", 12, "bold") 
    )
inserisci_portainizio = tkinter.Entry(frame)

inserisci_portafine = tkinter.Entry(frame)

bottone_scansiona = tkinter.Button(frame, text="SCANSIONA", bg="#1e2460", 
fg="white", font=("Arial", 14, "bold"), command=scansiona 
    )

result_text = scrolledtext.ScrolledText(frame, width=30, height=17)

bottone_home = tkinter.Button(frame, text="HOME", command=Home)

#Posizionamento degli Widget
spazio_titolo.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
spazio_Host.grid(row=1, column=0)
inserisci_Host.grid(row=1, column=1, pady=10)
spazio_portainizio.grid(row=2, column=0)
inserisci_portainizio.grid(row=2, column=1, pady=0)
inserisci_portafine.grid(row=3, column=1, pady=10)
bottone_scansiona.grid(row=4, column=0, columnspan=2, pady=10)
result_text.grid(row=5,column=0, columnspan=2, pady=5)
bottone_home.grid(row=6, column=0, columnspan=2, pady=10)

frame.pack(side="top", pady=0)

# Impostiamo il peso (weight) per la riga e le colonne in modo che possano espandersi correttamente
frame.grid_rowconfigure(6, weight=1)  # Per la riga 6 (dove c'è il bottone "HOME")
frame.grid_columnconfigure(0, weight=1)  
frame.grid_columnconfigure(1, weight=1)  




finestra.mainloop() #fino quando c'è questo loop l'app funzionerà
