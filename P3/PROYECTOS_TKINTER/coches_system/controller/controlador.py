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