from tkinter import Tk
from window import MainWindow
from load_window import loadingWindow

if __name__ == "__main__": # Aqui arrancamos la pantalla de carga
    loadingWindow
    root=Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) /2 # Aqui centramos la imagen
    y = (root.winfo_screenheight() - root.winfo_reqheight()) /2
    root.geometry(f"+{int(x)}+{int(y)}") # Aqui terminamos de centrarla
    app = loadingWindow(root)
    root.mainloop()     