"""Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento. 
El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20% 
(solo existen dos claves)."""

nombre=input("INGRESE EL NOMBRE DEL PRODUCTO \n")
clave=input("INGRESE LA CLAVE (01 O 02):\n")

if clave=='01' or clave=='02':
    precio =float(input("INGRESE EL PRECIO\n"))
    if clave=='01':
        precio_desc=precio*0.9
    else:
        precio_desc=precio*0.8
    print(F"NOMBRE: {nombre}\n *CLAVE: {clave}\n *PRECIO: ${precio}\n *PRECIO CON DESCUENTO: ${precio_desc:.2f}")
else:
    print("ERROR, LA CLAVE NO ES CORRECTA")