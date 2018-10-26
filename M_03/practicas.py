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


