"""
Encapsular: Es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributos y metodos de una clase
a la hora de usar en objetos o en herencia.
"""

import  os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio

    @property # COLOR
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color=color    
    
    @property # TAMAÑO
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio=tamanio

    @property # PUBLICO
    def publico(self):
        return self.atributo_publico
    @publico.setter
    def publico(self,atributo_publico):
        self.atributo_publico=atributo_publico

    @property # PROTEGIDO
    def atributo_protegido(self):
        return self._atributo_protegido
    @atributo_protegido.setter
    def atributo_protegido(self,atributo_protegido):
        self._atributo_protegido=atributo_protegido

    @property # PRIVADO
    def atributo_privado(self):
        return self.__atributo_privado
    @atributo_privado.setter
    def atributo_privado(self,atributo_privado):
        self.__atributo_privado=atributo_privado

# Utilizar una clase

objeto=Clase("Rojo","Grande")
print(objeto.color)
print(objeto.tamanio)
print(objeto.publico)
print(objeto.atributo_protegido)
print(objeto.atributo_privado)
# print(objeto._atributo_protegido) # No es buena practica acceder a los valores directamente.
# print(objeto.getAtributoPrivado())