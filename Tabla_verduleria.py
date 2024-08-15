import tkinter as tk
 
class Table:
    def __init__(self, root):
        # Diccionario hardcodeado con productos y precios
        productos_precios = {
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
        # Crear un canvas y un scrollbar
        canvas = tk.Canvas(root)
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un frame dentro del canvas
        frame_tabla = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_tabla, anchor='center')

        # Crear el encabezado de la tabla
        tk.Label(frame_tabla, text="Producto", borderwidth=1, relief='solid', width=60, bg="lightgrey").grid(row=0, column=0, sticky="nsew")
        tk.Label(frame_tabla, text="Precio", borderwidth=1, relief='solid', width=40, bg="lightgrey").grid(row=0, column=1, sticky="nsew")

        # Crear las filas de la tabla con productos y precios
        for i, (producto, precio) in enumerate(productos_precios.items(), start=1):
            tk.Label(frame_tabla, text=producto,borderwidth=1,relief="sunken").grid(row=i, column=0, sticky="nsew")
            tk.Label(frame_tabla, text=precio,borderwidth=1,relief="sunken").grid(row=i, column=1, sticky="nsew")

        # Ajustar el tamaño del canvas
        frame_tabla.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        # Expandir columnas para ocupar todo el espacio disponible
        root.grid_columnconfigure(0, weight=10)
        root.grid_columnconfigure(1, weight=5)

        # Expandir filas para ocupar todo el espacio disponible
        for i in range(len(productos_precios) + 1):
            root.grid_rowconfigure(i, weight=1)
        
        # Configurar el scrollbar para que empiece desde arriba
        canvas.yview_moveto(0)