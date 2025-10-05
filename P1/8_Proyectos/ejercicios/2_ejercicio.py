"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el metodo __init__.
Calcular despues la suma, resta, multiplicacion y division. Utilizar un metodo para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
"""

class Calculadora:
    
    def __init__(self):

        self._num1 = int(input(f"\n\tNumero 1: "))
        self._num2 = int(input(f"\tNumero 2: "))
    
    # Metodos Setters y Getters

    @property
    def numero1(self):
        return self._num1
    @numero1.setter
    def numero1(self, num1):
        self.numero1=num1

    @property
    def numero2(self):
        return self._num2
    @numero2.setter
    def numero2(self, num2):
        self.numero2=num2

    # Metodos

    def sumar(self):
        return self._num1+self._num2
    
    def restar(self):
        return self._num1-self._num2
    
    def multiplicar(self):
        return self._num1*self._num2
    
    def dividir(self):
        return self._num1/self._num2
    
operacion=Calculadora() # Objeto

print(f"{operacion.numero1} + {operacion.numero2} = {operacion.sumar()}") # Metodo sumar
operacion.restar() # Metodo restar
operacion.multiplicar() # Metodo multiplicar
operacion.dividir() # Metodo dividir