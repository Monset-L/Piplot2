from tkinter import *
from tkinter import ttk
from controlador import *
from Ingreso import *

ventanam = Tk() 
ventanam.title("Piplot")
ventanam.geometry("700x400")
 
controltareas = tareas()
intIngreso = ingreso()
   
s1 = Frame(ventanam, bg="#B8FFAB")
s1.pack(fill='both', expand=True)

welcome = Label(s1, text="Bienvenido a Piplot", bg="#B8FFAB", font="Lucida 18 bold")
welcome.pack(pady=10)

tabla = ttk.Treeview(s1)
tabla['columns'] = ('Nombre', 'Num', 'Descrip', 'Inicio', 'Fin')

tabla.column("#0", width=0, stretch=NO)
tabla.column("Nombre", anchor=CENTER, width=80)
tabla.column("Num", anchor=CENTER, width=80)
tabla.column("Descrip", anchor=CENTER, width=80)
tabla.column("Inicio", anchor=CENTER, width=80)
tabla.column("Fin", anchor=CENTER, width=80)

tabla.heading("#0", text="", anchor=CENTER)
tabla.heading("Nombre", text="Nombre", anchor=CENTER)
tabla.heading("Num", text="Número", anchor=CENTER)
tabla.heading("Descrip", text="Descripción", anchor=CENTER)
tabla.heading("Inicio", text="Inicio", anchor=CENTER)
tabla.heading("Fin", text="Fin", anchor=CENTER)

tabla.insert(parent='',index='end',iid=0,text='',
values=('1','Física Ej.','Espejos Esféricos','3/10/23', '3/13/23'))
tabla.insert(parent='',index='end',iid=1,text='',
values=('2','Mate Ejercicios','Derivs. Parciales','3/9/23', '3/14/23'))
tabla.insert(parent='',index='end',iid=2,text='',
values=('3','Expo Ética','Valores','3/10', '3/14/23'))

tabla.pack(pady=5)

def agregar ():
    controltareas.agregar_tarea(entrada.get())
    
def ver():
    
    controltareas.ver_tarea()
    
entrada = Entry(s1)
entrada.place(x=150, y=300)
    
boton_agregar = Button(s1, text="Agregar",command=agregar)
boton_agregar.place(x=410, y=295)

boton_ver = Button(s1, text="Ver tarea",command=ver)
boton_ver.place(x=480,y=295)

ventanam.mainloop()