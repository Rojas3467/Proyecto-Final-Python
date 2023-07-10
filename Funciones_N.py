def Programa1():
    print("Programa 1.\nValor que tomara la varaiable \n")
    A = 10
    B = 0
    C = 0
    B = A
    C = B
    A = A
    return A,B,C

def Programa2():
    print("Programa 2.\nValor de la variable AUX \n")
    A = 10
    B = 20
    AUX = 0
    AUX = A
    A = B
    B = AUX
    return A,B,AUX

def Programa3():
    print("Programa 3.\nPrograma que sume tres valores \n")
    A = float(input("Escriba el valor de la A: "))
    B = float(input("Escriba el valor de la B: "))
    C = float(input("Escriba el valor de la C: "))
    D = (A + B + C) / 3
    return round(D,2)

def Programa4():
    print("Programa 4.\n Programa que calcula el area de un triangulo \n")
    B = float(input("Escriba el valor de la Base: "))
    A = float(input("Escriba el valor de Altura: "))
    Area = (B * A ) / 2
    return Area

def Programa5():
    print("Programa 5.\n Programa que calcula el perimetro de un rectangulo \n")
    AB = float(input("Escriba el valor AB: "))
    BC = float(input("Escriba el valor BC: "))
    CD = float(input("Escriba el valor CD: "))
    DA = float(input("Escriba el valor DA: "))
    P = AB + BC + CD + DA
    return P

def Programa6():
    print("Programa 6.\n Programa que calcula el area de un trapecio \n")
    Base1 = float(input("Escriba el valor de Base 1: "))
    Base2 = float(input("Escriba el valor de Base 2: "))
    Altura = float(input("Escriba el valor de la Altura: "))
    A = ((Base1 + Base2)*Altura)/2
    return A
    
def Programa7():
    print("Programa 7.\n Programa que calcula el volumen de un prisma rectangular \n")
    Largo = float(input("Escriba el valor de Largo: "))
    Ancho = float(input("Escriba el valor de Ancho: "))
    Altura = float(input("Escriba el valor de la Altura: "))
    Vol = Largo * Ancho * Altura
    return Vol

def Programa8():
    print("Programa 8.\n Programa que resuelva ecuaciones lineales \n")
    x = float(input("Escriba el valor de X: "))
    A = 20 - (7 * x)
    B = (-7 * x) + 2 - (10 * x) + 5
    C = (4 * x) + 4 + (9 * x) + 18
    D = (6 * x) -5 - (8 * x) + 2
    E = ((5 * x) + 78) / 28
    F = (((6 * x) - 7) / 4) + (((3 * 7) -5)/7)
    return A,B,C,D,E,F

def Programa9():
    print("Programa 9.\n Programa que resuelva una ecuacion dandole un valor a X y a Y \n")
    a = float(input("Escriba el valor de A: "))
    b = float(input("Escribir el valor de B: "))
    c = float(input("Escribir el valor de C: "))
    C1 = (4 * a) + (3 * b)
    C2 = (21 * a) - 18 + (8 * b) - 5
    C3 = (4 * a) + (3 * b) + 7
    C4 = (2 * a) + (3 * b) - (c**5)
    C5 = (2 * a) + (3 * b) - (c**2)
    return C1,C2,C3,C4,C5

def Programa10():
    print("Programa 10.\nPrograma de la conversion de unidades\n")

    metros = float(input("Ingrese el valor de metros: "))

    pies = metros / 0.3048
    pulgadas = metros * 39.37
    return pies,pulgadas

def Programa11():
    print("Programa 11.\nPrograma que calcule la regla de tres simple")
    A = float(input("Escribir el valor de A: "))
    B = float(input("Escribir el valor de B: "))
    C = float(input("Escribir el valor de C: "))
    x = (B * C)/A
    return x

def Programa12():
    print("Programa 12.\nPrograma que calcule el interes a pagar por un prestamo")
    monto = float(input("Escribir el monto: "))
    tasa = float(input("Escribir la tasa: "))
    plazo = float(input("Escribir el plazo: "))
    tasaP = tasa * 100
    tasaM = tasa / 12
    cuota = round(monto * (tasaM/(1-(1+tasaM)**(- plazo))),2)
    interesM = round(monto * tasaM, 2)
    capitalM = round(cuota - interesM, 2)
    return cuota, interesM, capitalM

