# Programa 26 - Calcular los tres lados de un triangulos

l1 = float(input("Escribir el primer lado de la longitud: "))
l2 = float(input("Escribir el segundo lado de la longitud: "))
l3 = float(input("Escribir el tercer lado de la longitud: "))

if l1 == l2 and l1 == l3:
    print("El triangulo es Equilatero")

if l1 != l2 and  l1 != l3:
    print("El triangulo es escaleno")
    
if  l1 == l2 and l1 != l3:
    print("El triangulo es isosceles")
    
print("\n Fin del Programa")      