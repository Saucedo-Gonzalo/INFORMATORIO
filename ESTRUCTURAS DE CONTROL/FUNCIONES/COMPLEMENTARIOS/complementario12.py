"""En este ejercicio creará una función llamada proximo_primo que encuentra y devuelve el primer número primo mayor que algún número entero, n. 
El valor de n se pasará a la función como su único parámetro. 
Incluya un programa principal que lea un número entero del usuario y muestre el primer número primo mayor que el valor ingresado."""

def proximo_primo(num):
    cont=0
    while cont!=2:
        cont=0
        for i in range(1,(num+1)):
            if num%(i)==0:
                cont+=1

        num=num+1
    else:
        sal=num-1

    return sal

print("\n-----Bienvenido al SISTEMA-----\n")
num=int(input('INGRESE UN NUMERO PARA ENCONTRAR EL PROXIMO PRIMO:\t'))
print("\n---------------------------------------------------------------------------------\n")
print (proximo_primo(num))
print("\n-----Fin del programa-----\n")




    



