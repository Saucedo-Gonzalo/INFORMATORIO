"""Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee."""

resp='S'
suma=0
while resp.upper()=='S':
    cant=float(input("INGRESE LA CANTIDAD: \t"))
    precio=float(input("INGRESE EL PRECIO: \t"))
    suma+=cant*precio
    resp=input("\nSI DESEA INGRESAR OTRO PRODUCTO PRESIONE S, CASO CONTRARIO PRESIONE CUALQUIER TECLA\t")
else:
    print(f"EL TOTAL DE LA COMPRA ES: ${suma:.2f}")

    print("\n-----------SUPERMERCADO EL INGENIERO------------ " )



