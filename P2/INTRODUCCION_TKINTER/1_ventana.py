"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en Python para escritorio.
"""
from tkinter import *

ventana=Tk()
ventana.title("Mi primer App con Tkinter")
ventana.geometry("800x600")

ventana.mainloop() # Metodo que permite tener la ventana abierta todo el tiempo que dure la app activa.