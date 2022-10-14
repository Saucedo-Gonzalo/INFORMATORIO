"""Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. 
Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida."""

p1=float(input("INGRESE EL PRIMER MONTO:\t"))
p2=float(input("INGRESE EL SEGUNDO MONTO:\t"))
p3=float(input("INGRESE EL TERCER MONTO:\t"))

monto=p1+p2+p3

p1=(p1*100)/monto
p2=(p2*100)/monto
p3=(p3*100)/monto

print(f"PORCENTAJE INVERTIDO:\n *PERSONA 1: {p1:.2f}%\n *PERSONA 2: {p2:.2f}%\n *PERSONA 3: {p3:.2f}%")