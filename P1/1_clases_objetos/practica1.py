import os

"""
Practica 1: Implementar paradigma estructurado VS OO.
Crear un programa que obtenga el area de un rectangulo
"""

# 1. Estructurado

#def estRectangulo(base, altura):

#    area=base*altura
#    return area

#area = estRectangulo(6, 7)
#print(f"El area del rectangulo es la siguiente: {area}")

# 2. OO

os.system("cls")

class AreaRectangulo:

    def __init__(self, base, altura):
        self.base=base
        self.altura=altura


    def areaRectangulo(self):
        area=self.base*self.altura
        return area

rectangulo=AreaRectangulo(5,6) # Instanciar un objeto en la clase "AreaRectangulo"

print(f"El area del rectangulo es la siguiente: {rectangulo.areaRectangulo()}")