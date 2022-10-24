"""Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. El programa
 no permitirá introducir valores negativos para A y B y verificará que A es menor que B. Si A es mayor que B, 
se deben intercambiar los valores."""

import sys

numA=int(input("INGRESE UN NUMERO A: \t"))
numB=int(input("INGRESE UN NUMERO B: \t"))

while numA<0:
    numA=int(input("INGRESE UN NUMERO POSITIVO A: \t"))

while numB<0:
    numB=int(input("INGRESE UN NUMERO POSITIVO B: \t"))

if numA>numB:
    aux=numA
    numA=numB
    numB=aux
suma=0

for numero in range(numA,numB):
    if numero % 5==0:
        suma+=numero

print(f"\nLA SUMA DE LOS MULTUPLOS DE 5 COMPRENDIDOS ENTRE {numA} Y {numB} ES: {suma}")