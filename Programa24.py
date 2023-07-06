#Programa 24 - Calcular el numero mayor 

a = float(input("Escribir el primer numero: "))
b = float(input("Escribir el segundo numero: "))
c = float(input("Escribir el tercer numero: "))

if a > b and a > c:
   print("El mayor es A =", a)
   
if b > a and b > c:
    print("El mayor es B =", b)
    
if c > a and c > b:
    print("El mayor es C =", c)
    
print("\n Fin del Programa")    
