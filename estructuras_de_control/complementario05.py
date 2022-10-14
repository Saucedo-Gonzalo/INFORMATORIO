"""Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, de 
acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

Si A>=B + C à No se trata de un triángulo

Si A^2 = B^2 + C^2 à Es un triángulo rectángulo

Si A^2 > B^2 + C^2 à Es un triángulo obtusángulo

Si A^2 < B^2 + C^2 à Es un triángulo acutángulo"""


l1=int(input("INGRESE EL LADO 1:\t"))
l2=int(input("INGRESE EL LADO 2:\t"))
l3=int(input("INGRESE EL LADO 3:\t"))

if (l1>=(l2+l2)):
    print("NO ES UN TRIANGULO")
elif  (l1**2)==(l2**2+l3**2):
    print("ES UN TRIANGULO RECTÁNGULO")

elif  (l1**2)>(l2**2+l3**2):
    print("ES UN TRIANGULO OBTUSÁNGULO")
    
elif  (l1**2)<(l2**2+l3**2):
    print("ES UN TRIANGULO ACUTÁNGULO")

