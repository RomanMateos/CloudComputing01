cuenta = float(input("¿Cuánto fue el total de la cuenta?: "))
porcentaje = float(input("¿Qué porcentaje de propina quieres dejar? (ej: 20,30,40)): "))
propina = cuenta * (porcentaje / 100)
total = cuenta + propina
print("Propina: $", round(propina))
print("Total a pagar: $", round(total))
