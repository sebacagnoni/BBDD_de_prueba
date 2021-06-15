
from tkinter import *
from tkinter import messagebox
import sqlite3


#Interfaz gráfica de la BBDD----------------------------------------#
#Root---------------------------------------------------------------#
raiz = Tk()
raiz.title("BBDD con Python")
raiz.resizable(0, 0)
raiz.iconbitmap("bbdd.ico")
raiz.geometry("500x450")
raiz.config(bg = "light blue")

#1 Frame-------------------------------------------------------------#

miFrame  = Frame()
miFrame.config(bg = "#A4E5F0")
miFrame.pack()
miFrame.config(width = "450", height = "450")
miFrame.config(bd = 10)

miId = StringVar()
miNick = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miContraseña = StringVar()

#2 Frame
FrameBotton = Frame()
FrameBotton.config(width = "450", height = "50")
FrameBotton.config(bg = "#A4E5F0", bd = 10)
FrameBotton.pack()

# Menu----------------------------------------------------------------#
# Funcionalidades de la Cascada y Botones CRUD
#BBDD

def crearBBDD():

        conectarBBDD=sqlite3.connect("Registro de Usuarios")

        miCursor=conectarBBDD.cursor()

        try:
           miCursor.execute('''
                CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NICK_DE_USUARIO VARCHAR(20),
                NOMBRE VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                COMENTARIOS VARCHAR(100))
                ''')
           messagebox.showinfo("BBDD", "BBDD creada con éxito")

        except:

           messagebox.showwarning("¡Atención!", "la BBDD ya existe")

def salirAplicacion():
    valor = messagebox.askquestion("Salir","Deseas salir de la aplicación?")
    if valor == "yes":
        raiz.destroy()
              

#Borrar

 
def limpiarCampos():
        miId.set("")
        miNick.set("")
        miNombre.set("")
        miApellido.set("")
        miContraseña.set("")
        comentarioText.delete(1.0, END)#1.0 primer carácter hasta END
        #Limpio comentario
    
#CRUD
#CREATE
def crear():
   conectarBBDD=sqlite3.connect("Registro de Usuarios")
   miCursor = conectarBBDD.cursor()
   miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"  
             +  miNick.get() +
       "','" + miNombre.get() + 
       "','" + miApellido.get() + 
       "','" + miContraseña.get() +
       "','" + comentarioText.get("1.0", END) + "')")
   conectarBBDD.commit()

   messagebox.showinfo("BBDD", "Registro insertado con éxito")
#READ
def leer():
        conectarBBDD=sqlite3.connect("Registro de Usuarios")
        miCursor = conectarBBDD.cursor()
        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = "+ miId.get())
        elUsuario = miCursor.fetchall() #devuelve array con todos los registros seleccionados
        for datos in elUsuario:
                miId.set(datos[0])
                miNick.set(datos[1])
                miNombre.set(datos[2])
                miApellido.set(datos[3])
                miContraseña.set(datos[4])
                comentarioText.insert(1.0, datos[5])
        conectarBBDD.commit()
 
#Modificar 
def actualizar():

        conectarBBDD=sqlite3.connect("Registro de Usuarios")
        miCursor = conectarBBDD.cursor()
        miCursor.execute("UPDATE DATOSUSUARIOS SET NICK_DE_USUARIO= '" + miNick.get() +
        "', NOMBRE ='" + miNombre.get() + 
        "', PASSWORD ='" + miContraseña.get() + 
        "', APELLIDO ='" + miApellido.get() +
        "', COMENTARIOS ='" + comentarioText.get("1.0", END) +
        "'  WHERE ID =" + miId.get())
        conectarBBDD.commit()

        messagebox.showinfo("BBDD", "Registro actualizado con éxito")

#Eliminar registro
def eliminar():
        conectarBBDD=sqlite3.connect("Registro de Usuarios")
        miCursor = conectarBBDD.cursor()
        miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID ="+ miId.get())
        conectarBBDD.commit()
        messagebox.showinfo("BBDD", "Registro borrado con éxito")

#Menu------------------#
barraMenu = Menu()
raiz.config(menu = barraMenu, width = 300, height = 300)

