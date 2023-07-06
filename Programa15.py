print("Programa 15\n. Programa que calcule el precio de tres articulos de un supermercado")
A1 = input("Escriba el precio del Articulo1: " )
B2 = input("Escriba el precio del Articulo2: " )
C3 = input("Escriba el preco del Articulo3: " )

precioDelArticulo1 = float(A1)
precioDelArticulo2 = float(B2)
precioDelArticulo3 = float(C3)

totalSinImpuesto = precioDelArticulo1 + precioDelArticulo2 + precioDelArticulo3
totalDeCompra = totalSinImpuesto * 1.07
tDC = round(totalDeCompra,2)

print("El precio de los tres articulos es: ", tDC)
