import os
os.system("cls")

class Coches:

    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0

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
        pass
    
    def frenar(self):
        pass

# Multiples objetos.

coche1=Coches()
coche2=Coches()
coche3=Coches()

# Coche 1

coche1.marca="VW"
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
coche1.num_serie="183948192HSD" # Puede existir un atributo publico.

print(f"\n\tCoche 1: ")
print(f"Marca: {coche1.marca}")
print(f"Color: {coche1.getColor()}")
print(f"Modelo: {coche1.getModelo()}")
print(f"Velocidad: {coche1.getVelocidad()}")
print(f"Caballaje: {coche1.getCaballaje()}")
print(f"Plazas: {coche1.getPlazas()}")

# Coche 2

coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f"\n\tCoche 2:")
print(f"Marca: {coche2.getMarca()}")
print(f"Color: {coche2.getColor()}")
print(f"Modelo: {coche2.getModelo()}")
print(f"Velocidad: {coche2.getVelocidad()}")
print(f"Caballaje: {coche2.getCaballaje()}")
print(f"Plazas: {coche2.getPlazas()}")

# Coche 3

coche3.marca="Honda"

print(f"\n\tCoche 3: ")
print(f"Marca: {coche3.marca}")