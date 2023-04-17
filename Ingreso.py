from tkinter import *
from tkinter import  ttk
import tkinter as tk
from ControladorPiplot import *


controlador = controladorPBD()

def ejecutaInsert():
    controlador.guardarUsuario(varNomb.get(), varDesc.get(), varIni.get(), varFin.get())

def ejecutaSelectU():
    rsUsuario = controlador.consultarTarea(BusT.get())
    
    textBus.delete("0.0",END)

    if (rsUsuario == None):
        return
    for usu in rsUsuario:
        cadena = str(usu[0])+" "+ str(usu[1]) + " "+ str(usu[2])+ " "+ str(usu[3]+" "+ str(usu[4]))
    if(rsUsuario):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showerror("Error","Tarea no encontrado")
        
def tareas():
    rsUsuario = controlador.consulta()

    if (rsUsuario == None):
        return

    tree.delete(*tree.get_children())
    for usu in rsUsuario:
        tree.insert("", "end",text=usu[0], values=(usu[1], usu[2], usu[3], usu[4]))
        
#Funcion eliminar tareas

def ejecutaDelete():
    
    controlador.eliminarusuario(BusT3.get())
    
#Funcion Actualizar tarea   

def ejecutaUpdate():
    
    controlador.actualizartarea(BusT4.get(),varNomb2.get(), varDesc2.get(), varIni2.get(), varFin2.get())

Ventana = Tk()
Ventana.title("PIPLOT")

Ventana.geometry("600x400")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)


# Define un estilo personalizado para cada pestaña
style1 = ttk.Style()
style1.configure('Custom1.TFrame', background='lightblue')

style2 = ttk.Style()
style2.configure('Custom2.TFrame', background='lightgreen')

style3 = ttk.Style()
style3.configure('Custom3.TFrame', background='yellow')

style4 = ttk.Style()
style4.configure('Custom4.TFrame', background='pink')

style5 = ttk.Style()
style5.configure('Custom5.TFrame', background='#F68616')

# Asigna el estilo personalizado apropiado a cada pestaña
pestana1.configure(style='Custom1.TFrame')
pestana2.configure(style='Custom2.TFrame')
pestana3.configure(style='Custom3.TFrame')
pestana4.configure(style='Custom4.TFrame')
pestana5.configure(style='Custom5.TFrame')

titulo = Label(pestana1,text="Registro de Tareas", fg="Black", font=("Arial Black",18), bg='lightblue').pack()

varNomb = tk.StringVar()
lblNomb = Label(pestana1, text="Nombre: ", font=("Times",12),bg='lightblue').pack(pady=8)
txtNomb = Entry(pestana1,textvariable=varNomb).pack()

varDesc = tk.StringVar()
lblDesc = Label(pestana1, text="Descripcion: ", font=("Times",12),bg='lightblue').pack(pady=10)
txtDesc = Entry(pestana1,textvariable=varDesc).pack()

varIni = tk.StringVar()
lblIni = Label(pestana1, text="Fecha Inicio: ", font=("Times",12),bg='lightblue').pack(pady=10)
txtIni = Entry(pestana1,textvariable=varIni).pack()

varFin = tk.StringVar()
lblFin = Label(pestana1, text="Fecha Fin: ", font=("Times",12),bg='lightblue').pack(pady=10)
txtFin = Entry(pestana1,textvariable=varFin).pack()

btnGuardar = Button(pestana1, text="Guardar Tarea ", bg="#003E68", fg="white", font=("Arial Black",10), command=ejecutaInsert).pack(pady=18)


#Buscar una tarea

titulo = Label(pestana2,text="Buscar Tarea", fg="Black", font=("Arial Black",18),bg='lightgreen').pack()

BusT = tk.StringVar()
lblid= Label(pestana2, text="Numero de tarea: ", bg='lightgreen',font=("Times",16)).pack(pady=8)
txtid = Entry(pestana2,textvariable=BusT).pack()
btnBusqueda = Button(pestana2,text="Buscar", font=("Arial Black",10), bg="#FFDE71" ,command=ejecutaSelectU).pack(pady=10)

