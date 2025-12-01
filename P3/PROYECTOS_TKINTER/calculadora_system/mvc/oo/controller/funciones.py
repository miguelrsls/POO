from tkinter import messagebox
from model import operaciones

class Controladores:
    
    @staticmethod # Te permite usar la clase sin crear un objeto previamente.
    def operaciones(titulo,numero1,numero2,signo):
        if signo=="+":
            resultado=numero1+numero2
        elif signo=="-":
            resultado=numero1-numero2
        elif signo=="x":
            resultado=numero1*numero2
        elif signo=="/":
            resultado=numero1/numero2
        # messagebox.showinfo(icon="info",title=titulo,message=f"{numero1} {signo} {numero2} = {resultado}")
        respuesta=messagebox.askquestion(title=titulo, message=f"{numero1} {signo} {numero2} = {resultado}\n ¿Quieres guardar la operacion en la base de datos?",icon="question")
        if respuesta=="yes":
            respuesta=operaciones.Operaciones.crear(numero1,numero2,signo,resultado)
            Controladores.resultados_sql(respuesta)


    @staticmethod
    def eliminar(idn):
        respuesta=messagebox.askquestion(title="Eliminar", message=f"¿Quieres eliminar la operacion de la base de datos?",icon="question")
        if respuesta=="yes":
            respuesta=operaciones.Operaciones.eliminar(idn)
            Controladores.resultados_sql("Borrar Registro")

    @staticmethod
    def consultar():
        registros=operaciones.Operaciones.mostrar()
        return registros

    @staticmethod
    def actualizar(n1,n2,signo,res,idn):
        respuesta=messagebox.askquestion(title="Actualizar", message=f"{n1} {signo} {n2} = {res}\n ¿Quieres actualizar la operacion en la base de datos?",icon="question")
        if respuesta=="yes":
            respuesta=operaciones.Operaciones.actualizar(n1,n2,signo,res,idn)
            Controladores.resultados_sql("Actualizar Registro")

    @staticmethod
    def resultados_sql(respuesta):
        if respuesta:
            messagebox.showinfo(title="SQL", message="La accion se ha realizado con exito.", icon="info")
        else:
            messagebox.showinfo(title="SQL", message="No fue posible realizar la accion en este momento, intentelo nuevamente.", icon="warning")
    
    @staticmethod
    def buscar(idb):
        registros=operaciones.Operaciones.mostrarID(idb)
        if registros:
            return True
        else:
            messagebox.showinfo(title="No encontrado", message="No se ha encontrado una operacion con esa ID")
            return False