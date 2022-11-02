"""Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía
 pública.

Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5
dígitos a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.

Del valor numérico:

Los 3 primeros números corresponden a la patente

El 4 número indica

1- Tiró basura a la vía pública

0 - No tiró basura a la vía pública

El 5 número indica

1- Ya había sido multado el vehículo

0 - Vehículo sin multas.

Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de
éstos que ya habían sido multados."""

 

tot_tiro=0
tot_mult=0

opc='A'

while opc.upper() != 'Z':
    letras=input('INGRESE LAS LETRAS DE LA PATENTE:\t')
    while len(letras)!=3 or letras.isalpha()!=True: #isalpha es para que compare si solo hay letras del abecedario
        letras=input('INGRESE 3 LETRAS CORRECTAS DE LA PATENTE:\t')

    numeros=input('INGRESE LOS NUMEROS DE LA PATENTE:\t')
    while len(numeros)!=3 or numeros.isdigit()!=True:
        numeros=input('INGRESE 3 NUMEROS CORRECTOS DE LA PATENTE:\t')

    opc_basura=int(input('INGRESE UNA OPCION:\n *1- TIRÓ BASURA A LA VÍA PÚBLICA \n *0- NO TIRÓ BASURA A LA VÍA PUBLICA\n'))
    while opc_basura>1:
        print('\nERROR, INGRESE UNA OPCION CORRECTA')
        opc_basura=int(input('INGRESE UNA OPCION:\n *1- TIRÓ BASURA A LA VÍA PÚBLICA \n *0- NO TIRÓ BASURA A LA VÍA PUBLICA\n'))
    if opc_basura==1:
        tot_tiro+=1

    opc_multado=int(input('INGRESE UNA OPCION:\n 1- YA HABIA SIDO MULTADO\n 0- VEHÍCULO SIN MULTAS\n'))
    while opc_multado>1:
        print('\nERROR, INGRESE UNA OPCION CORRECTA')
        opc_multado=int(input('INGRESE UNA OPCION:\n 1- YA HABIA SIDO MULTADO\n 0- VEHÍCULO SIN MULTAS\n'))
    if opc_multado==1:
        tot_mult+=1

    opc=input('PARA FINALIZAR PRESIONE Z, PARA SEGUIR CUALQUIER OTRO CARACTER')
else:
    ('______________________________________________________________________')
    porc=tot_mult*100/tot_tiro
    print (f'\n PORCENTAJE DE VEHICULOS QUE HAN TIRADO BASURA Y YA HAN SIDO MULTADOS: %{(porc):.2f}')