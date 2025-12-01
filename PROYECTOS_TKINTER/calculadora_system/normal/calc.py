"""

Crear una calculadora:

1.- Dos campos de Texto
2.- 4 botones para las operaciones
3.- Mostrar el resultado en una alerta

"""

from tkinter import *
from tkinter import messagebox

ventana=Tk()

ventana.title("Calculadora")
ventana.geometry("800x600")
ventana.resizable(False, False)

#-----

def operaciones(titulo,numero1,numero2,signo):
    if signo=="+":
        resultado=numero1+numero2
    elif signo=="-":
        resultado=numero1-numero2
    elif signo=="x":
        resultado=numero1*numero2
    elif signo=="/":
        resultado=numero1/numero2
    messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}+{numero2}={resultado}")

#-----

titulo=Label(ventana, text="Calculadora Basica")
titulo.pack(pady=(20, 10))

n1=IntVar()
campo1=Entry(ventana, textvariable=n1, width=10, justify="center")
campo1.pack(pady=(10, 0), side=TOP, anchor=CENTER)

n2=IntVar()
campo2=Entry(ventana, textvariable=n2, width=10, justify="center")
campo2.pack(pady=(0, 10), side=TOP, anchor=CENTER)

#-----

bsuma=Button(ventana, text="+ Suma", command=lambda: operaciones("Suma",n1.get(),n2.get(),"+"))
bsuma.pack()

bresta=Button(ventana, text="- Resta", command=lambda: operaciones("Resta",n1.get(),n2.get(),"-"))
bresta.pack()

bmultiplicacion=Button(ventana, text="* Multiplicacion", command=lambda: operaciones("Multiplicación",n1.get(),n2.get(),"x"))
bmultiplicacion.pack()

bdivision=Button(ventana, text="/ Division", command=lambda: operaciones("División",n1.get(),n2.get(),"/"))
bdivision.pack()

salir=Button(ventana, 
             text="X Salir", 
             command=ventana.quit, 
             background="#E72E2E", 
             foreground="#FFFFFF", 
             activebackground="#9B3A3A", 
             activeforeground="#FFFFFF",
             width=10)
salir.pack(pady=50)

ventana.mainloop()