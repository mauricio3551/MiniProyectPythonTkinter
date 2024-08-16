import tkinter as tk
from tkinter import ttk, messagebox
from funcionalidades.Boton_agregar import agregar_producto
from funcionalidades.Boton_eliminar import eliminar_producto
from funcionalidades.Reloj_simple import crear_reloj
 
class Table:
    def __init__(self, root):
        # Diccionario hardcodeado con productos y precios
        self.productos_precios = {
            "Tomate": "$2.00",
            "Papa": "$1.50",
            "Zanahoria": "$1.20",
            "Lechuga": "$1.00",
            "Pepino": "$1.30",
            "Cebolla": "$1.10",
            "Ajo": "$0.90",
            "Apio": "$1.70",
            "Pimiento": "$2.50",
            "Calabacín": "$1.80",
            "Berenjena": "$2.10",
            "Brócoli": "$2.20",
            "Coliflor": "$2.30",
            "Espinaca": "$1.60",
            "Rábano": "$1.00",
            "Repollo": "$1.80",
            "Pepinillo": "$1.40",
            "Chayote": "$1.70",
            "Espárrago": "$2.80",
            "Nabo": "$1.30",
            "Remolacha": "$1.90",
            "Guisante": "$2.00",
            "Alcachofa": "$3.00",
            "Calabaza": "$2.40",
            "Champiñón": "$3.20",
            "Puerro": "$2.10",
            "Cilantro": "$0.80",
            "Perejil": "$0.70",
            "Albahaca": "$0.90",
            "Menta": "$0.85",
            "Laurel": "$0.75",
            "Jengibre": "$3.50",
            "Cúrcuma": "$3.20",
            "Frijol": "$1.90",
            "Lenteja": "$2.00",
            "Quinoa": "$3.00",
            "Arroz": "$1.80",
            "Maíz": "$2.00",
            "Aguacate": "$2.70",
            "Mango": "$2.20",
            "Plátano": "$1.50",
            "Fresa": "$3.00",
            "Manzana": "$2.50",
            "Naranja": "$2.00",
            "Mandarina": "$1.80",
            "Piña": "$3.00",
            "Cereza": "$4.00",
            "Uva": "$3.50",
            "Kiwi": "$2.80",
        }
        self.root = root
        
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
