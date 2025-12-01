from tkinter import *

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")
ventana.resizable(False, False)

def mostrarEstado():
    resultado.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

valor=IntVar()
scale=Scale(ventana)
scale.config(from_=0, 
             to=100, 
             orient="horizontal",
             variable=valor)
scale.pack()

boton=Button(ventana)
boton.config(text="Mostrar Valor",
             command=mostrarEstado)
boton.pack()

resultado=Label(ventana)
resultado.config(text="")
resultado.pack()

ventana.mainloop()