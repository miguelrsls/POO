from tkinter import *

def cambiarTexto():
    label_nombre.config(text="Miguel Ángel Rosales Soto",
                   font=("Montserrat"))
    label_password.config(text="12345",
                   font=("Montserrat"))

def regresar():
    label_nombre.config(text="Nombre",
                   font=("Montserrat"))
    label_password.config(text="Contraseña",
                   font=("Montserrat"))

ventana=Tk()
ventana.title("Uso de botones, marcos, etiquetas")
ventana.geometry("800x600")

login=Frame(ventana)
login.config(width=800,
            height=100,
            bg="#9BF1D0",
            relief=RAISED,
            border=2)
login.pack_propagate(False)
login.pack()

label_titulo=Label(login)
label_titulo.config(text="Inicio de Sesion",
                 bg="#9BF1D0",
                 font="Montserrat")
label_titulo.pack(pady=40)

label_nombre=Label(ventana)
label_nombre.config(text="Nombre: ",
                   font=("Montserrat"))
label_nombre.pack(pady=10)

label_password=Label(ventana)
label_password.config(text="Contraseña: ",
                   font=("Montserrat"))
label_password.pack(pady=10)

btn_aceptar=Button(ventana)
btn_aceptar.config(text="Aceptar",
                   command=cambiarTexto)
btn_aceptar.pack(pady=10)

btn_regresar=Button(ventana)
btn_regresar.config(text="Regresar",
                    command=regresar)
btn_regresar.pack(pady=10)

ventana.mainloop()