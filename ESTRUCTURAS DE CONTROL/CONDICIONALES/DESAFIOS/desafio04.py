"""Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.
Ingredientes comunes: Verduras y berenjena.
Ingredientes Receta 1: Lentejas y apio.
Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los
 ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo
  de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes."""

receta = int(input('Ingrese que tipo de receta desea: \n 1. Receta ecológica 1 \n 2. Receta ecológica 2 \n'))

if receta == 1:
    print('Los ingredientes para elegir son: \n 1. Lentejas \n 2. Apio \n 3.Verduras \n 4. Berenjena. \n Solo puede elegir 3.')
    ingrediente1 = str(input('Ingrese ingrediente 1 \n'))
    ingrediente2 = str(input('Ingrese ingrediente 2 \n'))
    ingrediente3 = str(input('Ingrese ingrediente 3 \n'))
elif receta == 2:
    print('Los ingredientes para elegir son: \n 1. Morron \n 2. Cebolla \n 3. Verduras \n 4. Berenjena. \n Solo puede elegir 3.')
    ingrediente1 = str(input('Ingrese ingrediente 1 \n'))
    ingrediente2 = str(input('Ingrese ingrediente 2 \n'))
    ingrediente3 = str(input('Ingrese ingrediente 3 \n'))

if receta == 1:
   print('Ha elegido la receta ecológica 1, los ingredientes elegidos son',ingrediente1,ingrediente2,ingrediente3,'\n Referencias: \n 1. Morron \n 2. Cebolla \n 3. Verduras \n 4. Berenjena.')
elif receta == 2:
   print('Ha elegido la receta ecológica 2, los ingredientes elegidos son',ingrediente1,ingrediente2,ingrediente3,'\n 1. Morron \n 2. Cebolla \n 3. Verduras \n 4. Berenjena.')