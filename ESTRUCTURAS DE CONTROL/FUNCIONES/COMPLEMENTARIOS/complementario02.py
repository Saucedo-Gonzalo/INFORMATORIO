"""En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 
por cada 140 metros recorridos. Escriba una función que tome la distancia recorrida (en kilómetros) 
como su único parámetro y devuelva la tarifa total como su único resultado. Escriba un programa principal que 
use la función.

Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas así el 
programa podrá actualizar fácilmente cuando las tasas aumentan. """

def tarifa(x):
    TARIFA=15
    TARIFA_BASE=40
    recorrido=((x*1000)//140)*TARIFA+ TARIFA_BASE
    return recorrido


print("\n-----Bienvenido al TAXI-----\n")
km = float(input("Ingrese los KM recorridos: "))
print("Su total es de: $", tarifa(km))
print("\n-----Fin del recorrido-----\n")
