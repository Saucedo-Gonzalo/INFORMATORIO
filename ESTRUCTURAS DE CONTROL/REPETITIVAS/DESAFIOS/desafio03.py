"""En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la 
caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la caja le entregan un código de 
descuento que se aplicará sobre el total de su compra. Determinar la cantidad que pagara cada cliente desde
 que la tienda abre hasta que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es 
blanca no obtendrá descuento."""

opc='A'
tot=0

while opc.upper() != 'Z':
    monto=float(input('\nINGRESE EL MONTO DE LA COMPRA: \t'))
    color =input('INGRESE UN COLOR: \n *ROJO--> R\n *AMARILLO --> A\n *BLANCA--> B\n')
    color=color.upper()
    while color!='A' and color!='R' and color!='B':
        print('ERROR, INGRESE UN COLOR VALIDO')
        color =input('INGRESE UN COLOR: \n *ROJO--> R\n *AMARILLO --> A\n *BLANCA--> B\n')
        color=color.upper()

    if color == 'A':
        desc=0.75
    elif color == 'B':
        desc=1
    else:
        desc=0.60

    tot+=monto*desc
    print('-----------------------------------------------------------------------')
    print (f'\nEL MONTO A PAGAR POR EL CLIENTE es: ${(monto*desc):.2f}')

    opc=input('PARA FINALIZAR PRESIONE Z, PARA SEGUIR CUALQUIER OTRO CARACTER')
else:
    ('______________________________________________________________________')
    print (f'\n RECAUDACION DEL DIA: ${(tot):.2f}')
    
    