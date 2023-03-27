from tkinter import Tk, Button, Frame, messagebox, Label, Entry

from controlador import *


controlador = tareas()
 
class ingreso:
    def __init__(self):
        self
     
  
    def showExito():
        msg= messagebox.showinfo("Exito", "Tu ingreso se agregó exitosamente")
        
        
    def ejecuta_insert():
        
        controlador.guardar_tarea(nombre2.get(), Descripcion2.get(), FI2.get(), FF2.get())
        
        
    ventana = Tk()
    ventana.title("Tareas")
    ventana.geometry("600x400")
    
    seccion1 = Frame(ventana, bg = "#B8FFAB")
    seccion1.pack(expand=True, fill="both")
    
    bienvenida = Label(seccion1, text="Registro de Tareas", bg="#B8FFAB", font="Lucida 20 bold")
    bienvenida.pack(pady=30)
    
    Nombre = Label(seccion1, text="Nombre de la tarea:", font="Arial 12", bg="#B8FFAB")
    Nombre.place(x=190, y=90)
    
    NoT = Label(seccion1, text="No. de la tarea:", font="Arial 12", bg="#B8FFAB")
    NoT.place(x=200, y=120)
    
    Descripcion = Label(seccion1, text="Descripción:", font="Arial 12", bg="#B8FFAB")
    Descripcion.place(x="200", y="140")
    
    FI = Label(seccion1, text="Fecha de inicio:", font="Arial 12", bg="#B8FFAB")
    FI.place(x="200", y="165")
    
    FF = Label(seccion1, text="Fecha de fin:", font="Arial 12", bg="#B8FFAB")
    FF.place(x="200", y="190")
    
    nombre2 = Entry(seccion1)
    nombre2.place(x=340, y=95)
    
    NoT2 = Entry(seccion1)
    NoT2.place(x=340, y=120)
    
    Descripcion2 = Entry(seccion1)
    Descripcion2.place(x=340, y=145)
    
    FI2 = Entry(seccion1)
    FI2.place(x=340, y=170)
    
    FF2 = Entry(seccion1)
    FF2.place(x=340, y=195)

    botonRegistrar = Button(seccion1, text="Guardar", fg="black", bg="White", font="Arial 12", command=ejecuta_insert)
    botonRegistrar.place(x=260, y=300)
    
    ventana.mainloop()