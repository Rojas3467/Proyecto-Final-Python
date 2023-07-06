def sumar_numeros_pares(i):
    suma = 0
    numero = 1
    for numero in range (1, i + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

suma = sumar_numeros_pares(20)
print("La suma de los pares: ", suma)