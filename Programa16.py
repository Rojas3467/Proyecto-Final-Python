print("Programa 16\n. Programa que calcule la nota final")
E1 = input("Escribir la primera evaluacion ")
E2 = input("Escribir la segunda evaluacion ")
E3 = input("Escribir la tercera evaluacion ")
E4 = input("Escribir la cuarta evaluacion ")
E5 = input("Escribir la quinta evaluacion ")

evaluacion1 = float(E1)
evaluacion2 = float(E2)
evaluacion3 = float(E3)
evaluacion4 = float(E4)
evaluacion5 = float(E5)

nota_final = ((evaluacion1 * 0.20) + (evaluacion2 * 0.15) + (evaluacion3 * 0.25) + (evaluacion4 * 0.10) + (evaluacion5 * 0.30)) / 100
notaFinal = round(nota_final,2)

print("la nota final es ", notaFinal)

