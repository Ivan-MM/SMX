humedad = int(input("Humedad: "))
if humedad >= 80 :
    print ("Si no te quieres mojar un paraguas debes de usar")
else:
    print ("No temas, no necesitas usar el paraguas si no es de sombrilla")


jamon = input("tienes jamón?")
abducion = input("te han abducido?")
dia = input("que dia?")
estudiar = input("cuanto has estudiado?")
if(( jamon == "si") or (( abducion == "si") and ( dia == "jueves")) or ( estudiar == "mucho")):
  print("has aprobado")
else:
  print("nos vemos en junio")


edad = int(input("Cuantos años tienes? "))
if ((edad <5)or(edad >= 65)):
    print ("entras gratis")
else:
    print ("tienes que pagar 2.5€")
    

    edad = int(input("que edad tienes?"))
sexe = input("eres hombre o mujer?")
color = int(input("Cual es el color de tu pelo? (1 Rubio/a, 2 Peliroja, 3 Morena, 0 para otro)"))
jubilado=input("estas jubilado/a?")
if ((sexe=="hombre")and(jubilado=="no")):
    print("pagas 1€")
if (((sexe=="mujer")and(color== 1)and(jubilado=="no"))or((jubilado=="si")and(edad>=65))):
   print("entras gratis")
if((sexe=="mujer")and(jubilado=="no")and(color==0)):
   print("pagas 50 centimos")
