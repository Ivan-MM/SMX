jamon = input("tienes jamón?")
abducion = input("te han abducido?")
dia = input("que dia?")
estudiar = input("cuanto has estudiado?")
if(( jamon == "si") or (( abducion == "si") and ( dia == "jueves")) or ( estudiar == "mucho")):
    print("has aprobado")
else:
    print("nos vemos en junio")
