"""
commit_05_12_25

Version Final
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