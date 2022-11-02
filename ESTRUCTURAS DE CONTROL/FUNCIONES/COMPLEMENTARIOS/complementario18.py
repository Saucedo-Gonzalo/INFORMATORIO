"""Escriba una función que determine mostrar cuántos días hay en un mes en particular. Su función tomará dos parámetros:
 el mes como un número entero entre 1 y 12, y el año como un número entero de cuatro dígitos. Asegúrese de que su función informa el número
  correcto de días en febrero para los años bisiestos.
 Incluya un programa principal que lea un mes y un año del usuario y muestre el número de días en ese mes."""

def dias(mes,anio):
    meses31=[1, 3, 5, 7, 8, 10, 12 ]
    if mes in meses31:
        dias=31
    else:
        if (mes ==2):
            if (anio % 4==0):
                dias=29
            else: 
                dias=28
        else:
            dias=30
    return print(f'EL MES {mes} TIENE {dias} DIAS')



print("\n-----Bienvenido al SISTEMA-----\n")
mes=int(input('INGRESE EL MES CON NUMEROS:\t'))
anio=int(input('INGRESE EL AÑO CON EL FORMATO AAAA:\t'))
print("\n---------------------------------------------------------------------------------\n")
dias(mes,anio)
print("\n-----Fin del programa-----\n")






