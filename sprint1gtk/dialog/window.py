from tkinter import Tk, ttk, Button
from yes_window import mostrar_yes_window
from no_window import mostrar_no_window

class MainWindow:
    def on_button_click(self, root):
        pass

    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        
        self.label = ttk.Label(self.frame, text="Si o no")
        self.label.pack()
        
        self.button = ttk.Button(self.frame, text="Si", command=mostrar_yes_window)
        self.button.pack(side="left")
        
        self.button1 = ttk.Button(self.frame, text="No", command=mostrar_no_window)
        self.button1.pack(side="right")