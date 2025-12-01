from tkinter import messagebox
from model import usuario,nota
from view import vista

class Controlador:

    @staticmethod
    def registrar(nombre,apellidos,email,password,ventana):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info", message=f"{nombre} {apellidos}, se registro correctamente con el email: {email}")
            vista.Interfaces.menu_login(ventana)
        else:
            messagebox.showinfo(icon="warning", message=f"{nombre} {apellidos}, no se pudo completar el proceso, intentelo nuevamente")
    
    @staticmethod
    def login(email,password, ventana):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info", message=f"{registro[1]} {registro[2]}, haz iniciado sesion correctamente.")
            vista.Interfaces.menu_notas(ventana, registro[0], registro[1], registro[2])

        else:
            messagebox.showinfo(icon="warning", message=f"Credenciales incorrectas, intentelo nuevamente")

    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        respuesta=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.resultados_sql("Crear nota", respuesta)

    @staticmethod
    def mostrar_nota(usuario_id):
        respuesta=nota.Nota.mostrar(usuario_id)
        return respuesta

    @staticmethod
    def eliminar_nota(id):
        respuesta=nota.Nota.eliminar(id)
        Controlador.resultados_sql("Eliminar nota", respuesta)

    @staticmethod
    def cambiar_nota(id,titulo,descripcion):
        respuesta=nota.Nota.actualizar(id,titulo,descripcion)
        Controlador.resultados_sql("Actualizar nota", respuesta)

    @staticmethod
    def resultados_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo, message="La accion se ha realizado con exito.", icon="info")
        else:
            messagebox.showinfo(title=titulo, message="No fue posible realizar la accion en este momento, intentelo nuevamente.", icon="warning")