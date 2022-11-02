#3) Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.

A=int(input("INGRESE UN VALOR PARA LA VARIABLE: \t "))
B=int(input("INGRESE UN VALOR PARA LA VARIABLE: \t "))
result=0

for i in range(A):
    result+=B

print ('\nRESULTADO: ',result)