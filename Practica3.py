from tkinter import *
from tkinter import messagebox
import sqlite3

ventana = Tk()
ventana.title("BBDD")


# ------------------Funciones-------------------
def conexionBBDD():
    conexion = sqlite3.connect("Usuarios")
    pointer = conexion.cursor()

    try:
        pointer.execute('''
        CREATE TABLE DATOS_USUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        APELLIDO_USUARIO VARCHAR(50),
        PASSWORD_USUARIO VARCHAR(20))
        ''')

        messagebox.showinfo("BBDD", "Base de datos creada con éxito")

    except:
        messagebox.showwarning("BBDD", "La base de datos ya existe")


def salirAplicacion():
    opcion = messagebox.askquestion("SalirBBDD", "¿Desea salir de la aplicación?")

    if opcion == "yes":
        ventana.destroy()


def limpiarCampos():
    id.set("")
    nombre.set("")
    apellido.set("")
    password.set("")


def crear():
    conexion = sqlite3.connect("Usuarios")
    pointer = conexion.cursor()

    datos = nombre.get(), apellido.get(), password.get()

    '''pointer.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + nombre.get() +
                    "','" + apellido.get() +
                    "','" + password.get() + "')")'''

    pointer.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, ?, ?, ?)", datos)

    conexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")


def leer():
    conexion = sqlite3.connect("Usuarios")
    pointer = conexion.cursor()

    pointer.execute("SELECT * FROM DATOS_USUARIOS WHERE ID = " + id.get())

    mostrarUsuario = pointer.fetchall()

    for usuario in mostrarUsuario:
        id.set(usuario[0])
        nombre.set(usuario[1])
        apellido.set(usuario[2])
        password.set((usuario[3]))

    conexion.commit()


def actualizar():
    conexion = sqlite3.connect("Usuarios")
    pointer = conexion.cursor()

    datos = nombre.get(), apellido.get(), password.get()

    '''pointer.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = '" + nombre.get() +
                    "', APELLIDO_USUARIO = '" + apellido.get() +
                    "', PASSWORD_USUARIO = '" + password.get() +
                    "' WHERE ID = " + id.get())'''

    pointer.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = ?, APELLIDO_USUARIO = ?, PASSWORD_USUARIO = ?" +
                    "WHERE ID = " + id.get(), datos)

    conexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def eliminar():
    conexion = sqlite3.connect("Usuarios")
    pointer = conexion.cursor()

    pointer.execute("DELETE FROM DATOS_USUARIOS WHERE ID = " + id.get())

    opcion = messagebox.askquestion("Eliminar registro", "¿Estás seguro que deseas eliminar este registro? \n "
                                                         "Esta acción no se puede deshacer")

    if opcion == "yes":
        conexion.commit()
        messagebox.showinfo("BBDD", "Registro eliminado con éxito")


# -------------------------Widgets-------------------------
menu = Menu(ventana)
ventana.config(menu=menu, width=300, height=300)

bdMenu = Menu(menu, tearoff=0)
bdMenu.add_command(label="Conectar", command=conexionBBDD)
bdMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(menu, tearoff=0)
borrarMenu.add_command(label="Borrar datos", command=limpiarCampos)

ayudaMenu = Menu(menu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

menu.add_cascade(label="BBDD", menu=bdMenu)
menu.add_cascade(label="Borrar", menu=borrarMenu)
menu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ------------------ Comienzo de campos ----------------

frame = Frame(ventana)
frame.pack()

# Etiquetas
etiquetaID = Label(frame, text="ID")
etiquetaID.grid(row=0, column=0, padx=10, pady=10)

etiquetaNombre = Label(frame, text="Nombre")
etiquetaNombre.grid(row=1, column="0", padx=10, pady=10)

etiquetaApellido = Label(frame, text="Apellido")
etiquetaApellido.grid(row=2, column=0, padx=10, pady=10)

etiquetaPassword = Label(frame, text="Password")
etiquetaPassword.grid(row=3, column=0, padx=10, pady=10)

# Campos de texto

id = StringVar()
nombre = StringVar()
apellido = StringVar()
password = StringVar()

campoID = Entry(frame, textvariable=id)
campoID.grid(row=0, column=1, padx=10, pady=10)

campoNombre = Entry(frame, textvariable=nombre)
campoNombre.grid(row=1, column=1, padx=10, pady=10)

campoApellido = Entry(frame, textvariable=apellido)
campoApellido.grid(row=2, column=1, padx=10, pady=10)

campoPassword = Entry(frame, textvariable=password)
campoPassword.grid(row=3, column=1, padx=10, pady=10)
campoPassword.config(show="*")

# Botones
frameButtons = Frame(ventana)
frameButtons.pack()

botonCrear = Button(frameButtons, text="Crear", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(frameButtons, text="Leer", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(frameButtons, text="Actualizar", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar = Button(frameButtons, text="Eliminar", command=eliminar)
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

ventana.mainloop()
