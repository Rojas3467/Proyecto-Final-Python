print("Programa 5.\n Programa que calcula el perimetro de un rectangulo \n")
i1 = input("Escriba el valor AB: ")
i2 = input("Escriba el valor BC: ")
i3 = input("Escriba el valor CD: ")
i4 = input("Escriba el valor DA: ")

AB = float(i1)
BC = float(i2)
CD = float(i3)
DA = float(i4)

P = AB + BC + CD + DA
PR = round(P,2)

print("El area de un rectangulo es", PR)