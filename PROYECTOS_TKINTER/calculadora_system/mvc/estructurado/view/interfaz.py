from tkinter import *
from tkinter import messagebox
from controller import funciones

def interfaz():
    ventana=Tk()

    ventana.title("Calculadora")
    ventana.geometry("800x600")
    ventana.resizable(False, False)

    titulo=Label(ventana, text="Calculadora Basica")
    titulo.pack(pady=(20, 10))

    n1=IntVar()
    campo1=Entry(ventana, textvariable=n1, width=10, justify="center")
    campo1.pack(pady=(10, 0), side=TOP, anchor=CENTER)

    n2=IntVar()
    campo2=Entry(ventana, textvariable=n2, width=10, justify="center")
    campo2.pack(pady=(0, 10), side=TOP, anchor=CENTER)

    #-----

    bsuma=Button(ventana, text="+ Suma", command=lambda: funciones.operaciones("Suma",n1.get(),n2.get(),"+"))
    bsuma.pack()

    bresta=Button(ventana, text="- Resta", command=lambda: funciones.operaciones("Resta",n1.get(),n2.get(),"-"))
    bresta.pack()

    bmultiplicacion=Button(ventana, text="* Multiplicacion", command=lambda: funciones.operaciones("Multiplicación",n1.get(),n2.get(),"x"))
    bmultiplicacion.pack()

    bdivision=Button(ventana, text="/ Division", command=lambda: funciones.operaciones("División",n1.get(),n2.get(),"/"))
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