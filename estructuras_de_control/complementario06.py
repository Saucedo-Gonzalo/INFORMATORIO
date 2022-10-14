"""Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. 
Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento

0 – 6000							15%

6000 – 7900					   10%

7900 – 12000					6%

Más de 12000				   0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, 
el sueldo actual y el sueldo aumentado."""

sueldo=float(input("INGRESE EL SUELDO DEL JUGADOR:\n"))

if sueldo<=6000:
    sueldo_nuevo=sueldo*1.15
    print(f"EL AUMENTO ES DEL 15%:\n *SUELDO ACTUAL: ${sueldo}\n *SUELDO ACTUALIZADO: $",format(sueldo_nuevo,'.2f'))
elif sueldo<=7900:
    sueldo_nuevo=sueldo*1.10
    print(f"EL AUMENTO ES DEL 10%:\n *SUELDO ACTUAL: ${sueldo}\n *SUELDO ACTUALIZADO: $",format(sueldo_nuevo,'.2f'))
elif sueldo<=12000:
    sueldo_nuevo=sueldo*1.06
    print(f"EL AUMENTO ES DEL 6%:\n *SUELDO ACTUAL: ${sueldo} \n *SUELDO ACTUALIZADO: $",format(sueldo_nuevo,'.2f'))
elif sueldo>12000:
    print(f"NO RECIBE AUMENTO:\n *SUELDO ACTUAL: ${sueldo}")