"""Un número primo es un número entero mayor que 1 que solo es divisible por uno y por sí mismo.
Escriba una función que determine si su parámetro es primo o no, devolviendo True si lo es y False en caso
contrario. Escriba un programa principal que lea un número entero del usuario y muestre un mensaje que
indique si es primo o no. Asegúrese de 
que el programa principal no se ejecutará si el archivo que contiene su solución se importa a otro programa."""


def primo (num):
   cont=0
   for i in range(num):
      if num%(i+1) == 0:
         cont+=1
   if cont>2:
      return False
   else:
      return True


print("\n-----Bienvenido al SISTEMA-----\n")
num=int(input('INGRESE UN NUMERO PARA VERIFICAR SI ES PRIMO:\t'))
print("\n---------------------------------------------------------------------------------\n")
print (primo(num))
print("\n-----Fin del programa-----\n")