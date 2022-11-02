"""Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus
parámetros y devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como resultado
de la función. Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo
rectángulo del usuario, use su función para calcular la longitud de la hipotenusa y muestre el resultado."""

import math

def triangulo (ladoA, ladoB):
    hipotenusa= math.sqrt(ladoA**2+ladoB**2)
    return hipotenusa

print("\n-----Bienvenido al PITAGORAS-SYSTEMS-----\n")
ladoA = float(input("Ingrese el lado A:\t "))
ladoB = float(input("Ingrese el lado B:\t "))
print("El resultado es:",triangulo(ladoA, ladoB))
print("\n-----Fin del programa-----\n")