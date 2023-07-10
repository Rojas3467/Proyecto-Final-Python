# se importan funciones desde la carpeta "Funciones_N.py"
from Funciones_N import Programa1, Programa2, Programa3, Programa4, Programa5, Programa6, Programa7, Programa8, Programa9, Programa10, Programa11, Programa12, Programa13, Programa14, Programa15, Programa16, Programa17, Programa18, Programa19, Programa20, Programa21, Programa22, Programa23, Programa24, Programa25, Programa26, Programa27, Programa28, Programa29, Programa30, Programa31, Programa32, Programa33, Programa34, Programa35, Programa36, Programa37, Programa38, Programa39

#Bucle Principal
while True:
    #se pide al usuario ingresar el nombre del programa que desea llamar
    Nombre_Programa = input("Ingrese Nombre del programa que se desea llamar(o ´salir´ para terminar): ")
    
    #Se utiliza estructuras condicionales para determinar que funcion llamar
    if Nombre_Programa == "salir":
        break
    elif Nombre_Programa == "Programa1":
        resultado = Programa1()
        print("El valor que tomara la varaiable es: ", resultado)
        print(".....................")
    elif Nombre_Programa == "Programa2":
        resultado = Programa2()
        print("El Valor de la variable AUX es:",resultado)
        print(".....................")
    elif Nombre_Programa == "Programa3":
        resultado = Programa3()
        print("La suma de tres valores es:",resultado)
        print(".....................")
    elif Nombre_Programa == "Programa4":
        resultado = Programa4()
        print("El Area de un Triangulo es:",resultado)
        print(".....................")
    elif Nombre_Programa == "Programa5":
        resultado = Programa5()
        print("El Perimetro de un Rectangulo es: ",resultado)
        print(".....................")
    elif Nombre_Programa == "Programa6":
        resultado = Programa6()
        print("El Area de un Trapecio es: ",resultado)
        print(".....................")
    elif Nombre_Programa == "Programa7":
        resultado = Programa7()
        print("El volumen de un prisma rectangular es: ",resultado)
        print(".....................")
    elif Nombre_Programa == "Programa8":
        A, B, C, D, E, F = Programa8()
        print("El resultado de A es ", A)
        print("El resultado de B es ", B)
        print("El resultado de C es ", C)
        print("El resultado de D es ", D)
        print("El resultado de E es ",round(E,2))
        print("El resultado de F es ",round(F,2))
        print(".....................")
    elif Nombre_Programa == "Programa9":
        C1, C2, C3, C4, C5 = Programa9()
        print("El resultado de c1 es ", C1)
        print("El resultado de c2 es ", C2)
        print("El resultado de c3 es ", C3)
        print("El resultado de c4 es ", C4)
        print("El resultado de c5 es ", C5)
        print(".....................")
    elif Nombre_Programa == "Programa10":
        pies, pulgadas = Programa10()
        print("la conversion de metros a pies es: ", round(pies, 2) )
        print("La conversion de metros a pulgadas es: ", round(pulgadas, 2))
        print(".....................")
    elif Nombre_Programa == "Programa11":
        resultado = Programa11()
        print("El cuarto valor proporcional es: ", round(resultado, 2))
        print(".....................")
    elif Nombre_Programa == "Programa12":
        cuota, interesM, capitalM = Programa12()
        print(f"la cuota es de ", round(cuota,2))
        print("El interes mensual es ", round(interesM,2))
        print("La capital mensual es ", round(capitalM,2))
        print(".....................")
    elif Nombre_Programa == "Programa13":
        resultado = Programa13()
        print("El salario neto de un empleado es: ",round(resultado, 2))
        print(".....................")
    elif Nombre_Programa == "Programa14":
        resultado = Programa14()
        print("El costo total de una compra de combustible es: ",resultado)
        print(".....................")
    elif Nombre_Programa == "Programa15":
        resultado = Programa15()
        print("El precio de los tres articulos es: ", round(resultado,2))
        print(".....................")
    elif Nombre_Programa == "Programa16":
        resultado = Programa16()
        print("la nota final es ", resultado)
        print(".....................")
    elif Nombre_Programa == "Programa17":
        gramos, kilogramos, centimetros, metros = Programa17()
        print(" La medida equivalente de kilogramos a gramos es:", gramos)
        print(" La medida equivalente de gramos a  kilogramos es:", kilogramos)
        print(" La medida equivalente de metros a centimetros es:", centimetros)
        print(" La medida equivalente de centimetros a metros es:", metros)
        print(".....................")
    elif Nombre_Programa == "Programa18":
        resultado = Programa18()
        print("La capital final es: ", round(resultado, 2))
        print(".....................")
    elif Nombre_Programa == "Programa19":
        totalSinImpuesto, precioConImpuesto, totalDeCompra = Programa19()
        print("El precio de la compra sin impuesto es: ", round(totalSinImpuesto,2))
        print("El precio de la compra con impuesto es: ", round(precioConImpuesto,2))
        print("El precio de los 5 articulos es: ", round(totalDeCompra,2))
    elif Nombre_Programa == "Programa20":
        descuento, salarioNeto = Programa20()
        print("El descuento es: ", descuento )
        print("El salario neto de sus empleados es: ", salarioNeto)
    elif Nombre_Programa == "Programa21":
        Programa21()
    elif Nombre_Programa == "Programa22":
        Programa22()
    elif Nombre_Programa == "Programa23":
        Programa23()
    elif Nombre_Programa == "Programa24":
        Programa24()
    elif Nombre_Programa == "Programa25":
        Programa25()
    elif Nombre_Programa == "Programa26":
        Programa26()
    elif Nombre_Programa == "Programa27":
        Programa27()
    elif Nombre_Programa == "Programa28":
        Programa28()
    elif Nombre_Programa == "Programa29":
        Programa29()
    elif Nombre_Programa == "Programa30":
        Programa30()
    elif Nombre_Programa == "Programa31":
        Programa31()
    elif Nombre_Programa == "Programa32":
        Programa32()
    elif Nombre_Programa == "Programa33":
        Programa33()
    elif Nombre_Programa == "Programa34":
        Programa34()
    elif Nombre_Programa == "Programa35":
        Programa35()
    elif Nombre_Programa == "Programa36":
        Programa36()
    elif Nombre_Programa == "Programa37":
        Programa37()
    elif Nombre_Programa == "Programa38":
        resultado = Programa38()
        print("La suma de los pares: ", resultado)
    elif Nombre_Programa == "Programa39":
        resultado = Programa39()
        print("El area de un triangulo es: ", resultado)
    else:
        print("Nombre de programa incorrecto")


