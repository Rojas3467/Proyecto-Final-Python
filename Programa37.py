i = 1
while i <= 5:
    a = float(input("Escribir el primer numero: "))
    b = float(input("Escribir el segundo numero: "))
    c = float(input("Escribir el tercer numero: "))

    if a > b and a > c:
       print("El mayor es a =", a)
       
    if b > a and b > c:
        print("El mayor es b =", b)
        
    if c > a and c > b:
        print("El mayor es c =", c)
    i += 1    

