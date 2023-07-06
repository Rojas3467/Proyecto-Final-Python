print("Programa 11\n. Programa que calcule la regla de tres simple")

v1 = input("Escribir el valor de A: ")
v2 = input("Escribir el valor de B: ")
v3 = input("Escribir el valor de C: ")

A = float(v1)
B = float(v2)
C = float(v3)

x = (B * C)/A
xr = round(x,2)

print("El cuarto valor proporcional es: ", xr)


