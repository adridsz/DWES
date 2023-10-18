import requests
import threading
from PIL import ImageTk, Image
from io import BytesIO

class Cell:
    def __init__(self,nombre, url, descripcion):
        self.nombre = nombre # Aqui almacenamos el nombre de la imagen
        self.url = url # De aqui para abajo descargamos y cargamos la imagen
        response = requests.get(self.url) 
        img_data = Image.open(BytesIO(response.content))
        self.image_tk = ImageTk.PhotoImage(img_data) # Aqui termina el proceso de la imagen
        self.descripcion = descripcion # Aqui almacenamos la descripcion de la imagen
        #rescalada = (Image.open(BytesIO(response.content))).resize((100, 100), Image.Resampling.LANCZOS)