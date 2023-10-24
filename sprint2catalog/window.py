import threading
import requests
from PIL import Image, ImageTk
from tkinter import Canvas, Frame, Label, Scrollbar, Tk, ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import mostrar_detalles

class MainWindow():
    cells = []
    
    def __init__(self, root, json_data):
        root.title("MainWindow")
        for paisaje in json_data:
            nombre = paisaje.get("name")
            descripcion = paisaje.get("description")
            url = paisaje.get("image_url")
            cell = Cell(nombre, url, descripcion)
            self.cells.append(cell)
        
        # SCROLLBAR
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview, width=15)
        
        # Creamos el frame del scroll scroll
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        #Configuramos el scroll en el canvas
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        for i, cell in enumerate(self.cells):
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(pady=10)
            label = tk.Label(frame, image=cell.image_tk, text=cell.nombre, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda= cell: mostrar_detalles(celda))
        
        #Configuramos la posicion del scroll en la ventana
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)