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
    
    
    
