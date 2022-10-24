# Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. 
# El ciclo debe finalizar cuando el usuario ingresa 0.

num=int(input("INGRESE UN NUMERO PARA VERICAR (PARA FINALIZAR PRESIONE 0)\n"))

while num>0:
    if num%2==0:
        print (f'EL NUMERO {num} ES PAR')
    else:
        print (f'EL NUMERO {num} ES IMPAR')
    num=int(input("INGRESE UN NUMERO PARA VERICAR (PARA FINALIZAR PRESIONE 0)\n"))
else:
    print ('------------------FIN DEL PROGRAMA-------------------')