def Programa13():
    print("Programa 13.\nPrograma que calcule el salario neto de un empleado")
    salarioBruto = float(input("Escribir el valor del salario bruto: "))
    seguroSocial = salarioBruto * 0.0514
    seguroEducativo = salarioBruto * 0.02
    cuotaPrestamo = 50
    salarioNeto = salarioBruto - seguroSocial -seguroEducativo -  cuotaPrestamo
    return salarioNeto

def Programa14():
    print("Programa 14.\nPrograma que calcule el costo total de una compra de combustible")
    precioGasolina95 = float(input("Escribir el precio de la gasolin 95: "))
    cantidadLitros = float(input("Escribir la cantidad de litros: "))
    costoSinImpuesto = precioGasolina95 * cantidadLitros
    costoTotal = costoSinImpuesto * 1.07
    return costoTotal

def Programa15():
    print("Programa 15.\nPrograma que calcule el precio de tres articulos de un supermercado")
    precioDelArticulo1 = float(input("Escriba el precio del Articulo1: " ))
    precioDelArticulo2 = float(input("Escriba el precio del Articulo2: " ))
    precioDelArticulo3 = float(input("Escriba el preco del Articulo3: " ))
    totalSinImpuesto = precioDelArticulo1 + precioDelArticulo2 + precioDelArticulo3
    totalDeCompra = totalSinImpuesto * 1.07
    return totalDeCompra

def Programa16():
    print("Programa 16.\nPrograma que calcule la nota final")
    evaluacion1 = float(input("Escribir la primera evaluacion "))
    evaluacion2 = float(input("Escribir la segunda evaluacion "))
    evaluacion3 = float(input("Escribir la tercera evaluacion "))
    evaluacion4 = float(input("Escribir la cuarta evaluacion "))
    evaluacion5 = float(input("Escribir la quinta evaluacion "))
    nota_final = round(((evaluacion1 * 0.20) + (evaluacion2 * 0.15) + (evaluacion3 * 0.25) + (evaluacion4 * 0.10) + (evaluacion5 * 0.30)) / 100, 2)
    return nota_final

def Programa17():
    print("Programa 17.\nConversion de unidades de medidas ")
    unidad = float(input("Ingrese la cantidad: "))
    gramos = round(unidad / 0.001, 2)
    kilogramos = round(unidad / 1000, 2)
    centimetros = round(unidad / 0.01, 2)
    metros = round(unidad / 100, 2)
    return gramos, kilogramos,centimetros, metros

def Programa18():
    print("Programa 18.\nCalculo del interes compuesto")
    Ci = float(input("Ingrese la capital inicial "))
    i = float(input("Ingrese la tasa de interes "))
    n = float(input("Ingrese el periodo de ahorro "))
    cf = round(Ci * (1 + i) ** n, 2)
    return cf

def Programa19():
    print("Programa 19.\nPrograma para calcular cuanto es la compra de articulos")
    valorDelArticulo1 = float(input("Ingrese el valor del Articulo1: "))
    valorDelArticulo2 = float(input("Ingrese el valor del Articulo2: "))
    valorDelArticulo3 = float(input("Ingrese el valor del Articulo3: "))
    valorDelArticulo4 = float(input("Ingrese el valor del Articulo4: "))
    valorDelArticulo5 = float(input("Ingrese el valor del Articulo5: "))
    totalSinImpuesto = round(valorDelArticulo1 + valorDelArticulo2 + valorDelArticulo3 + valorDelArticulo4 + valorDelArticulo5, 2)
    totalConImpuesto = totalSinImpuesto * 0.07
    precioConImpuesto = round(totalSinImpuesto + totalConImpuesto, 2)
    totalDeCompra = round(totalSinImpuesto / 5, 2)
    return totalSinImpuesto, precioConImpuesto, totalDeCompra

def Programa20():
    print("Programa 20.\nPrograma calcular el salario de neto de sus empleados")
    salarioBruto = float(input("Escribir el valor del salario bruto: "))
    seguroSocial = salarioBruto * 0.08
    seguroEducativo = salarioBruto * 0.02
    impuesto = salarioBruto * 0.15
    prestamo = 100
    descuento = seguroSocial + seguroEducativo + impuesto + prestamo
    salarioNeto = (salarioBruto - descuento)
    return descuento, salarioNeto

def Programa21():
    # Programa 21 - Calcula si una persona paga impuesto
    salario = float(input("Escriba el salario: "))
    if salario == 3000:
        impuesto = salario * 1.07
        print("Esta persona debe abonar impuesto", impuesto)
    else:
        print("No debe abonar impuesto")
        
def Programa22():
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
        
