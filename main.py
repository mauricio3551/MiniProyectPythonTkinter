import tkinter as tk
from funcionalidades.Lista_de_tareas import crear_lista_De_tareas
from funcionalidades.Tabla_verduleria import Table

ventana = tk.Tk()
ventana.geometry("1024x480")

#Frame superior para colocar los botones
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear el menú principal
menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Principal', menu=menu_principal)

# Submenú de opciones
submenu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label='Opciones', menu=submenu)
menu_principal.add_cascade(label="Salir", command=ventana.quit)

# Añadir opciones al submenú
submenu.add_command(label="Lista de Tareas", command=crear_lista_De_tareas)
submenu.add_separator()

# Frame derecho para la tabla de verduleria
frame_tabla = tk.Frame(ventana, height=30)
frame_tabla.pack(side=tk.RIGHT, fill=tk.BOTH, pady=15)

# Crear la tabla de verdulería en el frame inferior
tabla = Table(frame_tabla)

# Frame izquierdo para la imagen de verduleria
frame_izquierdo = tk.Frame(ventana, height=30)
frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, pady=15, padx=15)

frame_imagen = tk.Frame(frame_izquierdo)
frame_imagen.pack(side=tk.TOP, fill=tk.BOTH)

ruta_imagen = "imagenes/imagen_verduras_costado.png"

imagen = tk.PhotoImage(file=ruta_imagen)
label_imagen = tk.Label(frame_imagen, image=imagen)
label_imagen.pack(side=tk.TOP)
label_imagen.image = imagen


ventana.mainloop()

