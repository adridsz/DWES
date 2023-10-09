import tkinter as tk
from tkinter import ttk

def mostrar_no_window():
    no_root= tk.Tk()
    no_root.title("Ventana del no")
    
    label = ttk.Label(no_root, text="No")
    label.pack(pady=10)
    
    no_root.mainloop()