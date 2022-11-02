"""Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al 
usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. """
import sys
"""PARTE A
password='43064998'  


password_input=input('INGRESE LA CONTRASEÑA:\t')

while password_input!=password:
    print('-----------------------------------------------------------------------')   
    print('CONTRASEÑA INCORRECTA, VUELVA A INGRESARLA\n')
    password_input=input('INGRESE LA CONTRASEÑA:\t')
else:
    print('INGRESO ACEPTADO')"""

#PARTE B

password='43064998'  
intentos=0

password_input=input('INGRESE LA CONTRASEÑA:\t')

while password_input!=password:
    intentos+=1
    if intentos>5:
        sys.exit('\nERROR, LA CUENTA QUEDO BLOQUEADA POR SEGURIDAD.')
    
    
    print('-----------------------------------------------------------------------')   
    print('CONTRASEÑA INCORRECTA, VUELVA A INGRESARLA\n')
    password_input=input('INGRESE LA CONTRASEÑA:\t')
else:
    print('INGRESO ACEPTADO')

    