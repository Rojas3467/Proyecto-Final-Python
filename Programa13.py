print("Programa 13\n- Programa que calcule el salario neto de un empleado")
i1 = input("Escribir el valor del salario bruto: ")

salarioBruto = float(i1)

seguroSocial = salarioBruto * 0.0514
seguroEducativo = salarioBruto * 0.02
cuotaPrestamo = 50
salarioNeto = salarioBruto - seguroSocial -seguroEducativo -  cuotaPrestamo

salarioN = round(salarioNeto,2)

print("El salario neto de un empleado es: ",salarioN)
 