import threading
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import Tk, ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import mostrar_detalles

def load_image_from_url(self, url): # Aqui hacemos la petición para descargar la imagen
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content))
    return ImageTk.PhotoImage(img_data)

class MainWindow():
    
    def __init__(self, root, json_data):
        #Titulo ventana
        root.title("MainWindow") # Le damos el titulo a la ventana principal
        
        for paisaje in json_data: # Bucle para cargar las imagenes
            label = ttk.Label(root, image= load_image_from_url(paisaje.get("image_url")), text= paisaje.get("description"))
            label.grid(row=paisaje, column=0)