import os
os.system('cls')
import pymongo
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

# Creacion de variables para poder conectar a MongoDB
MONGO_HOST = 'localhost'
MONGO_PUERTO = '27017'
MONGO_TIEMPO = 1000  # Tiempo en el que mongo se conecta a la base de datos

MONGO_URI = 'mongodb://' + MONGO_HOST + ':' + MONGO_PUERTO + '/'

# Conexion Base de datos y Acesso a la coleccion

MONGO_BD = "TiendaLibros"
MONGO_COLLECTION = "Libros"
cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS = MONGO_TIEMPO)
BaseDatos = cliente[MONGO_BD]
coleccion = BaseDatos[MONGO_COLLECTION]

# Definicion de nuestras funciones para que el programa se ejecute
def ListarDatos():
    try:
        registro = tabla.get_children()
        for registro in registro:
            tabla.delete(registro)
        # Acesso a documentos y obtencion de cada campo
        for documento in coleccion.find():
            tabla.insert('',0, text = documento["_id"],values = documento["Título"])
        cliente.close
    except pymongo.errors.SeverSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido" + errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectar a MongoDB"+errorConexion)

def AgregarDatos():
    if len(Título.get())!=0:
        try:
            documento={"Título":Título.get()}
            coleccion.insert_one(documento)
            Título.delete(0,END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    ListarDatos()

# Creacion de Ventana y tablas con un sistema de grilla en donde nuestra tabla estara en ciertas posiciones nuestra ventana
# Mas nombres de columnas

Ventana = Tk()
tabla = ttk.Treeview(Ventana, columns=2)
tabla.grid(row=1, column=0, columnspan=2)

tabla.heading("#0", text="ID")
tabla.heading("#1", text="Título")

# Creacion de casillas y boton

Label(Ventana, text="Título").grid(row=2,column=0)
Título = Entry(Ventana)
Título.grid(row=2,column=1)
Agregar = Button(Ventana, text = "Agregar", command = AgregarDatos, bg = "green", fg = "white")
Agregar.grid(row=3, columnspan=2)


ListarDatos()
Ventana.mainloop() # Tendra un ciclo principal teniendo control en nuestro programa