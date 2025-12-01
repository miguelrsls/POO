from tkinter import *
from tkinter import messagebox
from controller import controlador

class Interfaces():

    def __init__(self,ventana):
        ventana.title("Gestion de Coches")
        ventana.geometry("800x800")
        Interfaces.menu_principal(ventana)

    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_principal(ventana):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text="Sistema de Gestion de Coches")
        lblTitulo.pack(pady=5)

        btnAutos=Button(ventana, text="Autos", command=lambda: Interfaces.menu_acciones(ventana,"Autos"))
        btnAutos.pack(pady=(20,0))

        btnCamionetas=Button(ventana, text="Camionetas", command=lambda: Interfaces.menu_acciones(ventana,"Camionetas"))
        btnCamionetas.pack(pady=(0,0))

        btnCamiones=Button(ventana, text="Camiones", command=lambda: Interfaces.menu_acciones(ventana,"Camiones"))
        btnCamiones.pack(pady=(0,0))

        btnSalir=Button(ventana, text="Salir", command=ventana.quit)
        btnSalir.pack(pady=50)

    def menu_acciones(ventana,titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Acciones: {titulo}")
        lblTitulo.pack(pady=5)

        btnInsertar=Button(ventana, text="Insertar", command=lambda: Interfaces.insertar_autos(ventana,titulo))
        btnInsertar.pack(pady=(20,0))

        btnConsultar=Button(ventana, text="Consultar", command=lambda: Interfaces.consultar_autos(ventana,titulo))
        btnConsultar.pack(pady=(0,0))

        btnCambiar=Button(ventana, text="Cambiar", command=lambda: Interfaces.cambiar_autos(ventana,titulo))
        btnCambiar.pack(pady=(0,0))

        btnEliminar=Button(ventana, text="Eliminar", command=lambda: Interfaces.borrar_autos(ventana, titulo))
        btnEliminar.pack(pady=(0,0))

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_principal(ventana))
        btnVolver.pack(pady=50)

    def insertar_autos(ventana,titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Insertar en {titulo}")
        lblTitulo.pack(pady=5)

        marca=StringVar()
        lblMarca=Label(ventana, text="Marca")
        txtMarca=Entry(ventana, textvariable=marca)
        txtMarca.focus()
        lblMarca.pack(pady=(10,0))
        txtMarca.pack(pady=(0,0))

        color=StringVar()
        lblColor=Label(ventana, text="Color")
        txtColor=Entry(ventana, textvariable=color)
        txtColor.focus()
        lblColor.pack(pady=(10,0))
        txtColor.pack(pady=(0,0))

        modelo=StringVar()
        lblModelo=Label(ventana, text="Modelo")
        txtModelo=Entry(ventana, textvariable=modelo)
        txtModelo.focus()
        lblModelo.pack(pady=(10,0))
        txtModelo.pack(pady=(0,0))

        velocidad=IntVar()
        lblVelocidad=Label(ventana, text="Velocidad")
        txtVelocidad=Entry(ventana, textvariable=velocidad)
        txtVelocidad.focus()
        lblVelocidad.pack(pady=(10,0))
        txtVelocidad.pack(pady=(0,0))

        caballaje=IntVar()
        lblCaballaje=Label(ventana, text="Caballaje")
        txtCaballaje=Entry(ventana, textvariable=caballaje)
        txtCaballaje.focus()
        lblCaballaje.pack(pady=(10,0))
        txtCaballaje.pack(pady=(0,0))

        plazas=IntVar()
        lblPlazas=Label(ventana, text="Plazas")
        txtPlazas=Entry(ventana, textvariable=plazas)
        txtPlazas.focus()
        lblPlazas.pack(pady=(10,0))
        txtPlazas.pack(pady=(0,0))

        # Camionetas

        traccion=IntVar()
        lblTraccion=Label(ventana, text="Traccion")
        txtTraccion=Entry(ventana, textvariable=traccion)
        txtTraccion.focus()
        lblTraccion.pack(pady=(10,0))
        txtTraccion.pack(pady=(0,0))

        cerrada=StringVar()
        lblCerrada=Label(ventana, text="Cerrada (SI / NO)")
        txtCerrada=Entry(ventana, textvariable=cerrada)
        txtCerrada.focus()
        lblCerrada.pack(pady=(10,0))
        txtCerrada.pack(pady=(0,0))

        # Camiones

        ejes=IntVar()
        lblEjes=Label(ventana, text="Ejes")
        txtEjes=Entry(ventana, textvariable=ejes)
        txtEjes.focus()
        lblEjes.pack(pady=(10,0))
        txtEjes.pack(pady=(0,0))

        capacidad=IntVar()
        lblCapacidad=Label(ventana, text="Capacidad")
        txtCapacidad=Entry(ventana, textvariable=capacidad)
        txtCapacidad.focus()
        lblCapacidad.pack(pady=(10,0))
        txtCapacidad.pack(pady=(0,0))

        btnGuardar=Button(ventana, text="Guardar")
        btnGuardar.pack(pady=(50,0))

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=(0,50))

    def consultar_autos(ventana, titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Consultas en {titulo}")
        lblTitulo.pack(pady=5)

        lblConsultas=Label(ventana, text=f"No hay consultas en este momento dentro de {titulo}")
        lblConsultas.pack(pady=10)

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=50)

    def cambiar_autos(ventana, titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Cambiar en {titulo}")
        lblTitulo.pack(pady=5)

        idn=IntVar()
        lblIDN=Label(ventana, text="ID")
        txtID=Entry(ventana, textvariable=idn)
        txtID.focus()
        lblIDN.pack(pady=(10,0))
        txtID.pack(pady=(0,0))

        marca=StringVar()
        lblMarca=Label(ventana, text="Marca")
        txtMarca=Entry(ventana, textvariable=marca)
        txtMarca.focus()
        lblMarca.pack(pady=(10,0))
        txtMarca.pack(pady=(0,0))

        color=StringVar()
        lblColor=Label(ventana, text="Color")
        txtColor=Entry(ventana, textvariable=color)
        txtColor.focus()
        lblColor.pack(pady=(10,0))
        txtColor.pack(pady=(0,0))

        modelo=StringVar()
        lblModelo=Label(ventana, text="Modelo")
        txtModelo=Entry(ventana, textvariable=modelo)
        txtModelo.focus()
        lblModelo.pack(pady=(10,0))
        txtModelo.pack(pady=(0,0))

        velocidad=IntVar()
        lblVelocidad=Label(ventana, text="Velocidad")
        txtVelocidad=Entry(ventana, textvariable=velocidad)
        txtVelocidad.focus()
        lblVelocidad.pack(pady=(10,0))
        txtVelocidad.pack(pady=(0,0))

        caballaje=IntVar()
        lblCaballaje=Label(ventana, text="Caballaje")
        txtCaballaje=Entry(ventana, textvariable=caballaje)
        txtCaballaje.focus()
        lblCaballaje.pack(pady=(10,0))
        txtCaballaje.pack(pady=(0,0))

        plazas=IntVar()
        lblPlazas=Label(ventana, text="Plazas")
        txtPlazas=Entry(ventana, textvariable=plazas)
        txtPlazas.focus()
        lblPlazas.pack(pady=(10,0))
        txtPlazas.pack(pady=(0,0))

        # Camionetas

        traccion=IntVar()
        lblTraccion=Label(ventana, text="Traccion")
        txtTraccion=Entry(ventana, textvariable=traccion)
        txtTraccion.focus()
        lblTraccion.pack(pady=(10,0))
        txtTraccion.pack(pady=(0,0))

        cerrada=StringVar()
        lblCerrada=Label(ventana, text="Cerrada (SI / NO)")
        txtCerrada=Entry(ventana, textvariable=cerrada)
        txtCerrada.focus()
        lblCerrada.pack(pady=(10,0))
        txtCerrada.pack(pady=(0,0))

        # Camiones

        ejes=IntVar()
        lblEjes=Label(ventana, text="Ejes")
        txtEjes=Entry(ventana, textvariable=ejes)
        txtEjes.focus()
        lblEjes.pack(pady=(10,0))
        txtEjes.pack(pady=(0,0))

        capacidad=IntVar()
        lblCapacidad=Label(ventana, text="Capacidad")
        txtCapacidad=Entry(ventana, textvariable=capacidad)
        txtCapacidad.focus()
        lblCapacidad.pack(pady=(10,0))
        txtCapacidad.pack(pady=(0,0))

        btnGuardar=Button(ventana, text="Guardar")
        btnGuardar.pack(pady=(50,0))

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=(0,50))
    
    def borrar_autos(ventana, titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Borrar en {titulo} por ID")
        lblTitulo.pack(pady=5)

        idn=IntVar()
        lblIDN=Label(ventana, text="ID")
        txtID=Entry(ventana, textvariable=idn)
        txtID.focus()
        lblIDN.pack(pady=(10,0))
        txtID.pack(pady=(0,0))

        btnBorrar=Button(ventana, text="Borrar")
        btnBorrar.pack(pady=(50,0))

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=(0,50))