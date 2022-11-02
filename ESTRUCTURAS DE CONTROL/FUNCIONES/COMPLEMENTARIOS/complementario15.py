"""En este ejercicio escribirá una función que determina si una contraseña es buena o no. Definiremos como una buena contraseña aquella que
 tenga una longitud de al menos 8 caracteres y contenga al menos una letra mayúscula, al menos una letra minúscula y al menos un número. Su 
 función debe devolver verdadero si la contraseña que se le pasó, como único parámetro, es buena,
 de lo contrario debería devolver falso. Incluya un programa principal que lea una contraseña del usuario e informe si es buena o no"""


def passBueno(password):
    mayus=False
    min=False
    num=False
    if len(password)>=8:
        tam=True
    else:
        return False
    
    for i in(password):
        if i.isupper():
            mayus=True
        elif i.islower():
            min=True
        elif i.isdigit():
            num=True

        if mayus and min and num: #si se cumple antes de que termina con esto ya cortará
            return True
        
    return False
                


password=input('INGRESE UNA CONTRASEÑA:\t')
print(passBueno(password))