import tkinter as tk
import pandas as pd
from tkinter import messagebox

def eliminar_producto(self):
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion)
            producto = item['values'][0]
            del  self.productos_precios[producto]
            self.tree.delete(seleccion)

             # Actualizar el archivo Excel
            df = pd.DataFrame(list(self.productos_precios.items()), columns=["Producto", "Precio"])
            df.to_excel("datos/productos_precios.xlsx", index=False)

        else:
            messagebox.showerror("Error", "Debe seleccionar un producto para eliminar.")