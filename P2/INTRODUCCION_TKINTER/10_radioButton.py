from tkinter import *

ventana=Tk()
ventana.title("Radio Button")
ventana.geometry("500x500")
ventana.resizable(False, False)

def mostrarEstado():
    lbl_seleccion.config(text=f"Opcion seleccionada: {opcion.get()}")

# Botones Radio
opcion=StringVar()

radioBoton1=Radiobutton(ventana)
radioBoton1.config(text="Opcion 1",
                  variable=opcion,
                  value="Opcion1")
radioBoton1.pack()

radioBoton2=Radiobutton(ventana)
radioBoton2.config(text="Opcion 2",
                  variable=opcion,
                  value="Opcion2")
radioBoton2.pack()

radioBoton3=Radiobutton(ventana)
radioBoton3.config(text="Opcion 3",
                  variable=opcion,
                  value="Opcion3")
radioBoton3.pack()

# Boton para confirmar.
btn_seleccion=Button(ventana)
btn_seleccion.config(text="Mostrar Seleccion",
                     command=mostrarEstado)
btn_seleccion.pack(pady=10)

# Texto notificaciones.
lbl_seleccion=Label(ventana)
lbl_seleccion.config(text="")
lbl_seleccion.pack(pady=10)

ventana.mainloop()