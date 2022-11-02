"""Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en dispositivos
 pequeños como teléfonos inteligentes. En este ejercicio, escribirá una función que capitaliza los caracteres
  apropiados en una cadena. Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y 
  seguida de un espacio. El primer carácter de la cadena también debe estar en mayúscula, así como el primer 
  carácter no espacial después de un ".", "!" o "?" Por ejemplo, si la función se proporciona con la cadena 
  "¿a qué hora tengo que estar allí? ¿cuál es la dirección?" entonces debería devolver la cadena "¿A qué hora 
  tengo que estar allí? ¿Cuál es la dirección?". Incluya un 
programa principal que lea una cadena del usuario, la capitalice utilizando su función y muestre el resultado."""

def prim_mayus (cadena):
    cont=0
    sal=''
    for i in(cadena):  
        if i.isalpha() and cont==0:
            sal =sal + i.upper()
            cont=1
        else:
            sal=sal+ i
     #si ocupo capitalize() no cubre el caso en el que tenga por ej, ¿hola? hace mayus el ¿ y no la h.
    return sal

print("\n-----Bienvenido al SISTEMA-----\n")
cadena=input("INGRESE UNA CADENA POR FAVOR: \t")
print("\n---------------------------------------------------------------------------------\n")
print (prim_mayus(cadena))
print("\n-----Fin del programa-----\n")

