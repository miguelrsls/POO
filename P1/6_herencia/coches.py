import os
os.system("cls")

class Coches:

    # Metodo constructor. Con este metodo se inicializa un objeto cuando es creado con valores iniciales.

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    # Metodos Get y Set.

    def getMarca(self):
        return self._marca
    def setMarca(self,marca):
        self._marca=marca
    
    def getColor(self):
        return self._color
    def setColor(self,color):
        self._color=color
    
    def getModelo(self):
        return self._modelo
    def setModelo(self,modelo):
        self._modelo=modelo
    
    def getVelocidad(self):
        return self._velocidad
    def setVelocidad(self,velocidad):
        self._velocidad=velocidad
    
    def getCaballaje(self):
        return self._caballaje
    def setCaballaje(self,caballaje):
        self._caballaje=caballaje
    
    def getPlazas(self):
        return self._plazas
    def setPlazas(self,plazas):
        self._plazas=plazas
        
    # Metodos o acciones o funciones que hace el objeto.
    
    def acelerar(self):
        return "Estoy acelerando el coche."
    
    def frenar(self):
        return "Estoy frenando el coche."
    
class Camiones(Coches):


    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas) # Trae todos los atributos de la clase Coches.
        
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

        # Metodos Set y Get

    @property
    def eje(self):
        return self.__eje
    @eje.setter
    def eje(self,eje):
        self.__eje=eje
        
    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    @capacidadCarga.setter
    def capacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga
        
    # Metodos

    def cargar(self, tipo_carga):
        self.__tipo_carga=tipo_carga
        return self.__tipo_carga

class Camionetas(Coches):

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas) # Trae todos los atributos de la clase Coches.
        
        self.__traccion=traccion
        self.__cerrada=cerrada

    # Metodos Set y Get.}

    @property
    def traccion(self):
        return self.__traccion
    @traccion.setter
    def traccion(self, traccion):
        self.__traccion=traccion
    
    @property
    def cerrada(self):
        return self.__cerrada
    @cerrada.setter
    def cerrada(self, cerrada):
        self.__cerrada=cerrada

    # Metodos

    def transportar(self, numeropasajeros):
        self.__numeropasajeros=numeropasajeros
        return self.__numeropasajeros