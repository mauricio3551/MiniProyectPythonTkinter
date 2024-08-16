
import tkinter as tk
import time

def crear_reloj(parent):
    reloj = tk.Label(parent, font=('Arial', 12), background='black', foreground='white')
    reloj.pack(side=tk.TOP, anchor='nw', padx=10, pady=10)

    def actualizar_reloj():
        tiempo_actual = time.strftime('%H:%M:%S')
        reloj.config(text=tiempo_actual)
        reloj.after(1000, actualizar_reloj) # Actualiza cada segundo

    actualizar_reloj()
    return reloj