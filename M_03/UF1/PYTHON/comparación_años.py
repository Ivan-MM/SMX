#config: utf-8
anyo_actual=int(input("en que año estamos?"))
anyo=int(input("elige un año cualquiera"))
if ((anyo_actual==0)or(anyo==0)):
  print("el año 0 no existe")
else:
  if (anyo_actual>anyo):
    mayor=(anyo_actual - anyo)
      print("para llegar a este año", anyo, "falta", mayor, "años")
  else:
    if (anyo_actual<anyo):
      menor=(anyo-anyo_actual)
        print("desde el año", anyo_actual, "faltan", menor, "años")
