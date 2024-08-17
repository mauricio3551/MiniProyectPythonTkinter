import tkinter as tk
from tkinter import ttk
import pandas as pd
from funcionalidades.Boton_agregar import agregar_producto
from funcionalidades.Boton_eliminar import eliminar_producto
from funcionalidades.Reloj_simple import crear_reloj
 
class Table:
    def __init__(self, root):
        self.root = root

        # Leer datos de excel y convertirlos en un diccionario
        self.productos_precios = self.leer_excel()
        
        # Configurar el Treeview
        self.tree = ttk.Treeview(root, columns=("Producto", "Total"), show='headings')
        self.tree.heading("Producto", text="PRODUCTO", anchor="center")
        self.tree.heading("Total", text="TOTAL", anchor="center")
        self.tree.column("Producto", anchor=tk.CENTER)
        self.tree.column("Total", anchor=tk.CENTER)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Añadir scroll
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Llenar la tabla con el diccionario
        self.llenar_tabla()

        # Botones de acción
        frame_botones = tk.Frame(root)
        frame_botones.pack(side=tk.BOTTOM, padx=10, pady=10, anchor="center")

        reloj = crear_reloj(frame_botones)
        reloj.pack(pady=(0,100), padx=(20, 0))

        self.btn_agregar = tk.Button(frame_botones, text="Agregar Producto", command=lambda: agregar_producto(self))
        self.btn_agregar.pack(fill=tk.X)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar Producto", command=lambda: eliminar_producto(self))
        self.btn_eliminar.pack(fill=tk.X, pady=70)

    def llenar_tabla(self):
        for producto, total in  self.productos_precios.items():
            self.tree.insert("", tk.END, values=(producto, total))
    
    def leer_excel(self):
        excel_path = "datos/productos_precios.xlsx"

        # Con esto se lee el archivo xlsx
        df = pd.read_excel(excel_path)

        resultado = pd.Series(df.Precio.values, index=df.Producto).to_dict()

        return resultado
