from tkinter import *
from tkinter import messagebox
from controller import funciones
from model import operaciones
from tkinter import messagebox

class Vistas:
    
    def __init__(self, ventana):
        
        ventana.title("Calculadora")
        ventana.geometry("800x600")
        # ventana.resizable(False, False)
        self.interfaz(ventana)

    def menuPrincipal(self,ventana):
            
            menuBar=Menu(ventana) # Crear menu
            ventana.config(menu=menuBar) # Asignar menu a la ventana

            archivoMenu=Menu(menuBar, tearoff=False) # Creamos boton Archivo en el menu
            menuBar.add_cascade(label="Archivo", menu=archivoMenu) # Crea una cascada de opciones del boton
            
            archivoMenu.add_command(label="Agregar", command=lambda: self.interfaz(ventana)) # Agrega el comando Agregar en la cascada
            archivoMenu.add_command(label="Consultar", command=lambda: self.consultar(ventana)) # Agrega el comando Consultar en la cascada
            archivoMenu.add_command(label="Cambiar", command=lambda: self.cambiar(ventana)) # Agrega el comando Cambiar en la cascada
            archivoMenu.add_command(label="Eliminar", command=lambda: self.buscar(ventana)) # Agrega el comando Borrar en la cascada
            archivoMenu.add_separator() # Agrega un separador en la cascada
            archivoMenu.add_command(label="Salir", command=ventana.quit) # Agrega un comando que cierra la ventana

    def cambiar(self, ventana):

        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo=Label(ventana, text=".:: Cambiar una Operacion ::.")
        lbl_titulo.pack(pady=10)


        lbl_id=Label(ventana, text="ID de la operacion:")
        lbl_id.pack(pady=10)
        idn=IntVar()
        txt_id=Entry(ventana, textvariable=idn, width=10, justify="center")
        txt_id.pack(pady=(0, 10))
        
        # -------------------------------
        
        lbl_nnum1=Label(ventana, text="Nuevo Numero 1:")
        lbl_nnum1.pack(pady=10)
        num1n=IntVar()
        txt_nnum1=Entry(ventana, textvariable=num1n, justify="center")
        txt_nnum1.pack(pady=(0, 10))

        # -------------------------------
        
        lbl_nnum2=Label(ventana, text="Nuevo Numero 2:")
        lbl_nnum2.pack(pady=10)
        num2n=IntVar()
        txt_nnum2=Entry(ventana, textvariable=num2n, justify="center")
        txt_nnum2.pack(pady=(0, 10))

        # -------------------------------
        
        lbl_signo=Label(ventana, text="Nuevo Signo:")
        lbl_signo.pack(pady=10)
        signon=StringVar()
        txt_signo=Entry(ventana, textvariable=signon, justify="center")
        txt_signo.pack(pady=(0, 10))

        # -------------------------------
        
        lbl_resultado=Label(ventana, text="Nuevo Resultado:")
        lbl_resultado.pack(pady=10)
        resultadon=StringVar()
        txt_resultado=Entry(ventana, textvariable=resultadon, justify="center")
        txt_resultado.pack(pady=(0, 10))

        btn_guardar=Button(ventana, 
                    text="O Guardar", 
                    command=lambda: funciones.Controladores.actualizar(num1n.get(), num2n.get(), signon.get(), resultadon.get(), idn.get()), 
                    background="#5BE033", 
                    foreground="#FFFFFF", 
                    activebackground="#2EBB4C", 
                    activeforeground="#FFFFFF",
                    width=10)
        btn_guardar.pack(pady=(25,5))

        btn_volver=Button(ventana, 
                          text="< Volver", 
                          command=lambda: self.interfaz(ventana), 
                          background="#2E3AE7", 
                          foreground="#FFFFFF", 
                          activebackground="#5C31C2", 
                          activeforeground="#FFFFFF",width=10)
        btn_volver.pack(pady=(5,25))

    def consultar(self, ventana):
        
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo=Label(ventana, text=".:: Listado de las Operaciones ::.")
        lbl_titulo.pack(pady=10)

        idm=funciones.Controladores.consultar()
        
        filas=""
        if len(idm)>0:
             num_operaciones=1
             for fila in idm:
                  filas=filas+f"\nOperacion: {num_operaciones} ID: {fila[0]} Fecha de Creacion: {fila[1]} \nOperacion: {fila[2]} {fila[4]} {fila[3]} {fila[5]}\n"
                  num_operaciones+=1
        else:
             messagebox.showinfo(icon="warning", message="... No existen operaciones en el sistema ...")

        lbl_consultas=Label(ventana, text=f"{filas}")
        lbl_consultas.pack(pady=10)

        btn_volver=Button(ventana, 
                          text="< Volver", 
                          command=lambda: self.interfaz(ventana), 
                          background="#2E3AE7", 
                          foreground="#FFFFFF", 
                          activebackground="#5C31C2", 
                          activeforeground="#FFFFFF",width=10)
        btn_volver.pack(pady=50)

    def eliminar(self, ventana, idb):

        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo=Label(ventana, text=".:: Borrar una Operacion ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana, text="ID de la Operacion")
        lbl_id.pack(pady=5)

        idb=IntVar()
        txt_id=Entry(ventana, textvariable=idb, width=10, justify="right", state="readonly")
        txt_id.focus()
        txt_id.pack(pady=10)

        btn_eliminar=Button(ventana, 
                    text="X Eliminar", 
                    command=lambda:funciones.Controladores.eliminar(idb), 
                    background="#E72E2E", 
                    foreground="#FFFFFF", 
                    activebackground="#9B3A3A", 
                    activeforeground="#FFFFFF",
                    width=10)
        btn_eliminar.pack(pady=10)

        btn_volver=Button(ventana, 
                          text="< Volver", 
                          command=lambda: self.interfaz(ventana), 
                          background="#2E3AE7", 
                          foreground="#FFFFFF", 
                          activebackground="#5C31C2", 
                          activeforeground="#FFFFFF",width=10)
        btn_volver.pack(pady=50)

    def buscar(self, ventana):
            
            self.borrarPantalla(ventana)
            self.menuPrincipal(ventana)

            lbl_titulobuscar=Label(ventana, text=".:: Buscar operacion a eliminar ::.")
            lbl_titulobuscar.pack(pady=10)

            lbl_idbuscar=Label(ventana, text="ID de la Operacion")
            lbl_idbuscar.pack(pady=5)

            idb=IntVar()
            txt_idb=Entry(ventana, textvariable=idb, width=10, justify="right", )
            txt_idb.focus()
            txt_idb.pack(pady=10)

            btn_consultar=Button(ventana, 
                        text="O Buscar", 
                        command=lambda:Vistas.eliminar(self,ventana,txt_idb.get()), 
                        background="#2E59E7", 
                        foreground="#FFFFFF", 
                        activebackground="#443A9B", 
                        activeforeground="#FFFFFF",
                        width=10)
            btn_consultar.pack(pady=10)

            btn_volver=Button(ventana, 
                          text="< Volver", 
                          command=lambda: self.interfaz(ventana), 
                          background="#2E3AE7", 
                          foreground="#FFFFFF", 
                          activebackground="#5C31C2", 
                          activeforeground="#FFFFFF",width=10)
            btn_volver.pack(pady=50)

    def interfaz(self, ventana):
        
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        lbl_titulo=Label(ventana, text=".:: Agregar una Operacion ::.")
        lbl_titulo.pack(pady=10)

        n1=IntVar()
        campo1=Entry(ventana, textvariable=n1, width=10, justify="center")
        campo1.focus()
        campo1.pack(pady=(10, 0), side=TOP, anchor=CENTER)

        n2=IntVar()
        campo2=Entry(ventana, textvariable=n2, width=10, justify="center")
        campo2.focus()
        campo2.pack(pady=(0, 10), side=TOP, anchor=CENTER)

        #-----

        bsuma=Button(ventana, text="+ Suma", command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        bsuma.config(background="#3291A8", 
                    foreground="#FFFFFF", 
                    activebackground="#34588D", 
                    activeforeground="#FFFFFF",)
        bsuma.pack()

        bresta=Button(ventana, text="- Resta", command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        bresta.config(background="#3291A8", 
                    foreground="#FFFFFF", 
                    activebackground="#34588D", 
                    activeforeground="#FFFFFF",)
        bresta.pack()

        bmultiplicacion=Button(ventana, text="* Multiplicacion", command=lambda: funciones.Controladores.operaciones("Multiplicación",n1.get(),n2.get(),"x"))
        bmultiplicacion.config(background="#3291A8", 
                    foreground="#FFFFFF", 
                    activebackground="#34588D", 
                    activeforeground="#FFFFFF",)
        bmultiplicacion.pack()

        bdivision=Button(ventana, text="/ Division", command=lambda: funciones.Controladores.operaciones("División",n1.get(),n2.get(),"/"))
        bdivision.config(background="#3291A8", 
                    foreground="#FFFFFF", 
                    activebackground="#34588D", 
                    activeforeground="#FFFFFF",)
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

    def borrarPantalla(self, ventana):
         
         for widget in ventana.winfo_children():
              widget.destroy()