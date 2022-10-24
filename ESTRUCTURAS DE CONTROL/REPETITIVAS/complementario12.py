"""Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. Debe diseñar un programa que permita
 monto por cliente y el total recaudado por la gasolinera, tomando en cuenta lo siguiente:
• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
• El programa finaliza cuando se introduce una D como tipo de gasolina."""

monto=1
tot=0
tipo=''
while tipo!='D':
    tipo=(input('*INGRESE EL TIPO DE CLIENTE:\n A\n B\n C\n D (para salir)\n ')).upper()
    if tipo=='A':
        litros=float(input("INGRESE LOS LITROS CARGADOS:\t"))
        monto=50*litros
        print(f'\n*EL MONTO A PAGAR POR EL CLIENTE ES: ${monto}')
        tot+=monto
    elif tipo=='B':
        litros=float(input("INGRESE LOS LITROS CARGADOS:\t"))
        monto=55*litros
        print(f'\n*EL MONTO A PAGAR POR EL CLIENTE ES: ${monto}')
        tot+=monto
    elif tipo=='C':
        litros=float(input("INGRESE LOS LITROS CARGADOS:\t"))
        monto=60*litros
        print(f'\n*EL MONTO A PAGAR POR EL CLIENTE ES: ${monto}')
        tot+=monto
    elif tipo=='D':
        print(f'TOTAL DEL DIA: ${tot}')
    else:
        print('INGRESE UN TIPO VALIDO')
        continue

