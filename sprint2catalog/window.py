from tkinter import Tk, ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import mostrar_detalles

class MainWindow():
    
    def __init__(self, root):
        #Titulo ventana
        root.title("MainWindow")
        
        
        #Aqui defino las imagenes
        self.cells = [
            Cell("Paisaje 1", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\1.jpg", "Esta es una foto del eje cafetero de Colombia, esto es una región la cual cuenta con pueblos coloridos y estos sobreviven a base del comercio del cafe"),
            Cell("Paisaje 2", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\2.jpg", "Esto es una foto del cabo de San Juan, esto se encuentra dentro del parque nacional de Tayrona. Aqui aun subsisten pueblos indigenas a pesar de ser una zona tan bonita para el turismo"),
            Cell("Paisaje 3", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\3.jpg", "Esta es otra foto del eje cafetero de Colombia, esto es una región la cual cuenta con pueblos coloridos y estos sobreviven a base del comercio del cafe"),
            Cell("Paisaje 4", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\4.jpg", "Esta es una foto del eje cafetero de Colombia, esto es una región la cual cuenta con pueblos coloridos y estos sobreviven a base del comercio del cafe"),
            Cell("Paisaje 5", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\5.jpg", "Esta es una foto de Cartajena de Indias, es un distrito cultural y turistico. Es patrimonio nacional y de la Humanidad")
        ]
        
        #Bucle para ver las imagenes
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.imageTk, text= cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda= cell: mostrar_detalles(celda))