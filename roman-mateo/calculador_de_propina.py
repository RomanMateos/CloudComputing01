# Programa para calcular la propina en un restaurante

# Solicitar al usuario el total de la cuenta
total_cuenta = float(input("Ingrese el total de la cuenta: "))

# Solicitar el porcentaje de propina que desea dejar
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 10, 15, 20): "))

# Calcular el monto de la propina
monto_propina = (total_cuenta * porcentaje_propina) / 100

# Calcular el total a pagar (cuenta + propina)
total_pagar = total_cuenta + monto_propina

# Mostrar los valores por pantalla
print("\nMonto de la propina: ${:.2f}".format(monto_propina))
print("Total a pagar: ${:.2f}".format(total_pagar))
