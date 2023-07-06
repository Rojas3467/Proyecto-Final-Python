print("Programa 12\n. Programa que calcule el interes a pagar por un prestamo")

monto = float(input("Escribir el monto: "))
tasa = float(input("Escribir la tasa: "))
plazo = float(input("Escribir el plazo: "))

tasaP = tasa * 100
tasaM = tasa / 12
cuota = monto * (tasaM/(1-(1+tasaM)**(- plazo)))
interesM = monto * tasaM
capitalM = cuota - interesM

print(f"la cuota es de ", round(cuota,2))
print("El interes mensual es ", round(interesM,2))
print("La capital mensual es ", round(capitalM,2))
