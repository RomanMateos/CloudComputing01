print("Hola buenas tardes")
cuenta = int(input("Ingrese el total de su cuenta: "))
total = 0

confirmacion = input("¿Desea dejar propina?")
if confirmacion.lower() == "si":
  print("Selecciona una 20% 10% 5% ")
  print("Ingresar en número entero positivo")
  propina = int(input("¿Cuanta propina desea dejar?: "))
  if propina == 20: total = cuenta * 1.2
  elif propina == 10: total = cuenta * 1.1
  elif propina == 5: total = cuenta * 1.05
  else: print("Válor incorrecto, inténtelo de nuevo")
  print(f"Su total a pagar es de {total}") 
elif confirmacion.lower() == "no":
  print(f"Su total a cancelar es: {cuenta}")
else: print("Entrada inválida, escriba (si/no)")


