from tkinter import *
import os

# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "image/logo_utd.png")

ventana=Tk()
ventana.title("Imagenes Pillow")
ventana.geometry("500x500")

def  mensaje(tipo):
    lbl_resultado.config(text=f"{tipo}")

# Primer forma de agregar imagenes con TKinter

# PhotoImage
imagen=PhotoImage(file="P2\INTRODUCCION_TKINTER\Image\logo_utd.png")

# Mostrar imagen dentro de un Label y el boton
lbl_imagen=Label(ventana)
lbl_imagen.config(text="",
                  width=100, 
                  height=50,
                  image=imagen)
lbl_imagen.pack()

btn_imagen=Button(ventana)
btn_imagen.config(image=imagen,
                  width=100, 
                  height=50,
                  command=lambda: mensaje("Hola Python"))
btn_imagen.pack()

lbl_resultado=Label(ventana)
lbl_resultado.config(text="")
lbl_resultado.pack()

ventana.mainloop()