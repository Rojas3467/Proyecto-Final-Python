print("Programa 20\n. Programa calcular el salario de neto de sus empleados")
A1 = input("Escribir el valor del salario bruto: ")

salarioBruto = float(A1)

seguroSocial = salarioBruto * 0.08
seguroEducativo = salarioBruto * 0.02
impuesto = salarioBruto * 0.15
prestamo = 100
descuento = seguroSocial + seguroEducativo + impuesto + prestamo
salarioNeto = (salarioBruto - descuento)

print("El descuento es: ", descuento )
print("El salario neto de sus empleados es: ", salarioNeto)