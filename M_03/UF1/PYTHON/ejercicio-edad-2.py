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
