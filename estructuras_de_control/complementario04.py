#4 Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
#--------------------------------------------------------------------------------#
n1=int(input("INGRESE EL DIVIDENDO:\t"))
n2=int(input("INGRESE EL DIVISOR:\t"))

if (n2==0):
    print("no se puede dividir entre cero")
else:
    if n1%n2==0:
        print(f"EL NUMERO {n1} ES DIVISOR DE {n2}")