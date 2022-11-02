""" Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le 
asigna como un porcentaje de su salario mensual que depende de su antigüedad en la empresa de acuerdo con la
 sig. tabla:

Tiempo												Utilidad

Menos de 1 año							    	5% del salario

Más de 1 año y hasta 2 años		                 7% del salario

Más de 2 años y hasta 5 años                     10% del salario

Más de 10 años							    	 20% del salario"""

resp='S'

while resp.upper()== 'S':
    nombre=input('INGRESE EL NOMVRE DEL TRABAJADOR\t')
    salario=float(input('INGRESE EL SALARIO MENSUAL DEL TRABAJADOR\t'))
    anios=float(input('INGRESE LA ANTIGÜEDAD DEL TRABAJADOR\t'))

    if anios<1:
        utilidad=salario*0.05
    elif anios<=2:
        utilidad=salario*0.07
    elif anios<=5:
        utilidad=salario*0.10
    elif anios>10:
        utilidad=salario*0.20
    else:
        utilidad=0
    
    print(f'*TRABAJADOR: {nombre}\n -ANTIGÜEDAD: {anios}\n -UTILIDAD: ${utilidad}\n')
    resp=input('SI DESEA SEGUIR EN EL PROGRAMA PRESIONE S')
