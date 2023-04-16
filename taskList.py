from tkinter import *
from tkinter import ttk
from ControladorPiplot import *
from tkinter import messagebox

ventanam = Tk() 
ventanam.title("Piplot")
ventanam.geometry("700x400")

def vAgregar():
    
    def showExito():
        num = NoT2.get()
        nom = nombre2.get()
        desc = Descripcion2.get()
        finicio = FI2.get()
        ffinal = FF2.get()
        tabla.insert(parent='',index='end',iid=num,text='',
        values=(num,nom,desc,finicio, ffinal))
        msg= messagebox.showinfo("Exito", "Tu ingreso se agregó exitosamente")
        
    ventana = Toplevel()
    ventana.title("Tareas")
    ventana.geometry("600x400")
    
    def vVolver():
        ventana.withdraw() 
    
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

    botonRegistrar = Button(seccion1, text="Guardar", fg="black", bg="White", font="Arial 12", command= showExito)
    botonRegistrar.place(x=260, y=300)
    
    btnRegresar = Button(seccion1, text="Regresar", fg="Black", bg="white", font="Arial 12", command= vVolver)
    btnRegresar.place(x=380, y=300)

s1 = Frame(ventanam, bg="#B8FFAB")
s1.pack(fill='both', expand=True)

welcome = Label(s1, text="Bienvenido a Piplot", bg="#B8FFAB", font="Lucida 18 bold")
welcome.pack(pady=10)

tabla = ttk.Treeview(s1)
tabla['columns'] = ('Num', 'Nombre', 'Descrip', 'Inicio', 'Fin')

tabla.column("#0", width=0, stretch=NO)
tabla.column("Num", anchor=CENTER, width=80)
tabla.column("Nombre", anchor=CENTER, width=80)
tabla.column("Descrip", anchor=CENTER, width=80)
tabla.column("Inicio", anchor=CENTER, width=80)
tabla.column("Fin", anchor=CENTER, width=80)

tabla.heading("#0", text="", anchor=CENTER)
tabla.heading("Num", text="Número", anchor=CENTER)
tabla.heading("Nombre", text="Nombre", anchor=CENTER)
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
    
entrada = Entry(s1)
entrada.place(x=150, y=300)
    
boton_agregar = Button(s1, text="Agregar",command=vAgregar)
boton_agregar.place(x=410, y=295)

boton_ver = Button(s1, text="Ver tarea")
boton_ver.place(x=480,y=295)

ventanam.mainloop()