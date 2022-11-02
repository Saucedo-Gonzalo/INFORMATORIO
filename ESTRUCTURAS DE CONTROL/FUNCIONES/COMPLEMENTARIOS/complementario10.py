"""Escriba una función llamada precedencia que devuelve un número entero que representa la precedencia de un
 operador matemático. Una cadena que contiene el operador se pasará a la función como su único parámetro. 
 Su función debe devolver 1 para + y -, 2 para * y /, y 3 para ˆ. Si la cadena que se pasa a la función no es 
 uno de estos operadores, la función debería devolver -1. Incluya un programa principal que lea un operador
  del usuario y muestre la precedencia del operador o un mensaje de error que indique que la entrada no era un 
  operador.

En este ejercicio, se usa ˆ para representar la exponenciación, en lugar de la elección de Python de **, 
para facilitar el desarrollo de la solución."""

def precedencia(cadena):
    if len(cadena)>1:
        cadena=input("INGRESE EL CARACTER DE LA OPERACIÓN POR FAVOR: \t")
    if cadena=='+' or cadena=='-':
        salida=1
    elif cadena=='*':
        salida=2
    elif cadena=='^':
        salida=3
    else:
        salida=-1

    return salida

cadena=input("INGRESE EL CARACTER DE LA OPERACIÓN POR FAVOR: \t")
print (precedencia(cadena))