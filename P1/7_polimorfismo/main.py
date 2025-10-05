import os
from coches import *

def datosGenerales(tipo):
    print(f"\n\t\t..: Ingresar los datos del vehiculo tipo: {tipo} :..")
    marca=input(f"\nMarca: ").upper()
    color=input(f"\nColor: ").upper()
    modelo=input(f"\nModelo: ").upper()
    velocidad=int(input(f"\nVelocidad: "))
    potencia=int(input(f"\nPotencia: "))
    plazas=int(input(f"\nPlazas: "))
    return marca, color, modelo, velocidad, potencia, plazas

def imprimirGenerales(marca, color, modelo, velocidad, potencia, plazas):
    print(f"\n\t\tDatos del Vehiculo: ")
    print(f"\nMarca: {marca}")
    print(f"Color: {color}")
    print(f"Modelo: {modelo}")
    print(f"Velocidad: {velocidad}")
    print(f"Potencia: {potencia}")
    print(f"Plazas: {plazas}")

def autos():
    os.system("cls")
    marca, color, modelo, velocidad, potencia, plazas=datosGenerales("Auto")
    coche=Coches(marca, color, modelo, velocidad, potencia, plazas)
    
    imprimirGenerales(marca, color, modelo, velocidad, potencia, plazas)

def camiones():
    os.system("cls")
    marca, color, modelo, velocidad, potencia, plazas=datosGenerales("Camion")
    
    eje=int(input(f"\nEjes: "))
    capacidadCarga=int(input(f"\nCapacida de Carga: "))
    camion=Camiones(marca, color, modelo, velocidad, potencia, plazas, eje, capacidadCarga)
    
    imprimirGenerales(marca, color, modelo, velocidad, potencia, plazas)
    print(f"# Eje: {camion.eje}")
    print(f"Capacidad de Carga: {camion.capacidadCarga}")

def camionetas():
    os.system("cls")
    marca, color, modelo, velocidad, potencia, plazas=datosGenerales("Camionetas")
    
    traccion=int(input(f"\nTraccion: "))
    cerrada=input(f"\n¿Cerrada? (SI/NO) ").upper()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False
    camioneta=Camionetas(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada)

    imprimirGenerales(marca, color, modelo, velocidad, potencia, plazas)
    print(f"Traccion: {camioneta.traccion}")
    print(f"Cerrada: {camioneta.cerrada}")

def espereTecla():
    input(f"\n\tOprima ENTER para continuar")

os.system("cls")

def main():

    opcion=True
    while opcion:
    
        os.system("cls")
        
        opcion=input(f"\n\t\t..: Menu Principal :..\n\n1.- Autos\n2.- Camionetas\n3.- Camiones\n4.- Salir\n\n\tElige una opcion: ").lower().strip()

        match opcion:
            
            case "1": # Menu autos.
                autos()
                espereTecla()
            
            case "2": # Menu camionetas.
                camionetas()
                espereTecla()
            
            case "3": # Menu camiones.
                camiones()
                espereTecla()
            
            case "4": # Salir
                os.system("cls")
                print(f"\n\t\t..: ¡Gracias por usar el SW! :..\n")
                espereTecla()
                opcion=False
            
            case _: # Opcion invalida
                os.system("cls")
                print(f"\n\t\tOpcion no valida... Vuelva a intentarlo.\n")
                espereTecla()
                opcion=True

if __name__=="__main__":
    main()