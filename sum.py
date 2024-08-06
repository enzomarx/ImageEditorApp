import tkinter as tk
from tkinter import ttk

# definições padrões tkinter window
root = tk.Tk() # Raiz

root.iconbitmap(r'C:\Users\PC\Downloads\iconteste.ico')
root.title('Tkinter Window Demo') # Titulo

# Geometria
root.geometry('800x400+300+0') # Geometria
root.resizable(True, True) # Redimensionar
root.wm_minsize(500, 200) # Tamanho minimo da janela
root.wm_maxsize(1366, 768) # Tamanho máximo da janela

# Atributos
root.attributes('-alpha', 0.8) # Opacidade/Invisibilidade __Atributo__
root.attributes('-topmost', 1) # Janela sempre no topo __Atribbuto__

# Label
tk.Label(root, text='Classic Label').pack() # Criar Label clássica
ttk.Label(root, text='Themed Label').pack() # Criar Label temática

# Widgets
## Button

The_button = ttk.Button(root, text='Original Image')











root.mainloop() # Loop

