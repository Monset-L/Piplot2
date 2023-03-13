
from tkinter import *
import tkinter as tk


class tareas ():
    
    def __init__(self):
        
        self.tarea = ""
        
        

    def agregar_tarea(entrada):
        
        lista = []
        elemento = entrada.set()
        lista.append(elemento)
        
        
        listbox = tk.Listbox(ventana, width=30)
        listbox.insert(tk.END, elemento)
        listbox.pack()
        
        entrada.delete(0, tk.END)
        print(entrada)
        
       
        
    def ver_tarea():
        
        ventana = tk.Tk()




        listbox = tk.Listbox(ventana, width=30)
        

        ventana.mainloop()