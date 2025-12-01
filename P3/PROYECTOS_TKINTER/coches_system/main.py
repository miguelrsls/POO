"""
commit_01_12_25

1) Implementacion de MVC
2) POO
3) Interfaces:
    3.1 menu_principal()
    3.2 menu_acciones()
    3.3 insertar_autos()
    3.4 consultar_autos()
    3.5 cambiar_autos()
    3.6 borrar_autos()
"""

from tkinter import *
from view import vista

class App:
    def __init__(self, ventana):
        view=vista.Interfaces(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()