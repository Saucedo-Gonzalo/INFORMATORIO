"""Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto
 en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL.
  Escribir un programa que determine si es factible la utilización de fertilizantes."""

hectareas= float(input("INGRESE LA CANTIDAD DE HECTAREAS (valor en metros cuadrados)"))
abarca=float(input("CUANTO ABARCA EL COMPUESTO (valor en metros cuadrados)): \n"))
vegetacion=input("INGRESE EL TIPO DE VEGETACION: \n")

if vegetacion.upper()== 'MATORRAL':
    print("NO ES FACTIBLE EL USO DE FERTILIZANTES")
else:
    tot=(abarca*100)/hectareas
    if tot>10:
        print("ES FACTIBLE EL USO DE FERTILIZANTES: \n")
    else:
        print("NO ES FACTIBLE EL USO DE FERTILIZANTES: \n")