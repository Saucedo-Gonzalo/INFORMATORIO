"""Diseña un programa al que se proporcione como entradas dos enteros y un carácter. 
El programa deberá sumar, restar, multiplicar o dividir los valores de los dos primeros parámetros
 dependiendo del código indicado en el tercer parámetro, y devolver el resultado. 
Por ejemplo si el usuario ingresa la opción “S”, se deberán sumar los números."""
import sys
resp='S'


while resp.upper()== 'S':
    num1=int(input('INGRESE EL PRIMER ENTERO\t'))
    num2=int(input('INGRESE EL SEGUNDO ENTERO\t'))
    opc=input('INGRESE LA OPCION DESEADA: \n +SUMA--> S\n -RESTA --> R \n *MULTIPLICAR --> M\n DIVIDIR --> D \n')
    opc=opc.upper()

    if opc == 'S':
        result = num1+num2
    elif opc == 'R':
        result = num1-num2
    elif opc == 'M':
        result = num1*num2
    elif opc == 'D':
        result = num1/num2
    else:
        print ('LA OPCION INGRESADA ES INCORRECTA, VUELVA A INGRESAR LOS DATOS')
        continue
    
    print(f'EL RESULTADO DE LA OPERACION DESEADA ES: {result}')

    resp=input('SI DESEA SEGUIR EN EL PROGRAMA PRESIONE S')