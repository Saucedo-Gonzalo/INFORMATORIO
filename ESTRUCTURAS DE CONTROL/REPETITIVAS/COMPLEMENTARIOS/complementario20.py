"""El Centro de Salud de Rosario tiene registradas N consultas médicas de menores. De cada consulta tiene 
como datos: la edad del menor y el día de visita. Los datos están ordenados en forma creciente por día. 
Proponer un fin de datos para cada día. Se desea conocer, para cada día, la edad promedio de pacientes y 
además el día en que se registró el máximo de pacientes."""

tot=0
tot_fecha=0
acum_edad=0
tot_acum=0
maximo=0

fecha=input('INGRESE LA FECHA\t')
resg_fecha=fecha
while fecha!='0':    
    if resg_fecha== fecha:
        edad=int(input('INGRESE LA EDAD DEL MENOR:\t'))
                
        acum_edad+=edad
        tot_fecha+=1
        tot_acum+=edad
        tot+=1
        fecha=input('\nINGRESE LA FECHA \n(SI DESEA TERMINAR EL PROGRAMA PRESIONE 0):\t ')
    else:
        prom=acum_edad/tot_fecha
        print(f'EL PROMEDIO DE EDAD DE LA FECHA {resg_fecha} ES: {prom:.2f}\n ')
        print('-----------------------------------------------------------------------')
        if maximo<tot_fecha:
            maximo= tot_fecha
            fecha_max=resg_fecha

        resg_fecha=fecha
        acum_edad=0
        tot_fecha=0
else:
    prom=acum_edad/tot_fecha
    print(f'EL PROMEDIO DE EDAD DE LA FECHA {resg_fecha} ES: {prom:.2f}\n ')
    print('-----------------------------------------------------------------------')
    if maximo<tot_fecha:
        maximo= tot_fecha
        fecha_max=resg_fecha

    prom=tot_acum/tot
    print('______________________________________________________________________')
    print(f'EL PROMEDIO DE EDAD DE TODAS LAS CONSULTAS ({tot}) ES: %{prom:.2f}\n')
    print(f'LA FECHA EN LA CUAL SE REGISTRO MAYOR CANTIDAD DE PACIENTES FUE {fecha_max} Y HUBO {maximo} PACIENTES')

"""QUEDARON COSAS POR VER PERO PAVADAS (FORMATO DE COMO SE MUESTRAN LAS COSAS, ETC)"""