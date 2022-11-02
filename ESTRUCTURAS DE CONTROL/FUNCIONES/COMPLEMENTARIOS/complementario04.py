"""Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros
 como resultado. Incluya un programa principal que lea tres valores del usuario y muestre su mediana.

Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. 
Se puede encontrar usando declaraciones if, o con un poco de creatividad matemática."""

def valor_medio(x1,x2,x3):
    if x1>=x2 and x1<=x3:
        result=x1
    elif x2>=x1 and x2<=x3:
        result=x2
    elif x3>=x1 and x3<=x2:
        result=x3
    return result

print("\n-----Bienvenido al SISTEMA-----\n")
x1 = float(input("Ingrese un valor numerico:\t"))
x2 = float(input("Ingrese un valor numerico:\t"))
x3 = float(input("Ingrese un valor numerico:\t"))
print(f"El valor medio es: {valor_medio(x1, x2, x3):.2f}")
print("\n-----Fin del programa-----\n")