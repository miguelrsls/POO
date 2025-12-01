from tkinter import *

ventana=Tk()
ventana.title("Menu")
ventana.geometry("500x500")
ventana.resizable(False, False)

def mostrarEstado(tipo):
    resultado.config(text=f"{tipo}")

menuBar=Menu(ventana) # Crear menu
ventana.config(menu=menuBar) # Asignar menu a la ventana

archivoMenu=Menu(menuBar, tearoff=False) # Creamos boton Archivo en el menu
menuBar.add_cascade(label="Archivo", menu=archivoMenu) # Crea una cascada de opciones del boton
archivoMenu.add_command(label="Nuevo Archivo", command=lambda: mostrarEstado("Nuevo Archivo")) # Agrega el comando Nuevo Archivo en la cascada
archivoMenu.add_command(label="Guardar Archivo", command=lambda: mostrarEstado("Guardar Archivo")) # Agrega el comando Guardar Archivo en la cascada
archivoMenu.add_separator() # Agrega un separador en la cascada
archivoMenu.add_command(label="Salir", command=ventana.quit) # Agrega un comando que cierra la ventana

edicionMenu=Menu(menuBar, tearoff=False) # Creamos boton Edicion en el menu
menuBar.add_cascade(label="Edicion", menu=edicionMenu) # Crea una cascada de opciones del boton
edicionMenu.add_command(label="Copiar", command=lambda: mostrarEstado("Copiar")) # Agrega el comando Copiar en la cascada
edicionMenu.add_command(label="Recortar", command=lambda: mostrarEstado("Recortar")) # Agrega el comando Recortar en la cascada
edicionMenu.add_separator() # Agrega un separador en la cascada
edicionMenu.add_command(label="Salir", command=ventana.quit) # Agrega un comando que cierra la ventana

resultado=Label(ventana)
resultado.config(text="")
resultado.pack()

ventana.mainloop()