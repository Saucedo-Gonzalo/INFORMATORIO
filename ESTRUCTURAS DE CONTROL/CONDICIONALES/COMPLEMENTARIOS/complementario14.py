#Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.

num1=float(input("INGRESE UN NUMERO: \n"))
num2=float(input("INGRESE UN NUMERO: \n"))

if num1==num2:
    result=num1*num2
elif num1>num2:
    result=num1-num2
else:
    result=num1+num2

print (f"RESULTADO: {result:.2f}")