def Programa23():
    #Programa 23 - mostrar si una persona es mayor
    edad = int(input("Escriba la edad de una persona: "))
    if edad >= 18:
        print("mayor de edad")
    else:
        print("menor de edad")
        
def Programa24():
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
        
def Programa25():
    #Programa 25  - Calcular el precio final de un producto despues de aplicar un descuento porcentaje del descuento
    precio = float(input("Escribir el precio del producto: "))
    descuento = float(input("Escribir el porcentaje del descuento del producto: "))
    if precio < 50:
        descuento = precio * descuento/100
        precioFinal = precio - descuento
        print("Oferta especial", precioFinal)
    
    if precio >= 50:
        descuento = precio * descuento/100
        precioFinal = precio - descuento
        print("precio final", precioFinal)
        
def Programa26():
    # Programa 26 - Calcular los tres lados de un triangulos
    l1 = float(input("Escribir el primer lado de la longitud: "))
    l2 = float(input("Escribir el segundo lado de la longitud: "))
    l3 = float(input("Escribir el tercer lado de la longitud: "))
    if l1 == l2 and l1 == l3:
        print("El triangulo es Equilatero")
    if l1 != l2 and  l1 != l3:
        print("El triangulo es escaleno")    
    if  l1 == l2 and l1 != l3:
        print("El triangulo es isosceles")
        
def Programa27():
    # Programa 27 - Que solicite al usuario que ingrese un numero
    numero = int(input("Escribir un numero: "))
    if numero > 0:
        print("El numero es positivo ")
    elif numero == 0:
        print("El numero es cero ")
    else:
        print("El numero es negativo ")
        
def Programa28():
    # Programa 28 - Que solicite al usuario que ingrese una calificacion
    calificacion = int(input("Escribir una calificacion: "))

    if  90 <= calificacion <= 100:
        print("A", calificacion)
    elif  80 <= calificacion <= 89:
        print("B", calificacion )
    elif 70 <= calificacion <= 79:
        print("C", calificacion )
    elif 60 <= calificacion <= 69:
        print("D", calificacion )
    else:
        print("F", calificacion )
        
def Programa29():
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
        
def Programa30():
    nidia = 1
    while nidia <= 5:
        calificacion = int(input("Escribir una calificacion: "))
        if  90 <= calificacion <= 100:
            print("A", calificacion)
        elif  80 <= calificacion <= 89:
            print("B", calificacion )
        elif 70 <= calificacion <= 79:
            print("C", calificacion )
        elif 60 <= calificacion <= 69:
            print("D", calificacion )
        else:
            print("F", calificacion )
        nidia += 1
 
def Programa31():
    valor = 1
    
    while valor <= 10:
        print (valor)
        if valor == 7:
            break
        valor += 1
        
def Programa32():
    calificaciones = int(input("Ingrese el numero de calificaciones a evaluar: "))

    for i in range(calificaciones):
        calificacion = float(input("Ingrese la califcacion: "))
    
        if calificacion >= 90 and calificacion <= 100:
            letra = "A"
        elif calificacion >= 80 and calificacion <= 89:
            letra = "B"
        elif calificacion >= 70 and calificacion <= 79:
            letra = "C"
        elif calificacion >= 60 and calificacion <= 69:
            letra = "D"
        else:
            letra = "F"
        
        print(f"La calificacion es {letra}")
    return None        
    
def Programa33():
    for i in range (1, 13):
        print("Tabla de multiplicar del", i)
        print("--------------------")
        for j in range(1, 13):
            resultado = i * j
            print(i, "x", j, "=", resultado)
            print()    
    return None

def Programa34():
    i = 1

    while i < 15:
        print(i)
        if i % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
        
        i += 1
    return None

def Programa35():
    n = range(0, 10)
    for x in n:
        print(x)
        if 5 <= x <= 9:
            print("El numero es mayor")
        
        elif 1 <= x <= 4:
            print("El numero es menor")
        
        else:
            print("menor o igual a cero")
            
def Programa36():
    articulos = 5
    contador = 0
    while contador < articulos:
        precio = float(input("Escribir precio de articulos: "))
        impuesto = precio * 0.07
        precio_total = precio + impuesto
        print("El resultado de precio total ", precio_total)
        contador += 1
    
def Programa37():
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
        
def Programa38():
    suma = 0
    for numero in range (2,21,2):
        suma += numero
    return suma

def Programa39():
    base = 4
    altura = 6
    Area = (base * altura)/2
    return Area        