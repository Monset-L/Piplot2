from tkinter import *
from controlador import *

ventana = Tk() 
ventana.title =("Piplot")
ventana.geometry=("600x400")
ventana.configure(background="#B8FFAB")
    
seccion1 = Frame(ventana, bg="#B8FFAB")
seccion1.pack(expand=True, fill='both')
      
def agregar ():
    asd.agregar_tarea(entrada.get())
    
def ver():
    
    asd.ver_tarea()
    
asd = tareas()
    
entrada = Entry(seccion1)
entrada.pack()
    
boton_agregar = Button(seccion1, text="Agregar",command=agregar)
boton_agregar.pack()

boton_ver = Button(seccion1, text="Ver tarea",command=ver)
boton_ver.pack()

ventana.mainloop()