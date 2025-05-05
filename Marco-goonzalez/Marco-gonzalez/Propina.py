total = int(input("cuanto va a pagar: "))
propina = str(input("va a dejar propina si/no?: "))
if propina.lower() == "si":
  porcentaje = int(input("cuanta propina va a dejar?: "))
  print("su total a pagar es: ", total * (porcentaje/100))
else:
  print("su total a pagar es: ", total)

