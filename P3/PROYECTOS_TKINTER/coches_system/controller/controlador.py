from tkinter import messagebox
from model import cochesBD
from view import vista

class Autos:

    @staticmethod
    def insertarAutos(marca,color,modelo,velocidad,caballaje,plazas,ventana):
        resultado=cochesBD.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        Autos.resultados_sql("Insertar Autos", resultado, ventana)
    
    @staticmethod
    def consultarAutos():
        resultado=cochesBD.Autos.consultar()
        return resultado

    @staticmethod
    def actualizarAutos(marca, color, modelo,velocidad,caballaje,plazas,id, ventana):
        resultado=cochesBD.Autos.actualizar(marca, color, modelo,velocidad,caballaje,plazas,id)
        Autos.resultados_sql("Actualizar Autos", resultado, ventana)

    @staticmethod
    def borrarAutos(id, ventana):
        resultado=cochesBD.Autos.eliminar(id)
        Autos.resultados_sql("Eliminar Autos", resultado, ventana)

    @staticmethod
    def resultados_sql(titulo,respuesta,ventana):
        if respuesta:
            messagebox.showinfo(title=titulo, message="La accion se ha realizado con exito.", icon="info")
            vista.Interfaces.menu_acciones(ventana, "Autos")
        else:
            messagebox.showinfo(title=titulo, message="No fue posible realizar la accion en este momento, intentelo nuevamente.", icon="warning")

class Camionetas:

    @staticmethod
    def insertarCamionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,ventana):
        resultado=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        Camionetas.resultados_sql_camionetas("Insertar Camionetas", resultado, ventana)
    
    @staticmethod
    def consultarCamionetas():
        resultado=cochesBD.Camionetas.consultar()
        return resultado

    @staticmethod
    def actualizarCamionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id,ventana):
        resultado=cochesBD.Camionetas.actualizar(marca, color, modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
        Camionetas.resultados_sql_camionetas("Actualizar Camionetas", resultado, ventana)

    @staticmethod
    def borrarCamionetas(id, ventana):
        resultado=cochesBD.Camionetas.eliminar(id)
        Camionetas.resultados_sql_camionetas("Eliminar Camionetas", resultado, ventana)

    @staticmethod
    def resultados_sql_camionetas(titulo,respuesta,ventana):
        if respuesta:
            messagebox.showinfo(title=titulo, message="La accion se ha realizado con exito.", icon="info")
            vista.Interfaces.menu_acciones(ventana, "Camionetas")
        else:
            messagebox.showinfo(title=titulo, message="No fue posible realizar la accion en este momento, intentelo nuevamente.", icon="warning")

class Camiones:

    @staticmethod
    def insertarCamiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,ventana):
        resultado=cochesBD.Camiones.insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
        Camiones.resultados_sql_camiones("Insertar Camiones", resultado, ventana)
    
    @staticmethod
    def consultarCamiones():
        resultado=cochesBD.Camiones.consultar()
        return resultado

    @staticmethod
    def actualizarCamiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id,ventana):
        resultado=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
        Camiones.resultados_sql_camiones("Actualizar Camiones", resultado, ventana)

    @staticmethod
    def borrarCamiones(id, ventana):
        resultado=cochesBD.Camiones.eliminar(id)
        Camiones.resultados_sql_camiones("Eliminar Camiones", resultado, ventana)

    @staticmethod
    def resultados_sql_camiones(titulo,respuesta,ventana):
        if respuesta:
            messagebox.showinfo(title=titulo, message="La accion se ha realizado con exito.", icon="info")
            vista.Interfaces.menu_acciones(ventana, "Camiones")
        else:
            messagebox.showinfo(title=titulo, message="No fue posible realizar la accion en este momento, intentelo nuevamente.", icon="warning")