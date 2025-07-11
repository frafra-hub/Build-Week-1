import tkinter
from tkinter import scrolledtext, filedialog, messagebox
import os
from httprequest2 import run_request
import subprocess




finestra = tkinter.Tk()
finestra.title("Port Scanner")
finestra.geometry("400x610")
finestra.configure(bg="#1e2460")

frame = tkinter.Frame(bg="#1e2460") #Container


#PathPrincipale
directory_attuale_GUI = os.path.dirname(os.path.abspath(__file__))

#Funzioni
def esegui_request():

    url = inserisci_url.get()

    if not url:
        messagebox.showerror("Inserisci un URL valido.")
        return
    
    if not url.startswith("http://"):
        url = "http://" + url
        
    try:
        log_file_path = run_request(url)
        result_text.delete(1.0, tkinter.END)
        result_text.insert(tkinter.END, f"Le richieste sono state completate con successo. \nSalvato in:\n{log_file_path}\n")

    except Exception as e:
        messagebox.showerror("Errore")

def Home():
    finestra.destroy()
    Path_Home = os.path.join(directory_attuale_GUI, "eseguibile2.py")
    subprocess.run(["python", Path_Home])


def download_buttonexc():
    log_dir = "http_requests_logs"
    if not os.path.exists(log_dir):
        messagebox.ERROR("Non ci sono log da scaricare")
        return
    
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filepath:
        latest_log_file = max([os.path.join(log_dir, f) for f in os.listdir(log_dir)], key=os.path.getctime)
        with open(latest_log_file, "r") as file:
            content = file.read()

        with open(filepath, "w") as file:
            file.write(content)


#Widget
spazio_titolo = tkinter.Label(frame, text="Web Request", 
    bg="#1e2460", fg="white",font=("Arial", 25, "bold")
    )

spazio_IP = tkinter.Label(frame, text="URL ", 
    bg="#1e2460", font=("Arial", 12, "bold")
    )

inserisci_url = tkinter.Entry(frame, width=31)
inserisci_url.insert(tkinter.END, "http://")

bottone_scansiona = tkinter.Button(frame, text="SCANSIONA", bg="#1e2460", 
fg="white", font=("Arial", 14, "bold"), command=esegui_request, width=23
    )

result_text = scrolledtext.ScrolledText(frame, width=30, height=22)

download_button = tkinter.Button(frame, text="DOWNLOAD", command=download_buttonexc, width=12)

bottone_home = tkinter.Button(frame, text="HOME", command=Home, width=12)


#Posizionamento Widget
spazio_titolo.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
inserisci_url.grid(row=1, column=0, columnspan=2)
bottone_scansiona.grid(row=2, column=0, columnspan=2, pady=10)
result_text.grid(row=3,column=0, columnspan=2, pady=5)
download_button.grid(row=4, column=1, columnspan=1)
bottone_home.grid(row=4, column=0, columnspan=1)

frame.pack(side="top", pady=0)

finestra.mainloop() 
