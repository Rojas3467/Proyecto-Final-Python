def calcular_area_triangulo(base,altura):
    Area = (base * altura)/2
    return Area

Base = float(input("Escriba el valor de la Base: "))
Altura = float(input("Escriba el valor de Altura: "))

Area = (Base * Altura ) / 2

print("El area de un triangulo es: ",Area)