archivoBBDD = Menu(barraMenu, tearoff = 0)
archivoBBDD.add_command(label = "Conectar", command = crearBBDD)
archivoBBDD.add_command(label = "Salir", command = salirAplicacion )

archivoCRUD = Menu(barraMenu, tearoff = 0)
archivoCRUD.add_command(label = "Crear", command = crear)
archivoCRUD.add_command(label = "Leer", command = leer)
archivoCRUD.add_command(label = "Modificar", command = actualizar)
archivoCRUD.add_command(label = "Borrar", command = eliminar)

archivoBorrar = Menu(barraMenu, tearoff = 0)
archivoBorrar.add_command(label = "Borrar campos", command = limpiarCampos)


archivoAyuda = Menu(barraMenu, tearoff = 0)


archivoLicencia = Menu(barraMenu, tearoff = 0)
archivoLicencia.add_command(label = "Acerca de...")



#Menu Visual-------------#
barraMenu.add_cascade(label = "BBDD", menu = archivoBBDD)
barraMenu.add_cascade(label = "CRUD", menu = archivoCRUD)
barraMenu.add_cascade(label = "Borrar", menu = archivoBorrar)
barraMenu.add_cascade(label = "Ayuda", menu = archivoAyuda)
barraMenu.add_cascade(label = "Licencia", menu = archivoLicencia)




#Entradas y Labels----------------------------------------------#
#Labels-----------------------------------#

idLabel = Label(miFrame, text = "ID:", bg ="#A4E5F0", font = ("console",12))
idLabel.grid(row = 0, column = 0, sticky = "e")

nicknameLabel = Label(miFrame, text = "Usuario:", bg = "#A4E5F0", font = ("console",12))
nicknameLabel.grid(row = 1, column = 0, sticky = "e")

nameLabel = Label(miFrame, text = "Nombre:", bg = "#A4E5F0", font = ("console",12))
nameLabel.grid(row = 2, column = 0, sticky = "e")

lastNameLabel = Label(miFrame, text = "Apellido:", bg = "#A4E5F0", font = ("console",12))
lastNameLabel.grid(row = 3, column = 0, sticky = "e")

passLabel = Label(miFrame, text = "Contraseña:", bg = "#A4E5F0", font = ("console",12))
passLabel.grid(row = 4, column = 0, sticky = "e")

comentarioLabel= Label(miFrame, text = "Comentario", bg = "#A4E5F0", font = ("console", 12))
comentarioLabel.grid(row = 5, column = 0, sticky = "e")

#Entradas-----------------------------------#


entryId = Entry(miFrame, textvariable = miId)
entryId.grid(row = 0, column = 1)

entryNickname = Entry(miFrame, textvariable = miNick)
entryNickname.grid(row = 1, column = 1)

entryName = Entry(miFrame, textvariable = miNombre)
entryName.grid(row = 2, column = 1)

entryLastname = Entry(miFrame, textvariable = miApellido)
entryLastname.grid(row = 3, column = 1)

entryPass = Entry(miFrame, textvariable = miContraseña)
entryPass.grid(row = 4, column = 1)
entryPass.config(show = "*")

comentarioText = Text(miFrame, width = 15, height = 4 )
comentarioText.grid(row = 5, column = 1, sticky = "e", padx = 10, pady = 10)

#Scrollbar---------------#

scrollVert = Scrollbar(miFrame, command = comentarioText.yview)
scrollVert.grid(row = 5, column = 2, sticky = "nsew")
comentarioText.config(yscrollcommand = scrollVert.set)

#Botones----------------------------------------------#
#Funcionalidades del Boton




#Boton-------------------#
crearButton = Button(FrameBotton, text = "Crear", command = crear)
crearButton.grid(row = 0, column = 0, padx = 10, pady = 10)

leerButton = Button(FrameBotton, text = "Leer", command = leer)
leerButton.grid(row = 0, column = 1, padx = 10, pady = 10)

actualizarButton = Button(FrameBotton, text = "Modificar", command = actualizar)
actualizarButton.grid(row = 0, column = 2, padx = 10, pady = 10)

borrarButton = Button(FrameBotton, text = "Borrar", command = eliminar)
borrarButton.grid(row = 0, column = 3, padx = 10, pady = 10)

raiz.mainloop()