import tkinter as tk
from tkinter import simpledialog, messagebox

def eliminar_producto(self):
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion)
            producto = item['values'][0]
            del  self.productos_precios[producto]
            self.tree.delete(seleccion)
        else:
            messagebox.showerror("Error", "Debe seleccionar un producto para eliminar.")