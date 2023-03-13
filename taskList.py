from tkinter import *

class taskList:
    
    def __init__(self, usuario):
        self.usuario = "piplot"

    ventana = Tk()
    ventana.title = "Piplot"
    ventana.geometry="600x400"
    ventana.configure(background="#B8FFAB")
    
    seccion1 = Frame(ventana, bg="#B8FFAB")
    seccion1.configure(height=10)
    
    
    seccion2 = Frame(ventana, bg="#B8FFCC")
    
    ventana.mainloop()