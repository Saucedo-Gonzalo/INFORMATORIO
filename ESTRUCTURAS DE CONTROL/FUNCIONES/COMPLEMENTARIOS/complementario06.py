"""Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de la terminal
en caracteres como segundo parámetro. Su función debe devolver una nueva cadena que consta de la cadena 
original y el número correcto de espacios iniciales para que la cadena original aparezca centrada dentro
del ancho proporcionado cuando se imprima. No agregue ningún carácter al final de la cadena.
Incluya un programa principal que use su función."""


def centrado(cadena,ancho):
    espacio=' '
    cadena_cent=espacio*ancho+cadena
    return cadena_cent




print("\n-----Bienvenido al SISTEMA-----\n")
cadena=input("INGRESE LA CADENA:\t")
ancho=int(input("INGRESE EL ANCHO:\t"))
print("---------------------------------------------------------------------------------")
print(centrado(cadena,ancho))
print("\n-----Fin del programa-----\n")