"""Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe un diagrama que lea por cada estudiante la calificación 
obtenida y calcule e imprima:

A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.

B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 80.

C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.

D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más."""

contA=0
contB=0
contC=0
contD=0

for i in range(100):
    nota=float(input("INGRESE LA NOTA OBTENIDA:\t"))
    if nota<50:
        contA+=1
    elif nota>=50 and nota<80:
        contB+=1
        if nota>=70:
            contC+=1
    elif nota>=80:
        contD+=1

print(f'NOTAS EN PORCENTAJES:\n *MENOR A 50: {contA}\n *MAYOR A 50 Y MENOR A 80: {contB} \n *MAYOR A 70 Y MENOR A 80: {contC} \n *MAYOR A 80: {contD} \n')
