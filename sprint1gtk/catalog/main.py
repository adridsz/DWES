from tkinter import Tk
from window import MainWindow
from load_window import loadingWindow

if __name__ == "__main__":
    loadingWindow
    root=Tk()
    app = loadingWindow(root)
    root.mainloop() 