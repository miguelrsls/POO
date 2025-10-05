# Instanciar los objetos para posteriormente implementarlos.

from coches import *

num_coches=int(input(f"Cuantos coches deseas aladir? "))

for i in range(0,num_coches):
    print(f"\n\t.:: Datos del Coche {i+1} ::.\n")
    marca=input(f"Ingresa la marca del auto: ").upper()
    color=input(f"Ingresa el color del auto: ").upper()
    modelo=input(f"Ingresa el modelo del auto: ").upper()
    velocidad=int(input(f"Ingresa la velocidad del auto: "))
    potencia=int(input(f"Ingresa la potencia del auto: "))
    plazas=int(input(f"Ingresa las plazas del auto: "))

    coche1=Coches(marca, color, modelo, velocidad, potencia, plazas)

    print(f"\n\tCoche {i+1}: ")
    print(f"Marca: {coche1.marca}")
    print(f"Color: {coche1.getColor()}")
    print(f"Modelo: {coche1.getModelo()}")
    print(f"Velocidad: {coche1.getVelocidad()}")
    print(f"Caballaje: {coche1.getCaballaje()}")
    print(f"Plazas: {coche1.getPlazas()}")

    print(f"\n\n\t{coche1.acelerar()}")