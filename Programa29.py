valor = 1

while valor <= 3:
    numero = int(input("Escribir un numero: "))
    if numero > 0:
        print("El numero es positivo ")
    elif numero == 0:
        print("El numero es cero ")
    else:
        print("El numero es negativo ")
    valor += 1  