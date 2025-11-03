from tkinter import *

ventana=Tk()
ventana.title("Marcos o Frames en Tkinter")
ventana.geometry("800x600")
# ventana.resizable(False, False) # No pueda modificarse el tamaño de la ventana.

marco1=Frame(ventana, 
             width=400, 
             height=200, 
             bg="#bc057f", 
             relief=SOLID,
             border=2)
marco1.pack_propagate(False) # Evitar que se modifique el estilo del marco.
marco1.pack(pady=200) # Es importante para que se dibuje o muestre el objeto dentro de la ventana.

marco2=Frame(marco1, 
             width=300, 
             height=100, 
             bg="#78139e", 
             relief=SOLID,
             border=2)
marco2.pack(pady=50)

ventana.mainloop()