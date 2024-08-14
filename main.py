import tkinter
from menu_desplegable import crear_menu_desplegable
from Lista_de_tareas import crear_lista_De_tareas
from Barra_desplazamiento import crear_barra_desplazamiento
from Reloj_simple import crear_reloj

ventana = tkinter.Tk()
ventana.geometry("1024x480")

#Definimos las funciones
def saludo():
    print("Hola")

#Boton para el Mini Proyecto de Lista de Tareas
boton1 = tkinter.Button(ventana, text = "Lista de Tareas", command = crear_lista_De_tareas)
boton1.pack()

#Boton para el Mini Proyecto de Menu Desplegable
boton1 = tkinter.Button(ventana, text = "Lista de Tareas", command = crear_lista_De_tareas)
boton1.pack()

#Boton para el Mini Proyecto de Barra de Desplazamiento
boton1 = tkinter.Button(ventana, text = "Lista de Tareas", command = crear_lista_De_tareas)
boton1.pack()

#Boton para el Mini Proyecto de
boton1 = tkinter.Button(ventana, text = "Lista de Tareas", command = crear_lista_De_tareas)
boton1.pack()


ventana.mainloop()

