import tkinter as tk
def crear_menu_desplegable(self):
    barra_menu = tk.Menu(self.root)

    menu_principal = tk.Menu(barra_menu)
    barra_menu.add_cascade(label = 'Principal', menu=menu_principal)

    submenu = tk.Menu(menu_principal)
    menu_principal.add_cascade(label = 'Opciones', menu=submenu)

    submenu.add_command(label = 'Opción 1')
    submenu.add_command(label = 'Opción 2')