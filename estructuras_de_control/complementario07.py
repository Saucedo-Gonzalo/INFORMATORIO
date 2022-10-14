"""7 Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. 
Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde."""
#--------------------------------------------------------------------------------#

compra=float(input("INGRESE EL MONTO DE LA COMPRA\n"))

if compra>1000:
    monto_desc=compra*0.85
    descuento=compra*0.15
    print(f"EL MONTO TOTAL DE LA COMPRA ES: $",format(monto_desc,'.2f'))
    print(f" EL DESCUENTO OBTENIDO EN PESOS ES: $",format(descuento,'.2f'))
else:
    print(f"EL MONTO TOTAL DE LA COMPRA ES: $",format(compra,'.2f'))
