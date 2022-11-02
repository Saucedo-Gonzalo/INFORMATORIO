#1) Determinar el número mayor de 10 números ingresados.
mayor=0
for i in range(10):
    num=int(input('INGRESE UN NUMERO: \t'))
    if num> mayor:
        mayor=num
        pos=i+1

print (f"EL MAYOR NUMERO ES: {mayor} \n FUE EL NUMERO {pos} INGRESADO")
