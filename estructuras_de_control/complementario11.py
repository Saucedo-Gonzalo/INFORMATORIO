"""Determinar si un alumno aprueba a reprueba un curso, 
sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario."""

nota1=float(input("INGRESE LA NOTA:\t"))
nota2=float(input("INGRESE LA NOTA:\t"))
nota3=float(input("INGRESE LA NOTA:\t"))

prom=(nota1+nota2+nota3)/3

if prom>70:
    print("APROBADO")
else:
    print("DESAPROBADO")

