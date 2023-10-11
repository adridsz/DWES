from tkinter import Tk, ttk, messagebox
import tkinter as tk
from cell import Cell

class MainWindow():
    
    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda " + cell.title
        messagebox.showinfo("Información" + message)
    
    def __init__(self, root):
        root.title("MainWindow")
        
        self.cells = [
            Cell("Paisaje 1", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\1.jpg"),
            Cell("Paisaje 2", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\2.jpg"),
            Cell("Paisaje 3", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\3.jpg"),
            Cell("Paisaje 4", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\4.jpg"),
            Cell("Paisaje 5", "C:\\msys64\\home\\Alumno\\DWES\\sprint1gtk\\catalog\\data\\unedited\\5.jpg")
        ]
        
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.imageTk, text= cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("Button-1", lambda event, cell= cell: self.on_button_clicked)