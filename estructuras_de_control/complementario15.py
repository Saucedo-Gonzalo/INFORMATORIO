"""Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
i. Si trabaja 40 horas o menos se le paga $16 por hora
ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra."""

horas=int(input("INGRESE LAS HORAS TRABAJADAS: \t"))  

if horas<41:
    pago=horas*16
else:
    extra=(horas-40)*20
    pago=(40*16)+extra

print(f"EL SALARIO SEMANAL ES DE: ${pago}")