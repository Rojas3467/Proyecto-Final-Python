# Programa 21 - Calcula si una persona paga impuesto

salario = float(input("Escriba el salario: "))
 
if salario == 3000:
     impuesto = salario * 1.07
     print("Esta persona debe abonar impuesto", impuesto)
else:
    print("No debe abonar impuesto")
    
print("\n Fin del Programa") 