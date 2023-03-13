import tkinter as tk
from controlador import *



ventana = tk.Tk() 
    
def agregar ():
    asd.agregar_tarea(entrada.get())
    
def ver():
    
    asd.ver_tarea()
    
asd = tareas
    
    

ventana.title = "Piplot"
ventana.geometry="600x400"
ventana.configure(background="#B8FFAB")
    
seccion1 = Frame(ventana, bg="#B8FFAB")
seccion1.configure(height=10)
    
entrada = tk.Entry(ventana)
entrada.pack()
    
boton_agregar = tk.Button(ventana, text="Agregar",command=agregar)
boton_agregar.pack()

boton_ver = tk.Button(ventana, text="Ver tarea",command=ver)
boton_ver.pack()





seccion2 = Frame(ventana, bg="#B8FFCC")

 
    
ventana.mainloop()