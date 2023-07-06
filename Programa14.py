print("Programa 14\n. Programa que calcule el costo total de una compra de combustible")
a1 = input("Escribir el precio de la gasolin 95: ")
a2 = input("Escribir la cantidad de litros: ")

precioGasolina95 = float(a1)
cantidadLitros = float(a2)

costoSinImpuesto = precioGasolina95 * cantidadLitros
costoTotal = costoSinImpuesto * 1.07

costoT = round(costoTotal,2)

print("El costo total de una compra de combustible es: ",round(costoT,2))
