from math import pi
area= input("¿Que area quiere calcular?(Escriba T si es un triangulo o C si es un cirulo)")
if (area=="T"):
    Tb=float(input("¿Cual es la base del tiangulo?"))
    Th=float(input("¿Cual es la altura del triangulo?"))
    respuesta=((Tb*Th)/2)
    print("El area del triangulo es","{0:.2f}".format(respuesta))
if (area=="C"):
    Cr=float(input("¿Cual es el radio del circulo?"))
    respuesta2=((Cr**2)*pi)  
    print("El area del triangulo es","{0:.2f}".format(respuesta2))
