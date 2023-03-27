
from tkinter import *
<<<<<<< Updated upstream
import tkinter as tk
=======
import sqlite3
from tkinter import messagebox
>>>>>>> Stashed changes


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
        
        
    def conexionBD (self):
        
        try:
            
            conexion = sqlite3.connect("C:/Users/iSkye/Documents/GitHub/Proyecto Integrador/DBTareas.db")
            print("Conectado con exito")
            return conexion
        
        
        except sqlite3.OperationalError:
            
            print("Error al conectar")
    
    def guardar_tarea(self,nom,desc,fini,ffin):
        
        conexion = self.conexionBD()
        cursor = conexion.cursor()
        
        
        if (nom == "" or desc == "" or fini =="" or ffin == ""):
            
            messagebox.showwarning("Advertencia","No se permiten campos vacios")
            
        else:
            
            cursor.execute("INSERT INTO Tareas VALUES (null,?,?,?,?)",(nom,desc,fini,ffin))
            conexion.commit()
            messagebox.showinfo("Informacion","Tarea guardada con exito")
            conexion.close()            
    
        