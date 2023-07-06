print("Programa 19\n. Programa para calcular cuanto es la compra de articulos")
A1 = input("Ingrese el valor del Articulo1: ")
A2 = input("Ingrese el valor del Articulo2: ")
A3 = input("Ingrese el valor del Articulo3: ")
A4 = input("Ingrese el valor del Articulo4: ")
A5 = input("Ingrese el valor del Articulo5: ")

valorDelArticulo1 = float(A1)
valorDelArticulo2 = float(A2)
valorDelArticulo3 = float(A3)
valorDelArticulo4 = float(A4)
valorDelArticulo5 = float(A5)

totalSinImpuesto = valorDelArticulo1 + valorDelArticulo2 + valorDelArticulo3 + valorDelArticulo4 + valorDelArticulo5
totalConImpuesto = totalSinImpuesto * 0.07
precioConImpuesto = totalSinImpuesto + totalConImpuesto
totalDeCompra = totalSinImpuesto / 5

print("El precio de la compra sin impuesto es: ", round(totalSinImpuesto,2))
print("El precio de la compra con impuesto es: ", round(precioConImpuesto,2))
print("El precio de los 5 articulos es: ", round(totalDeCompra,2))
