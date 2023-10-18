import threading
import requests
import tkinter as tk
from window import MainWindow
from tkinter import messagebox

class loadingWindow:
    
    def __init__(self, root):
        self.finished = False
        self.json_data = []
        self.root = root;
        self.root.title("CARGANDO...") # Aqui le damos el titulo a la ventana de carga
        self.root.geometry("170x120") # Aqui le damos el tamaño a la ventana de carga
        self.root.resizable(False, False) # Aqui indicamos que no se puede estirar ni ampliar la ventana de carga
        
        self.label = tk.Label(self.root, text="Cargando datos...", font=("arial", 14)) # Aqui mostramos un texto dentro de la ventana
        self.label.pack(side=tk.TOP, pady=10)
# De aqui para aabajo hacemos el circulo de carga
        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0 
        
        self.draw_progress_circle(self.progress)
        
        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        if self.thread.is_alive():
            self.check_thread()

    def draw_progress_circle(self, progress): # Aqui mostramos el circulo de carga
        self.canvas.delete("progress")
        angle = int(360 * (progress/100))

        self.canvas.create_arc(10, 10, 35, 35, start = 0, extent=angle, tags="progress", outline='green', width=5, style=tk.ARC)
    
    def update_progress_circle(self): # Aqui hacemos que el circulo de carga gire
        if self.progress < 100:
            self.progress+=10
        else:
            self.progress=0
        
        self.draw_progress_circle(self.progress)
        self.root.after(200, self.update_progress_circle)
    
    def fetch_json_data(self): # Aqui descargamos el json
        response = requests.get("https://raw.githubusercontent.com/adridsz/DWES/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished=True
    
    def check_thread(self): # Aqui comprobamos que la descarga fuera correcta
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

def launch_main_window(json_data): # Aqui lanzamos la ventana main
    root = tk.Tk()
    barra_menu =tk.Menu() # Aqui creamos el menu de ayuda
    menu_ayuda = tk.Menu(barra_menu, tearoff=False)
    menu_ayuda.add_command( # Aqui cremos el desplegable de acerca de
        label="Acerca de",
        command=acerca_de
    )
    barra_menu.add_cascade(menu=menu_ayuda, label="Ayuda")
    root.config(menu=barra_menu)
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) /2 # Aqui centramos la imagern
    y = (root.winfo_screenheight() - root.winfo_reqheight()) /2
    root.geometry(f"+{int(x)}+{int(y)}") # Aqui terminamos de centrarla
    app = MainWindow(root, json_data) #Aqui lanzamos la ventana principal
    root.mainloop()
    
def acerca_de():
    messagebox.showinfo(message="Acerca del desarrollador", title="Acerca de")