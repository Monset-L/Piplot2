
from tkinter import *


class tareas ():
    
    def __init__(self):
        
        self.tarea = ""
        
        

    def agregar_tarea(entrada):
        
        lista = []
        elemento = entrada.set()
        lista.append(elemento)
        
        
        listbox = Listbox(ventana, width=30)
        listbox.insert(END, elemento)
        listbox.pack()
        
        entrada.delete(0, END)
        print(entrada)
        
       
        
    def ver_tarea():
        
        ventana = Tk()




        listbox = Listbox(ventana, width=30)
        

        ventana.mainloop()