from tkinter import *

ventana=Tk()
ventana.title("Uso del mainloop")
ventana.geometry("800x700")
ventana.resizable(False, False)

marco1=Frame(ventana, 
             width=800 , 
             height=100, 
             bg="#f62d2d",
             relief=RAISED,
             border=2).pack()

marco2=Frame(ventana, 
             width=800, 
             height=100, 
             bg="#f67d2d",
             relief=RAISED,
             border=2).pack()

marco3=Frame(ventana, 
             width=800, 
             height=100, 
             bg="#f6d42d",
             relief=RAISED,
             border=2).pack()

marco4=Frame(ventana, 
             width=800, 
             height=100, 
             bg="#4ff62d",
             relief=RAISED,
             border=2).pack()

marco5=Frame(ventana, 
             width=800, 
             height=100, 
             bg="#2df6a9",
             relief=RAISED,
             border=2).pack()

marco6=Frame(ventana, 
             width=800, 
             height=100, 
             bg="#2d5cf6",
             relief=RAISED,
             border=2).pack()

marco7=Frame(ventana, 
             width=800, 
             height=100, 
             bg="#8b2df6",
             relief=RAISED,
             border=2).pack()

ventana.mainloop()