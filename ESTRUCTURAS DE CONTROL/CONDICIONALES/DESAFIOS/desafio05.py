"""La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio
(CÉNTRICO y NO CÉNTRICO) La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a 
M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra."""
import sys #para el que largue el error

nombre=input("Nombre del barrio: \t")
tipo=input("Tipo del barrio (1. CENTRICO 2. NO CÉNTRICO): \t")

prim= nombre[0]
seccion='B'
if tipo =='1':
    if prim.upper() <'M':
        seccion= 'A'
elif tipo =='2':
    if prim.upper()>='M':
        seccion= 'A'
else:
    sys.exit('caracter invalido')
    

print(f"EL BARRIO {nombre} PERTENECE A LA SECCION: {seccion}")