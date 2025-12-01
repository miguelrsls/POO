from tkinter import *

ventana=Tk()
ventana.title("List Box")
ventana.geometry("500x500")
ventana.resizable(False, False)

def mostrarEstado():
    seleccion=lista.get(lista.curselection())
    resultado.config(text=f"Seleccionaste: {seleccion}")

lista=Listbox(ventana)
lista.config(width=10,
             height=5,
             selectmode='single')
lista.pack()

opciones=['Amarillo', 'Rojo', 'Azul', 'Morado']
for i in opciones:
    lista.insert(END, i)

boton=Button(ventana)
boton.config(text="Mostrar seleccion del usuario", 
             command=mostrarEstado)
boton.pack()

resultado=Label(ventana)
resultado.config(text="")
resultado.pack()

ventana.mainloop()