# Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee.

resp='S'
cont=0
while resp.upper()=='S':  
    ladoA=float(input('INGRESE LA MEDIDA DEL LADO A: \n'))
    ladoB=float(input('INGRESE LA MEDIDA DEL LADO B: \n'))
    ladoC=float(input('INGRESE LA MEDIDA DEL LADO C: \n'))
    suma=ladoA+ladoB+ladoC
    cont+=1
    print(f'*EL PERIMETRO DEL TRIANGULO NUMERO {cont} INGRESADO ES: {suma}\n')
    resp=input('PARA CONTINUAR PRESIONE S, PARA SALIR CUALQUIER OTRO CARACTER\n')
