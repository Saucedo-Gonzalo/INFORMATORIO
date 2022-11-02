""" Escribir un programa el cual lea dos valores enteros. Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''.
 Si el segundo es menor que el primero, que imprima el mensaje ``Abajo''. Si los números son iguales, que imprima el mensaje ``igual''.
 Si alguno de los datos ingresados es igual a 0, que imprima un mensaje conteniendo la palabra ``Error''."""
num1=0
num2=0
resp='S'

while resp.upper() == 'S':
    num1=int(input("INGRESE EL NUMERO 1:\t"))
    num2=int(input("INGRESE EL NUMERO 2:\t"))
    
    
    if num1==0 or num2==0:
        print("ERROR")
    elif num1<num2:
        print("ABAJO")
    elif num1>num2:
        print("ARRIBA")
    elif num1==num2:
        print("IGUAL")
    
    resp =input("DESEA SEGUIR? S/N \n")

    

