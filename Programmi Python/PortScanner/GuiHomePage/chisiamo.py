import tkinter
import tkinter.scrolledtext
import subprocess
import os

finestra = tkinter.Tk()
finestra.title("Port Scanner")
finestra.geometry("400x650")
finestra.configure(bg="#1e2460")

#Os Directory
directory_attuale_GUI = os.path.dirname(os.path.abspath(__file__))

frame = tkinter.Frame(bg="#1e2460") #Container

def Home():
    finestra.destroy()
    Path_Home = os.path.join(directory_attuale_GUI, "eseguibile2.py")
    subprocess.run(["python", Path_Home])


#Widget
chisiamo = tkinter.Label(frame,  text="Chi Siamo",
    background="#1e2460", fg="white",font=("Arial", 30, "bold")
    )

didascalia = tkinter.Text(frame, width=38, height=27, 
    wrap=tkinter.WORD, padx=30, pady=20
    )

bottone_home = tkinter.Button(frame, text="HOME", command=Home)

#Posizionamento
chisiamo.grid(row=0, column=1, columnspan=2)
didascalia.grid(row=1, column=1, columnspan=2, pady=10)
bottone_home.grid(row=6, column=0, columnspan=2, pady=0)

#Inserisci il testo
testochisiamo = """Benvenuti in SecurityGriffins, la vostra guardiana digitale nel mondo online. In un'epoca in cui le minacce informatiche sono sempre più sofisticate e pervasive, siamo qui per proteggere ciò che conta di più: la sicurezza della vostra rete aziendale.
"""
testosoftware = """SecurityGriffins Port & WebRequest Scanner è uno strumento avanzato per la sicurezza delle reti aziendali. Il software esegue scansioni complete delle porte di rete e delle richieste web (Web Requests), identificando potenziali vulnerabilità e accessi non autorizzati. Grazie alla sua capacità di monitorare sia le porte che il traffico web, offre una protezione a 360° contro le minacce informatiche, garantendo la massima sicurezza per le infrastrutture IT aziendali.
"""
email1 = """-securitygriffins@gmail.com
"""
email2 = """-securitygriffinoffice@gmail.com
"""
 
didascalia.tag_configure("titolo", font=("Arial", 15, "bold"))

#Insert
didascalia.insert(tkinter.END, testochisiamo)
didascalia.insert(tkinter.END, "\n")
didascalia.insert(tkinter.END, "SOFTWARE\n", "titolo")
didascalia.insert(tkinter.END, testosoftware)
didascalia.insert(tkinter.END, "\n")
didascalia.insert(tkinter.END, "CONTATTACI\n", "titolo")
didascalia.insert(tkinter.END, email1)
didascalia.insert(tkinter.END, email2)

# Impostiamo il peso (weight) per la riga e le colonne in modo che possano espandersi correttamente
frame.grid_rowconfigure(6, weight=1)  # Per la riga 6 (dove c'è il bottone "HOME")
frame.grid_columnconfigure(0, weight=1)  
frame.grid_columnconfigure(1, weight=1)


#FRAME
frame.pack(side="top", pady=25)

finestra.mainloop()



