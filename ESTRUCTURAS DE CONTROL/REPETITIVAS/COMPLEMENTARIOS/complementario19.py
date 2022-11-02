"""Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:
a) porcentaje de varones menores de 15 años para cada zona
b) porcentaje de varones menores de 15 años para todo el municipio
Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin."""
tot=0
tot_zona=0
tot_v=0
tot_zona_v=0
zona=input('INGRESE LA ZONA\t')
resg_zona=zona
while zona!='0':    
    if resg_zona== zona:
        sexo=input('INGRESE EL SEXO (M O F):\t')
        edad=int(input('INGRESE LA EDAD:\t'))

        if edad<15: #hago asi para poder decir que el error esta en que puso otra cosa distanta a m o f
            if sexo.upper()=='M':
                tot_v+=1
                tot_zona_v+=1
                
        tot+=1
        tot_zona+=1
        zona=input('\nINGRESE LA ZONA (SI DESEA TERMINAR EL PROGRAMA PRESIONE 0):\t ')
    else:
        porc=(tot_zona_v*100)/tot_zona
        print(f'EL PORCENTAJE DE VARONES MENORES DE 15 EN LA ZONA {resg_zona} ES: %{porc}\n')
        print('-----------------------------------------------------------------------')
        resg_zona=zona
        tot_zona=0
        tot_zona_v=0
else:
    porc=(tot_v*100)/tot
    print('______________________________________________________________________')
    print(f'EL PORCENTAJE DE VARONES MENORES DE 15 EN EL MUNICIPIO ES: %{porc}')