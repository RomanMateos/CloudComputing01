total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo, 10 para 10%): "))
monto_propina = total_cuenta * (porcentaje_propina / 100)
total_pagar = total_cuenta + monto_propina

print(f"\nMonto de la propina: ${monto_propina:.2f}")
print(f"Total a pagar (cuenta + propina): ${total_pagar:.2f}")
