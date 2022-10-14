#1 Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
#--------------------------------------------------------------------------------#

n1=int(input("INGRESE EL NUMERO 1:\t"))
n2=int(input("INGRESE EL NUMERO 1:\t"))
n3=int(input("INGRESE EL NUMERO 1:\t"))

if (n1>n2) and (n1>n3):
    print(n1)

    if (n2>n3): 
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
elif (n2>n1) and (n2>n3):
    print(n2)

    if (n1>n3):
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
else:
    print(n3)

    if (n2>n1):
        print(n2)
        print(n1)
    else:
        print(n1)
        print(n2)

