"""Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. Una pizza puede ser sencilla (con sólo salsa y carne),
 o con ingredientes extras, tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule el precio de venta de una pizza, 
 dándole el tamaño y el número de ingredientes extras. El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño, más
  el número de ingredientes. En particular el costo total se calcula sumando:

- un costo fijo de preparación.

- un costo variable que es proporcional al tamaño de la pizza.

- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo)."""


costoPrep=float(input("INGRESAR EL COSTO FIJO DE PREPARCIÓN:\t"))

costoPeq=float(input("INGRESE EL COSTO VARIBLE PROPORCIONAL DE LA PIZZA DE TAMAÑO PEQUEÑO:\t "))
costoMed=float(input("INGRESE EL COSTO VARIBLE PROPORCIONAL DE LA PIZZA DE TAMAÑO MEDIANO:\t"))
costoGra=float(input("INGRESE EL COSTO VARIBLE PROPORCIONAL DE LA PIZZA DE TAMAÑO GRANDE:\t"))

costoExtra=float(input("INGRESE EL COSTO EXTRA POR CADA INGREDIENTE:\t"))

resp='S'

while resp.upper()=='S':
    tam=input("INGRESE EL TAMAÑO DE LA PIZZA: \n 1) PEQUEÑA \n 2) MEDIANA \n 3) GRANDE\n")
    ingExtra=int(input("INGRESE EL NUMERO DE INGREDIENTES EXTRAS: \t"))
    if tam=='1':
        costoTot=costoPeq+costoPrep+(costoExtra*ingExtra)
    elif tam=='2':
        costoTot=costoMed+costoPrep+(costoExtra*ingExtra)
    elif tam=='3':
        costoTot=costoGra+costoPrep+(costoExtra*ingExtra)
    else:
        print("INGRESE UN NUMERO PARA EL TAMAÑO DE PIZZA VALIDO")
        continue

    costoTot=costoTot*1.5
    print(f"EL PRECIO DE LA PIZZA ES: ${costoTot}")
    resp =input("DESEA REALIZAR OTRA VENTA? S/N \n")