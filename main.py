import tkinter as tk
from funcionalidades.menu_desplegable import crear_menu_desplegable
from funcionalidades.Lista_de_tareas import crear_lista_De_tareas
from funcionalidades.Barra_desplazamiento import crear_barra_desplazamiento
from funcionalidades.Reloj_simple import crear_reloj
from funcionalidades.Tabla_verduleria import Table

ventana = tk.Tk()
ventana.geometry("1024x480")

#Frame superior para colocar los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(side=tk.TOP, fill=tk.X, expand=False)

#Boton para el Mini Proyecto de Lista de Tareas
boton1 = tk.Button(frame_botones, text = "Lista de Tareas", command = crear_lista_De_tareas)
boton1.pack(side=tk.LEFT, padx=10, pady=10)

#Boton para el Mini Proyecto de Menu Desplegable
boton1 = tk.Button(frame_botones, text = "Menu desplegable", command = crear_menu_desplegable)
boton1.pack(side=tk.LEFT, padx=10, pady=10)

#Boton para el Mini Proyecto de Barra de Desplazamiento
boton1 = tk.Button(frame_botones, text = "Barra de desplazamiento", command = crear_barra_desplazamiento)
boton1.pack(side=tk.LEFT, padx=10, pady=10)

#Boton para el Mini Proyecto de Reloj
boton1 = tk.Button(frame_botones, text = "Reloj", command = crear_reloj)
boton1.pack(side=tk.LEFT, padx=10, pady=10)

# Frame inferior para la tabla de verduleria
frame_tabla = tk.Frame(ventana, height=30)
frame_tabla.pack(side=tk.RIGHT, fill=tk.BOTH, pady=15)

# Crear la tabla de verdulería en el frame inferior
tabla = Table(frame_tabla)

ventana.mainloop()

