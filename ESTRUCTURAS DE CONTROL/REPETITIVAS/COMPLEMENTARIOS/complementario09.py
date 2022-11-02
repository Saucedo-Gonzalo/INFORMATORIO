"""Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda.
 Desea obtener de todas las personas que alcance a encuestar en un día,
 que porcentaje tiene estudios de primaria, secundaria, carrera técnica, estudios profesionales y estudios de posgrado."""


resp='S'
cont_prim=0
cont_secu=0
cont_tec=0
cont_prof=0
cont_posg=0

while resp.upper()=='S':
    nombre=input('NOMBRE:\n')
    estudios=input('INGRESE UN NUMERO:\n 1.PRIMARIA \n 2.SECUNDARIA \n 3.CARRERA TECNICA \n 4.ESTUDIO PROFESIONAL\n 5. POSGRADO \n')
    if estudios=='1':
        cont_prim+=1
    elif estudios=='2':
        cont_secu+=1
    elif estudios=='3':
        cont_tec+=1
    elif estudios=='4':
        cont_prof+=1
    elif estudios=='5':
        cont_posg+=1
    else:
        print('INGRESE UN ESTUDIO VALIDO.\n')
        continue

    resp=input('PARA CONTINUAR PRESIONE S, PARA SALIR CUALQUIER OTRO CARACTER')

tot=cont_prim+cont_secu+cont_tec+cont_prof+cont_posg
print(f'PORCETAJES DE ESTUDIO DE {tot} PERSONAS: \n *PRIMARIA: {(cont_prim*100)/tot:.2f}% *SECUNDARIA: {(cont_secu*100)/tot:.2f}% *TECNICA: {(cont_tec*100)/tot:.2f}% *PROFESIONAL: {(cont_prof*100)/tot:.2f}% *POSGRADO: {(cont_posg*100)/tot:.2f}%')
