"""Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento y $ 2.95
 para cada segundo elemento posterior. Escriba una función que tome el número de elementos en el pedido como
  su único parámetro. Devuelva los gastos de envío del pedido como resultado de la función. Incluya un programa 
principal que lea la cantidad de artículos comprados al usuario y muestre los gastos de envío."""

def envio(elemento):
    base=10.95
    extra=2.95
    if elemento>1:
        precio=base+(extra*(elemento-1))
    else:
        precio=base
    return precio

print("\n-----Bienvenido al SISTEMA DE ENVIOS-----\n")
cant = float(input("Ingrese la cantidad de elementos a enviar:\t"))
print(f"Su total es de: $ {envio(cant):.2f}")
print("\n-----Fin del programa-----\n")