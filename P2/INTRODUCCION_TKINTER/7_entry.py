from tkinter import *

# def cambiar():
#     lbl_resultado.config(text=f"Bienvenido {nombre.get()}, un gusto verte de vuelta.",)
#     txt_nombre.config(state="disabled")

# ventana=Tk()
# ventana.title("Entry")
# ventana.geometry("800x600")
# ventana.resizable(False, False)

# lbl_nombre=Label(ventana)
# lbl_nombre.config(text="Ingrese su nombre:",
#                 font=("Montserrat", 12))
# lbl_nombre.pack(pady=10)

# nombre=StringVar()
# txt_nombre=Entry(ventana, textvariable=nombre)
# txt_nombre.config(width=50)
# txt_nombre.pack(pady=10)

# btn_saludar=Button(ventana)
# btn_saludar.config(text="Saludar",
#                    font=("Montserrat", 10),
#                    command=cambiar)
# btn_saludar.pack(pady=10)

# lbl_resultado=Label(ventana)
# lbl_resultado.config(text="")
# lbl_resultado.pack(pady=10)

# ventana.mainloop()

def cambiar():
     lbl_resultado.config(text=f"Bienvenido {nombre.get()}, un gusto verte de vuelta.",)

def borrar():
     txt_nombre.delete(0, END)
     txt_pass.delete(0, END)
     lbl_resultado.config(text="")

ventana=Tk()
ventana.title("Iniciar Sesion")
ventana.geometry("800x600")
ventana.resizable(False, False)

lbl_title=Label(ventana)
lbl_title.config(text="Bienvenido, inicia sesion.")
lbl_title.pack(pady=10)

lbl_nombre=Label(ventana)
lbl_nombre.config(text="Nombre:")
lbl_nombre.pack(pady=10)

nombre=StringVar()
txt_nombre=Entry(ventana, textvariable=nombre)
txt_nombre.config(width=30)
txt_nombre.pack()

lbl_pass=Label(ventana)
lbl_pass.config(text="Contraseña:")
lbl_pass.pack(pady=10)

password=StringVar()
txt_pass=Entry(ventana, textvariable=password, show="*")
txt_pass.config(width=30)
txt_pass.pack()

btn_iniciar=Button(ventana)
btn_iniciar.config(text="Iniciar Sesion",
                   width=15,
                   command=cambiar)
btn_iniciar.pack(pady=10)

lbl_resultado=Label(ventana)
lbl_resultado.config(text="")
lbl_resultado.pack(pady=10)

btn_borrar=Button(ventana)
btn_borrar.config(text="Borrar",
                   width=15,
                   command=borrar)
btn_borrar.pack(pady=10)

ventana.mainloop()