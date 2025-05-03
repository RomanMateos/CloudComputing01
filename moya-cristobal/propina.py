total = float(input("Ingresa el total de la cuenta: "))

porcentaje = float(input("Ingresa el porcentaje de propina: "))

propina = total * (porcentaje / 100)

total_cuentaxd = total + propina

print("Propina:", round(propina))
print("Total De La Cuenta: ", round(total_cuentaxd))
