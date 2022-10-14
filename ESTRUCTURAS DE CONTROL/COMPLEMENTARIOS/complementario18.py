"""Se leen tres números que son las longitudes de los lados de un triángulo.
 Determinar e informar si el mismo es equilátero (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados distintos)."""


A = int(input('Ingrese L1 \n'))
B = int(input('Ingrese L2 \n'))
C = int(input('Ingrese L3 \n'))

if A == B == C:
    print('Triángulo equilátero')
elif ((A == B) or (A == C) or (B == C)):
    print('Triángulo isósceles')
else:
    print('Triángulo escaleno')