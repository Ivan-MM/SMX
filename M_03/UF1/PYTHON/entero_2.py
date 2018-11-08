JUEGO DE PRUEBAS    
Entrada        Sortida
3             "positivo"
-2            "negativo"
0              "neutro"

numero=int(input("elige un numero cualquiera"))
if(numero<0):
  print("es negativo")
else:
  if(numero==0):
    print("es neutro")
  else:
    print("es positivo")
