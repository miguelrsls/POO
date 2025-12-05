from tkinter import *
from tkinter import messagebox
from controller import controlador
from model import cochesBD

class Interfaces():

    def __init__(self,ventana):
        ventana.title("Gestion de Coches")
        ventana.geometry("800x800")
        Interfaces.menu_principal(ventana)

    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    # Principal y acciones

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

        if titulo=="Autos":
            btnInsertar=Button(ventana, text="Insertar", command=lambda: Interfaces.insertar_autos(ventana,titulo))
            btnInsertar.pack(pady=(20,0))

            btnConsultar=Button(ventana, text="Consultar", command=lambda: Interfaces.consultar_autos(ventana,titulo))
            btnConsultar.pack(pady=(0,0))

            btnCambiar=Button(ventana, text="Cambiar", command=lambda: Interfaces.buscar_id(ventana, titulo, "Cambiar"))
            btnCambiar.pack(pady=(0,0))

            btnEliminar=Button(ventana, text="Eliminar", command=lambda: Interfaces.buscar_id(ventana, titulo, "Borrar"))
            btnEliminar.pack(pady=(0,0))
        
        elif titulo=="Camionetas":
            btnInsertar=Button(ventana, text="Insertar", command=lambda: Interfaces.insertar_camionetas(ventana,titulo))
            btnInsertar.pack(pady=(20,0))

            btnConsultar=Button(ventana, text="Consultar", command=lambda: Interfaces.consultar_camionetas(ventana,titulo))
            btnConsultar.pack(pady=(0,0))

            btnCambiar=Button(ventana, text="Cambiar", command=lambda: Interfaces.cambiar_camionetas(ventana,titulo))
            btnCambiar.pack(pady=(0,0))

            btnEliminarAutos=Button(ventana, text="Eliminar", command=lambda: Interfaces.borrar_camionetas(ventana, titulo))
            btnEliminarAutos.pack(pady=(0,0))
        
        elif titulo=="Camiones":
            btnInsertar=Button(ventana, text="Insertar", command=lambda: Interfaces.insertar_camiones(ventana,titulo))
            btnInsertar.pack(pady=(20,0))

            btnConsultar=Button(ventana, text="Consultar", command=lambda: Interfaces.consultar_camiones(ventana,titulo))
            btnConsultar.pack(pady=(0,0))

            btnCambiar=Button(ventana, text="Cambiar", command=lambda: Interfaces.cambiar_camiones(ventana,titulo))
            btnCambiar.pack(pady=(0,0))

            btnEliminarAutos=Button(ventana, text="Eliminar", command=lambda: Interfaces.borrar_camiones(ventana, titulo))
            btnEliminarAutos.pack(pady=(0,0))
        
        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_principal(ventana))
        btnVolver.pack(pady=50)

    def buscar_id(ventana,titulo,tipo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text="Buscar una Operacion")
        lblTitulo.pack(pady=5)

        idn=IntVar()
        lblID=Label(ventana, text="ID de la Operacion a Buscar")
        txtID=Entry(ventana, textvariable=idn)
        txtID.focus()
        lblID.pack(pady=(10,0))
        txtID.pack(pady=(0,10))

        if tipo=="Cambiar":
            Button(ventana, text="Buscar", command=lambda: Interfaces.cambiar_autos(ventana, titulo, txtID.get())).pack(pady=10)
        elif tipo=="Borrar":
            Button(ventana, text="Buscar", command=lambda: Interfaces.borrar_autos(ventana, titulo, txtID.get())).pack(pady=10)
        
        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=(0,50))
    
    # Autos

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

        btnGuardar=Button(ventana, text="Guardar", command=lambda: controlador.Autos.insertarAutos(txtMarca.get(), txtColor.get(), txtModelo.get(), txtVelocidad.get(), txtCaballaje.get(), txtPlazas.get(), ventana))
        btnGuardar.pack(pady=(50,0))

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=(0,50))

    def consultar_autos(ventana, titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Consultas en {titulo}")
        lblTitulo.pack(pady=5)

        # ---

        filas=""
        registros=controlador.Autos.consultarAutos()

        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"Auto: {num_notas}\n ID: {fila[0]}\n Marca: {fila[1]}\n Color: {fila[2]}\n Modelo: {fila[3]}\n Velocidad: {fila[4]}\n Caballaje: {fila[5]}\n Plazas: {fila[6]}\n\n"
                num_notas+=1
        else:
            messagebox.showinfo(icon="info", message=f"No existen {titulo}, intente agregar uno nuevo.")

        # -----

        lblConsultas=Label(ventana, text=filas)
        lblConsultas.pack(pady=10)

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=50)

    def cambiar_autos(ventana, titulo, idn):
        registro=cochesBD.Autos.IDAutos(idn)
        if registro is None:
            messagebox.showinfo(icon="info", message="No existen autos con esta ID en la base de datos...")
        else:
            Interfaces.borrarPantalla(ventana)

            lblTitulo=Label(ventana, text=f"Cambiar en {titulo}")
            lblTitulo.pack(pady=5)

            idna=IntVar()
            lblIDN=Label(ventana, text="ID")
            txtID=Entry(ventana, textvariable=idna, state="readonly")
            idna.set(idn)
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

            btnGuardar=Button(ventana, text="Guardar", command=lambda: controlador.Autos.actualizarAutos(txtMarca.get(), txtColor.get(), txtModelo.get(), txtVelocidad.get(), txtCaballaje.get(), txtPlazas.get(), txtID.get(), ventana))
            btnGuardar.pack(pady=(50,0))

            btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
            btnVolver.pack(pady=(0,50))
    
    def borrar_autos(ventana, titulo, idn):
        registro=cochesBD.Autos.IDAutos(idn)
        if registro is None:
            messagebox.showinfo(icon="info", message="No existen autos con esta ID en la base de datos...")
        else:
            Interfaces.borrarPantalla(ventana)

            lblTitulo=Label(ventana, text=f"Borrar en {titulo} por ID")
            lblTitulo.pack(pady=5)

            idna=IntVar()
            lblIDN=Label(ventana, text="ID")
            txtID=Entry(ventana, textvariable=idna, state="readonly")
            idna.set(idn)
            txtID.focus()
            lblIDN.pack(pady=(10,0))
            txtID.pack(pady=(0,0))

            btnBorrar=Button(ventana, text="Borrar", command=lambda: controlador.Autos.borrarAutos(txtID.get(), ventana))
            btnBorrar.pack(pady=(50,0))

            btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
            btnVolver.pack(pady=(0,50))
    
    # Camionetas

    def insertar_camionetas(ventana,titulo):
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

        # Camionetas ---------------------------------------------------------

        lblTraccion=Label(ventana, text="Traccion")
        lbxTraccion=Listbox(ventana,width=20,height=3,selectmode=SINGLE, exportselection=FALSE)
        trac=["Trasera","Delantera", "Total"]
        for i in trac:
            lbxTraccion.insert(END,i)
        lblTraccion.pack(pady=(10,0))
        lbxTraccion.pack(pady=(10,0))

        lblCerrada=Label(ventana, text="Cerrada")
        lbxCerrada=Listbox(ventana,width=20,height=2,selectmode=SINGLE, exportselection=FALSE)
        cerr=["Si","No"]
        for i in cerr:
            lbxCerrada.insert(END,i)
        lblCerrada.pack(pady=(10,0))
        lbxCerrada.pack(pady=(10,0))

        # ---------------------------------------------------------------------

        btnGuardar=Button(ventana, text="Guardar")
        btnGuardar.pack(pady=(50,0))

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=(0,50))

    def consultar_camionetas(ventana, titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Consultas en {titulo}")
        lblTitulo.pack(pady=5)

        lblConsultas=Label(ventana, text=f"No hay consultas en este momento dentro de {titulo}")
        lblConsultas.pack(pady=10)

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=50)

    def cambiar_camionetas(ventana, titulo):
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

        # Camionetas ---------------------------------------------------------

        lblTraccion=Label(ventana, text="Traccion")
        lbxTraccion=Listbox(ventana,width=20,height=3,selectmode=SINGLE, exportselection=FALSE)
        trac=["Trasera","Delantera", "Total"]
        for i in trac:
            lbxTraccion.insert(END,i)
        lblTraccion.pack(pady=(10,0))
        lbxTraccion.pack(pady=(10,0))

        lblCerrada=Label(ventana, text="Cerrada")
        lbxCerrada=Listbox(ventana,width=20,height=2,selectmode=SINGLE, exportselection=FALSE)
        cerr=["Si","No"]
        for i in cerr:
            lbxCerrada.insert(END,i)
        lblCerrada.pack(pady=(10,0))
        lbxCerrada.pack(pady=(10,0))

        # ---------------------------------------------------------------------

        btnGuardar=Button(ventana, text="Guardar")
        btnGuardar.pack(pady=(50,0))

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=(0,50))

    def borrar_camionetas(ventana, titulo):
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

    # Camiones

    def insertar_camiones(ventana,titulo):
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

    def consultar_camiones(ventana, titulo):
        Interfaces.borrarPantalla(ventana)

        lblTitulo=Label(ventana, text=f"Consultas en {titulo}")
        lblTitulo.pack(pady=5)

        lblConsultas=Label(ventana, text=f"No hay consultas en este momento dentro de {titulo}")
        lblConsultas.pack(pady=10)

        btnVolver=Button(ventana, text="Volver", command=lambda: Interfaces.menu_acciones(ventana,titulo))
        btnVolver.pack(pady=50)

    def cambiar_camiones(ventana, titulo):
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

    def borrar_camiones(ventana, titulo):
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