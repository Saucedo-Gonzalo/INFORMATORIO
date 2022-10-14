"""Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por cantidad según el siguiente criterio:
    i.      a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.
    ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.
 El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. Dado el importe bruto de una compra de libros,
 el tipo de cliente de que se trata y la cantidad total pedida por el mismo, determinar el importe bruto bonificado."""

importe=float(input("INGRESE EL IMPORTE DE LA COMPRA\n"))
tipo_cliente=input("INGRESE EL TIPO DE CLIENTE (L O P)\n")
cant=int(input("CANTIDAD DE LIBROS\n"))

if tipo_cliente.upper() == 'L':
    if cant >24:
        importe=importe*0.75
    else:
        importe=importe*0.8
elif tipo_cliente.upper() == 'P':
    if cant>5 and cant<=18:
        importe=importe*0.95
    elif cant>18:
        importe=importe*0.90

print(f"EL MONTO BONIFICADO ES: ${importe:.2f}")
print("---------FIN DEL PROGRAMA------------")

