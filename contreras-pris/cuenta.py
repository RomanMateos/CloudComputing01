"""cuenta bar"""

cuenta = int(input("Ingrese valor total cuenta: $"))
porcentaje = int(input("Porcentaje que desea dejar"))


propina = (cuenta  * porcentaje) / 100
total = cuenta + propina

print (f"Propina: {propina:.2f} $")
print (f"Total de la cuenta: {total:.2f} $")


