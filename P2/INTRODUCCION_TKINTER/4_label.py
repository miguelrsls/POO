from tkinter import *

ventana=Tk()
ventana.title("Uso de etiquetas (label)")
ventana.geometry("600x400")
ventana.resizable(False, False)

marco1=Frame(ventana,
             width=600,
             height=100,
             bg="#9162C7",
             relief=FLAT,
             border=2)
marco1.pack_propagate(False)
marco1.pack()

marco2=Frame(ventana,
             width=600,
             height=100,
             bg="#5E539E",
             relief=FLAT,
             border=2)
marco2.pack_propagate(False)
marco2.pack()

marco3=Frame(ventana,
             width=600,
             height=100,
             bg="#4B4780",
             relief=FLAT,
             border=2)
marco3.pack_propagate(False)
marco3.pack()

marco4=Frame(ventana,
             width=600,
             height=100,
             bg="#3D3A61",
             relief=FLAT,
             border=2)
marco4.pack_propagate(False)
marco4.pack()

# Etiquetas o Label

etiqueta1=Label(marco1,
                text="Miguel Ángel Rosales Soto",
                background="#9162C7").pack(pady=40)

etiqueta2=Label(marco2,
                text="Universidad Tecnologica de Durango",
                background="#5E539E").pack(pady=40)

etiqueta3=Label(marco3,
                text="Tecnologias de la Informacion",
                background="#4B4780").pack(pady=40)

etiqueta4=Label(marco4,
                text="Desarrollo de Software Multiplataforma",
                background="#3D3A61").pack(pady=40)

ventana.mainloop()