import tkinter as tk
from tkinter import ttk
from cell import Cell
def mostrar_detalles(cell):
    root = tk.Toplevel()
    root.title(cell.title)
    mostrarl = ttk.Label(root, image = cell.imageTk)
    mostrarl.pack()
    mostrarl2 = ttk.Label(root, text = cell.description)
    mostrarl2.pack()
    root.mainloop()