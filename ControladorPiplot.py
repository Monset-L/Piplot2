from tkinter import messagebox
import sqlite3

class controladorPBD:
    
    def __init__(self):
        pass
    #Preparamos la conexion a la base de datos para usarla cuando se ocupe
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/lenovo/Desktop/piplo2.db")
            print("Conexion exitosa")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def guardarUsuario(self,nom,desc,ini,fin):
        
        #1.- Llamar a la conexion
        conx = self.conexionBD()
        
        #2.- Revisar parametros vacios
        
        if(nom == "" or desc == "" or ini == "" or fin == ""):
            messagebox.showwarning("Aguas", "Revisa tu formulario")
            conx.close()
        else:
            #3.- Preparar datos y el querySQL
            cursor = conx.cursor()
            datos = (nom, desc, ini, fin)
            qrInsert="insert into Tareas(nomTarea,descTarea,fInicio,fFin) values(?,?,?,?)"
            
            #4.- Proceder a Insertar y cerramos la base de datos
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se guardo el usuario")
            
    def consultarTarea(self,num):
        #1.- Preparar la conexion
        
        conx= self.conexionBD()
        
        #2.- Verificar que el Id no este vacio
        
        if(num == ""):
            messagebox.showwarning("Error", "El numero de tarea esta vacio")
            conx.close()
        else:
            #3.- Proceder a buscar el usuario
            try:
                #4.- Preparar lo necesario para el select
                cursor=conx.cursor()
                sqlSelect = "select * from Tareas where Id="+num
                
                #5.- Ejecucion y guardado de la consulta
                
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error en la consulta")
                
    def consulta(self):
        #1.- Preparamos nuestra conexion a base de datos
        
        conx =self.conexionBD()
        try:
            #Preparamos el select
            cursor = conx.cursor()
            sqlSelect = "select * from Tareas"
            #Ejecutamos la consulta
            cursor.execute(sqlSelect)
            RSusuario = cursor.fetchall()
            conx.close()
                
            return RSusuario
                
        except sqlite3.OperationalError:
            print("Error en la consulta")