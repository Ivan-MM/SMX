#config: utf-8
from math import pi
area= input("¿Que area quiere calcular?(Escriba T si es un triangulo o C si es un cirulo)")
if (area=="T"):
    Tb=float(input("¿Cual es la base del tiangulo?"))
    Th=float(input("¿Cual es la altura del triangulo?"))
    respuesta=((Tb*Th)/2)
    if(respuesta>0):
        print("El area del triangulo es","{0:.2f}".format(respuesta))
    else:
        print("Esa area es imposible")
if (area=="C"):
    Cr=float(input("¿Cual es el radio del circulo?"))
    respuesta2=((Cr**2)*pi)
    if(respuesta2>0):
        print("El area del triangulo es","{0:.2f}".format(respuesta2))
    else:
        print("Esa area es imposible")
