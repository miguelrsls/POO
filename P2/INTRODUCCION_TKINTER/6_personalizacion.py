from tkinter import *

def cambiarFondo():
    etiqueta.config(bg="red",
                    fg="white",)
    
def regresarFondo():
    etiqueta.config(bg="lightblue",
                    fg="black")


ventana=Tk()
ventana.title("Personalizar Objetos")
ventana.geometry("800x600")
ventana.resizable(False, False)

etiqueta=Label(ventana)
etiqueta.config(text="Bienvenidos a Tkinter",
                bg="lightblue",
                fg="black",
                width=50,
                height=4,
                font=("Helvetica", 30, "bold"))
etiqueta.pack()

boton1=Button(ventana)
boton1.config(text="Haz clic",
              bg="black",
              fg="white",
              font=("Arial", 20, "bold"),
              relief=FLAT,
              border=1,
              width=15,
              activebackground="white",
              activeforeground="black",
              command=cambiarFondo)
boton1.pack(pady=15)

boton2=Button(ventana)
boton2.config(text="Regresar",
              bg="black",
              fg="white",
              font=("Arial", 20, "bold"),
              relief=FLAT,
              border=1,
              width=15,
              activebackground="white",
              activeforeground="black",
              command=regresarFondo)
boton2.pack(pady=15)

ventana.mainloop()