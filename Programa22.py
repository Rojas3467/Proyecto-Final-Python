#Programa 22 - calcular la temperatura

temperature = float(input("Escriba la temperatura: "))

if temperature < 20:
    if temperature < 10:
        print("Nivel azul")
    else:
        print("Nivel verde")
else:
    if temperature < 30:
        print("Nivel naranja")
    else:
        print("Nivel rojo")
        
print("\n Fin del Programa")        