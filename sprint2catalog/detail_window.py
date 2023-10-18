import tkinter as tk
from tkinter import ttk
from cell import Cell
def mostrar_detalles(cell): # Aqui creamos una ventana con los detalles de la imagen seleccionada
    root = tk.Toplevel()
    root.title(cell.nombre)
    mostrarl = ttk.Label(root, image = cell.image_tk)
    mostrarl.pack()
    mostrarl2 = ttk.Label(root, text = cell.descripcion)
    mostrarl2.pack()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) /2 # Aqui centramos la imagern
    y = (root.winfo_screenheight() - root.winfo_reqheight()) /2
    root.geometry(f"+{int(x)}+{int(y)}") # Aqui terminamos de centrarla
    root.mainloop() # Aqui lanzamos la ventana detallada