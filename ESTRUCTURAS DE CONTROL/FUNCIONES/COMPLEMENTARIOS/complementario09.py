"""En este ejercicio escribirá una función llamada es_entero que determina si los caracteres en una cadena 
representan un número entero válido. Al determinar si un string representa un número entero, debe ignorar 
cualquier espacio en blanco inicial o final. Una vez que se ignora este espacio en blanco, una cadena 
representa un número entero si su longitud es al menos 1 y solo contiene dígitos, o si su primer carácter 
es + o - y el primer carácter va seguido de uno o más caracteres, todos los cuales son dígitos Escriba un 
programa principal que lea una cadena del usuario e informe si representa o no un número entero.

Sugerencia: Puede encontrar los métodos lstrip, rstrip y / o strip para cadenas útiles cuando complete este
 ejercicio."""

#metodo lstrip se utiliza para eliminar todos los espacios en blanco iniciales 
#metodo rstrip devuelve una nueva cadena con los espacios en blanco del final eliminados.
#metodo strip se utiliza para eliminar todos los espacios en blanco iniciales y finales de una cadena. También tiene en cuenta los tabuladores y saltos de línea.

def es_entero(cadena):
    cadena = cadena.strip()
    resp=True
    cont=0
    for i in(cadena):
        if i.isdigit() ==False:
            if i!='+' and i!='-':
                resp=False
                break
            else:
                cont+=1
                if cont>1: #para que no ponga por ej: ++-87
                    resp=False
                    break
                
    return resp        

    
print("\n-----Bienvenido al SISTEMA-----\n")
cadena=input("INGRESE UNA CADENA POR FAVOR: \t")
print("\n---------------------------------------------------------------------------------\n")
print (es_entero(cadena))
print("\n-----Fin del programa-----\n")