subBus = Label(pestana2,text="Tarea:",fg="Black",font=("Times",16),bg='lightgreen').pack(pady= 10)
textBus = tk.Text(pestana2,height=7,width=52)
textBus.pack()

#Consulta de todas las tareas

Titulo = Label(pestana3,text="Tareas:",fg="Black",font=("Arial Black",15), bg="yellow").pack(pady=8)
tree = ttk.Treeview(pestana3)
tree['columns']=('NomTarea', 'DescTarea', 'FInicio', 'FFin')
tree.column('#0', width=30, minwidth=30)
tree.column('NomTarea', width=150, minwidth=150)
tree.column('DescTarea', width=120, minwidth=120)
tree.column('FInicio', width=80, minwidth=80)
tree.column('FFin', width=80, minwidth=80)
tree.heading('#0', text='Id')
tree.heading('NomTarea', text='Nombre Tarea')
tree.heading('DescTarea', text='Descripción')
tree.heading('FInicio', text='Fecha Inicio')
tree.heading('FFin', text='Fecha Fin')
tree.pack(padx=10, pady=10, fill=BOTH, expand=True)
btnBusquedas = Button(pestana3, font=("Arial Black", 10),text="Consultar",command=tareas).pack(pady=10)

#Eliminar tarea

titulo = Label(pestana4,text="Eliminar Tarea", fg="Black", font=("Arial Black",18), bg="pink").pack(pady=10)

BusT3 = tk.StringVar()

lblid= Label(pestana4, text="Numero de tarea: ", bg="pink", font=("Times",16)).pack(pady=10)

txtid = Entry(pestana4,textvariable=BusT3).pack(pady=10)

btnBusqueda = Button(pestana4,text="Eliminar", bg="red", font=("Arial Black", 10), fg="white",command=ejecutaDelete).pack(pady=10)


#Actualizar datos de la tarea con id

titulo = Label(pestana5,text="Actualizar Tarea", fg="Black", font=("Arial Black",18), bg="#F68616").pack(pady=3)

BusT4 = tk.StringVar()

lblid= Label(pestana5, text="Numero de tarea: ", bg="#F68616", font=("Times", 12)).pack(pady=3)

txtid = Entry(pestana5,textvariable=BusT4).pack(pady=3)

varNomb2 = tk.StringVar()

lblNomb = Label(pestana5, text="Nombre: ", bg="#F68616", font=("Times", 12)).pack(pady=3)

txtNomb = Entry(pestana5,textvariable=varNomb2).pack(pady=3)

varDesc2 = tk.StringVar()

lblDesc = Label(pestana5, text="Descripcion: ", bg="#F68616", font=("Times", 12)).pack(pady=3)

txtDesc = Entry(pestana5,textvariable=varDesc2).pack(pady=3)

varIni2 = tk.StringVar()

lblIni = Label(pestana5, text="Fecha Inicio: ", bg="#F68616", font=("Times", 12)).pack(pady=3)

txtIni = Entry(pestana5,textvariable=varIni2).pack(pady=3)

varFin2 = tk.StringVar()

lblFin = Label(pestana5, text="Fecha Final: ", bg="#F68616", font=("Times", 12)).pack(pady=3)

txtFin = Entry(pestana5,textvariable=varFin2).pack(pady=3)


btnBusqueda = Button(pestana5,text="Actualizar", font=("Arial Black", 10),command=ejecutaUpdate).pack(pady=5)



panel.add(pestana1, text="Registro de tareas")
panel.add(pestana2, text="Buscar")
panel.add(pestana3, text="Tareas guardadas")
panel.add(pestana4, text="Eliminar Tarea")
panel.add(pestana5, text="Actualizar Tarea")


Ventana.mainloop()