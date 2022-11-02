"""Las palabras como primero, segundo y tercero se refieren a números ordinales. En este ejercicio, 
escribirá una función que toma un número entero como su único parámetro y devuelve una cadena que contiene 
el número ordinal apropiado como único resultado. Su función debe manejar los enteros entre 1 y 12 (inclusive).
 Debería devolver una cadena vacía si se proporciona un valor fuera de este rango como parámetro. Incluya un
  programa principal que utilice su función mostrando cada número entero del 1 al 12 y su número ordinal."""

def ordinal(x):
    if x==1:
        ord='PRIMERO'
    elif x==2:
        ord='SEGUNDO'
    elif x==3:
        ord='TERCERO'
    elif x==4:
        ord='CUARTO'
    elif x==5:
        ord='QUINTO'
    elif x==6:
        ord='SEXTO'
    elif x==7:
        ord='SEPTIMO'
    elif x==8:
        ord='OCTAVO'
    elif x==9:
        ord='NOVENO'
    elif x==10:
        ord='DECIMO'
    elif x==11:
        ord='DECIMO PRIMERO'
    elif x==12:
        ord='DECIMO SEGUNDO'
    else:
        ord=''
    return ord    


print("\n-----Bienvenido al SISTEMA-----\n")

for x1 in range(1,13):
    print(f"El ordinal del número {x1} es:", ordinal(x1))


print("\n-----Fin del programa-----\n")