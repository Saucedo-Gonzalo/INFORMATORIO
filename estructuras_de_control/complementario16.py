"""Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas 
se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%."""

compra=input("SI DESEA REALIZAR UNA COMPRA INGRESE S, CASO CONTRARIO N\n")
cont=0
total=0 

while compra=='S':
    cont+=1
    precio=float(input("INGRESE EL PRECIO DE LA CAMISA:\t"))
    total+=precio
    compra=input("SI DESEA REALIZAR UNA COMPRA INGRESE S, CASO CONTRARIO N\n")

if cont>2:
    total=total*0.8
else:
    total=total*0.9  

if total!=0:
    print(f"\n*EL TOTAL DE LA COMPRA DE LAS {cont} CAMISAS ES: ${total:.2f} ")

print("------------------------FIN DEL PROGRAMA--------------------------")   
