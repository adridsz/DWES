import tkinter as tk
from tkinter import ttk

def mostrar_yes_window():
    yes_root= tk.Tk()
    yes_root.title("Ventana del si")
    
    label = ttk.Label(yes_root, text="Si")
    label.pack(pady=10)
    
    yes_root.mainloop()