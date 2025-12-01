from tkinter import *

ventana=Tk()
ventana.title("Check Button")
ventana.geometry("500x500")
ventana.resizable(False, False)

def mostrarEstado():
    if opcion.get()==1:
        lbl_notificaciones.config(text="Notificaciones Activadas")
    else:
        lbl_notificaciones.config(text="Notificaciones Desactivadas")

# Check Boton
opcion=IntVar()
checkboton=Checkbutton(ventana)
checkboton.config(text="¿Deseas recibir notificaciones?",
                  variable=opcion,
                  onvalue=1,
                  offvalue=0)
checkboton.pack()

# Boton para confirmar.
btn_confirmar=Button(ventana)
btn_confirmar.config(text="Confirmar",
                     command=mostrarEstado)
btn_confirmar.pack(pady=10)

# Texto notificaciones.
lbl_notificaciones=Label(ventana)
lbl_notificaciones.config(text="")
lbl_notificaciones.pack(pady=10)

ventana.mainloop()