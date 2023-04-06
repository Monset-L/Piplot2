from tkinter import *
from tkinter import  ttk
import tkinter as tk
from ControladorPiplot import *


controlador = controladorPBD()

def ejecutaInsert():
    controlador.guardarUsuario(varNomb.get(), varDesc.get(), varIni.get(), varFin.get())

def ejecutaSelectU():
    rsUsuario = controlador.consultarTarea(BusT.get())
    
    for usu in rsUsuario:
        cadena = str(usu[0])+" "+ str(usu[1]) + " "+ str(usu[2])+ " "+ str(usu[3]+" "+ str(usu[4]))
    if(rsUsuario):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showerror("Error","Tarea no encontrado")
        
def tareas():
    rsUsuario = controlador.consulta()
    tree.delete(*tree.get_children())
    for usu in rsUsuario:
        tree.insert("", "end",text=usu[0], values=(usu[1], usu[2], usu[3], usu[4]))
    

Ventana = Tk()
Ventana.title("PIPLOT")
Ventana.geometry("500x350")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#Registro de tareas

titulo = Label(pestana1,text="Registro de Tareas", fg="Black", font=("Arial Black",18)).pack()

varNomb = tk.StringVar()
lblNomb = Label(pestana1, text="Nombre: ").pack()
txtNomb = Entry(pestana1,textvariable=varNomb).pack()

varDesc = tk.StringVar()
lblDesc = Label(pestana1, text="Descripcion: ").pack()
txtDesc = Entry(pestana1,textvariable=varDesc).pack()

varIni = tk.StringVar()
lblIni = Label(pestana1, text="Fecha Inicio: ").pack()
txtIni = Entry(pestana1,textvariable=varIni).pack()

varFin = tk.StringVar()
lblFin = Label(pestana1, text="Fecha Inicio: ").pack()
txtFin = Entry(pestana1,textvariable=varFin).pack()

btnGuardar = Button(pestana1, text="Guardar Tarea: ", command=ejecutaInsert).pack()

#Buscar una tarea

titulo = Label(pestana2,text="Buscar Tarea", fg="Black", font=("Arial Black",18)).pack()

BusT = tk.StringVar()
lblid= Label(pestana2, text="Numero de tarea: ").pack()
txtid = Entry(pestana2,textvariable=BusT).pack()
btnBusqueda = Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()

subBus = Label(pestana2,text="Tarea:",fg="Black",font=("Arial Black",18)).pack()
textBus = tk.Text(pestana2,height=5,width=52)
textBus.pack()

#Consulta de todas las tareas

Titulo = Label(pestana3,text="Tareas:",fg="Black",font=("Arial Black",15)).pack()
tree = ttk.Treeview(pestana3)
tree['columns']=('NomTarea', 'DescTarea', 'FInicio', 'FFin')
tree.column('#0', width=30, minwidth=30)
tree.column('NomTarea', width=150, minwidth=150)
tree.column('DescTarea', width=120, minwidth=120)
tree.column('FInicio', width=80, minwidth=80)
tree.column('FFin', width=80, minwidth=80)
tree.heading('#0', text='Id')
tree.heading('NomTarea', text='NomTarea')
tree.heading('DescTarea', text='DescTarea')
tree.heading('FInicio', text='FInicio')
tree.heading('FFin', text='FFin')
tree.pack()
btnBusquedas = Button(pestana3,text="Consultar",command=tareas).pack()


panel.add(pestana1, text="Registro de tareas")
panel.add(pestana2, text="Buscar")
panel.add(pestana3, text="Tareas")
panel.add(pestana4, text="Eliminar Tarea")
panel.add(pestana5, text="Actualizar Tarea")


Ventana.mainloop()