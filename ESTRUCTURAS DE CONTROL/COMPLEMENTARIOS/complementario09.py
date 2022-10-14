"""En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital 
se reparte conforme a la sig. tabla:

ÁREA 		PORCENTAJE
Pediatría					60%
Traumatología		 20%
Kinesiología			 20%
Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal 		que se ingrese por teclado."""


monto=float(input("INGRESE EL MONTO PRESUPUESTAL\n"))

pediatria=monto*0.6
traumato_kinesio=monto*0.2

print(f"DINERO QUE RECIBIRÁ CADA ÁREA:\n *ÁREA DE PEDIATRÍA: {pediatria:.2f}\n *ÁREA DE TRAUMATOLOGÍA: {traumato_kinesio:.2f}\n *ÁREA DE KINESIOLOGÍA: {traumato_kinesio:.2f}")