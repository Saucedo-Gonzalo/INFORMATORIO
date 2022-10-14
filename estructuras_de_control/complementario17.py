"""Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media de las personas adultas de su sexo, 
siendo:
- estatura media de mujeres adultas: 1,65 m.
- estatura media de varones adultos: 1,72 m."""

altura=float(input("INGRESE LA ALTURA:\t"))
sexo=input("INGRESE SEXO (M O V):\t")
bandera=False

if (sexo=='M' and altura>1.65) or (sexo=='V' and altura>1.72):
    bandera=True

if bandera==False:
    print("LA PERSONA NO TIENE MAYOR ESTATURA QUE LA MEDIA")
else:
    print("LA PERSONA TIENE MAYOR ESTATURA QUE LA MEDIA")