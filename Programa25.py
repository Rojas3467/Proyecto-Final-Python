#Programa 25  - Calcular el precio final de un producto despues de aplicar un descuento porcentaje del descuento

precio = float(input("Escribir el precio del producto: "))
descuento = float(input("Escribir el porcentaje del descuento del producto: "))

if precio < 50:
    descuento = precio * descuento/100
    precioFinal = precio - descuento
    print("Oferta especial", precioFinal)
    
if precio > 50:
    descuento = precio * descuento/100
    precioFinal = precio - descuento
    print("precio final", precioFinal) 
      
print("\n Fin del Programa")    
