import threading
import requests
from PIL import Image, ImageTk
from tkinter import Tk, ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import mostrar_detalles

class MainWindow():
    cells = [] # Aqui creamos una lista que rellenaremos con los datos del json
    def __init__(self, root, json_data):
        #Titulo ventana
        root.title("MainWindow") # Le damos el titulo a la ventana principal
        
        for paisaje in json_data: # Con este bucle metemos los datos del json en la lista cells
            nombre = paisaje.get("name")
            descripcion = paisaje.get("description")
            url = paisaje.get("image_url")
            cell = Cell(nombre, url, descripcion)
            self.cells.append(cell)
        
        #Bucle para ver las imagenes
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text= cell.nombre, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda= cell: mostrar_detalles(celda))