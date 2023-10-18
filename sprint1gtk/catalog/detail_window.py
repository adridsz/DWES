import tkinter as tk
from tkinter import ttk
from cell import Cell
def mostrar_detalles(cell): # Aqui creamis una ventana con los detalles de la imagen seleccionada
    root = tk.Toplevel()
    root.title(cell.nombre)
    mostrarl = ttk.Label(root, image = cell.image_tk)
    mostrarl.pack()
    mostrarl2 = ttk.Label(root, text = cell.descripcion)
    mostrarl2.pack()
    root.mainloop()