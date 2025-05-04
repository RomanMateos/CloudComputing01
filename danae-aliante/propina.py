total_cuenta = float(input("ingresa el total de la cuenta: $."))
porcentaje_propina = float(input("ingresa el porcentaje de propina que desea dejar (popr ejemplo,10):"))
monto_propina = total_cuenta * (porcentaje_propina / 100)
total_pagar = total_cuenta + monto_propina
print(f"\nMonto de la propina: ${monto_propina:.2f}")
print(f"total a pagar(cuenta + propina): ${total_pagar:.2f}")

