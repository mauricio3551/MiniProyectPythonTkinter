import tkinter as tk
from tkinter import simpledialog, messagebox

def agregar_producto(self):
        # Crear una nueva ventana para añadir producto
        self.nueva_ventana = tk.Toplevel(self.root)
        self.nueva_ventana.title("Agregar Producto")

        self.nueva_ventana.geometry("300x150")

        tk.Label(self.nueva_ventana, text="Producto").grid(row=0, column=0, padx=10, pady=10)
        self.entrada_producto = tk.Entry(self.nueva_ventana)
        self.entrada_producto.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.nueva_ventana, text="Total").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_total = tk.Entry(self.nueva_ventana)
        self.entrada_total.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.nueva_ventana, text="Agregar", command=lambda:confirmar_agregar(self)).grid(row=2, columnspan=2, pady=5)

def confirmar_agregar(self):
        producto = self.entrada_producto.get()
        total = self.entrada_total.get()

        if producto and total.isdigit():
            self.productos_precios[producto] = int(total)
            self.tree.insert("", tk.END, values=(producto, f"${total}"))
            self.nueva_ventana.destroy()
        else:
            messagebox.showerror("Error", "Debe ingresar un nombre de producto válido y un total numérico.")