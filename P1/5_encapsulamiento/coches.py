import os
os.system("cls")

class Coches:

    # Metodo constructor. Con este metodo se inicializa un objeto cuando es creado con valores iniciales.

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

    """
    Crear los metodos setters y getters. Estos metodos son iportantes y necesarios en todas las clases para que el programador interactue
    con los valores de los atributoss a traves de estos metodos... digamos que es la manera mas adecuada y recomendada para solicitar un valor
    (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.

    En teoria se deberia crear un metodo Getters y Setters por cada atributo qeu contengla la clase

    Los metodos get siempre regresan un valor es decir el valor de la propiedad a traves del return.
    Por otro lado, el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion.
    """
    # Primer forma de crear Set y Get.

    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca=marca
    
    # Segunda forma de crear Set y Get.

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter # El nombre debe ser igual al de arriba.
    def marca(self, marca):
        self.__marca=marca
    
    # --------------------------------

    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color=color
    
    def getModelo(self):
        return self.__modelo
    def setModelo(self,modelo):
        self.__modelo=modelo
    
    def getVelocidad(self):
        return self.__velocidad
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad
    
    def getCaballaje(self):
        return self.__caballaje
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje
    
    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,plazas):
        self.__plazas=plazas
        
    # Metodos o acciones o funciones que hace el objeto.
    
    def acelerar(self):
        return "Estoy acelerando el coche."
    
    def frenar(self):
        return "Estoy frenando el coche."