#Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.

num=int(input("INGRESE UN NUMERO : \t"))

for i in range(num):
    if num%(i+1) ==0:
        print(f'*EL NUMERO {num} ES DIVISOR DE {i+1}\n')