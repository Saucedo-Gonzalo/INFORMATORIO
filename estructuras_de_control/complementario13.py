"""En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge 
al azar. Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, si es mayor
 o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta."""

monto=float(input("INGRESE EL MONTO TOTAL DE LA COMPRA\t"))
numero=int(input("INGRESE EL NUMERO ELEGIDO\t"))

if numero<74:
    desc=monto*0.15
else:
    desc=monto*0.20

print(f"POR LA COMPRA DE ${monto}, GRACIAS AL NUMERO QUE ELIGIO, SE LE REALIZARÁ UN DESCUENTO DE ${desc:.2f}")

