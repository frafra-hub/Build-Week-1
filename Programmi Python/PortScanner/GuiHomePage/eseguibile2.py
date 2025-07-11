import tkinter
from PIL import Image, ImageTk #Perchè di base tkinter non supporta .jpeg e .png
import subprocess #serve a collegare pagine esterne
import os

#Os Directory
directory_attuale_GUI = os.path.dirname(os.path.abspath(__file__))


#Funzione PageSwap
def ApriPortScanner():
    finestra.destroy()
    Path_Gui = os.path.join(directory_attuale_GUI, "GUIportscanner.py")
    subprocess.run(["python", Path_Gui])

def ChiSiamoButton():
    finestra.destroy()
    Path_ChiSiamo = os.path.join(directory_attuale_GUI, "chisiamo.py")
    subprocess.run(["python", Path_ChiSiamo])

def WebRequest():
    finestra.destroy()
    Path_Request = os.path.join(directory_attuale_GUI, "GUIwebrequest.py")
    subprocess.run(["python", Path_Request])



#Finestra Default
finestra = tkinter.Tk()
finestra.title("Home Page")
finestra.geometry("400x600")
finestra.configure(bg="#1e2460")



#Immagine Grifone
image_path = os.path.join(directory_attuale_GUI, "GrifFree.png")
Img = Image.open(image_path)
Img_dimensione = Img.resize((200, 200))
Img_tk = ImageTk.PhotoImage(Img_dimensione)





#Frame
frame = tkinter.Frame(finestra, bg="#1e2460")


#Creazione Widget
BottonePort = tkinter.Button(
    frame, text="Port Scanner", width=16, height=3, font=("Arial", 18, "bold"), 
    bg="#1e2460", fg="white", command=ApriPortScanner
    )


BottoneRequest = tkinter.Button(
    frame, text="Web Request", width=16, height=3, font=("Arial", 18, "bold"), 
    bg="#1e2460", fg="white", command=WebRequest,
    )

BottoneChiSiamo = tkinter.Button(
    frame, text="Chi siamo", width=16, height=3, font=("Arial", 18, "bold"), 
    bg="white", fg="#252850", command=ChiSiamoButton 
    )


ImgGrifone = tkinter.Label(frame, image=Img_tk, bg="#1e2460")



#Posizionameto Widget
ImgGrifone.pack(pady=0)
BottonePort.pack(pady=6)
BottoneRequest.pack(pady=6)
BottoneChiSiamo.pack(pady=6)


frame.pack(side="top", pady=30)


#MainLoop
finestra.mainloop()
