"""
commit_04_12_25

1) Controlador:

    1.1 menu_principal()
    1.2 menu_acciones()
    1.3 insertar_autos()
    1.4 consultar_autos()
    1.5 cambiar_autos()
    1.6 borrar_autos()
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