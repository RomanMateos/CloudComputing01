def calcular_propina():
    try:
        total_cuenta_str = input("Ingrese el total de la cuenta: ")
        total_cuenta = float(total_cuenta_str)

        porcentaje_propina_str = input("Ingrese el porcentaje de propina que desea dejar (ej: 10, 15, 20): ")
        porcentaje_propina = float(porcentaje_propina_str) / 100

        monto_propina = total_cuenta * porcentaje_propina
        total_a_pagar = total_cuenta + monto_propina

        print(f"\nMonto de la propina: ${monto_propina:.2f}")
        print(f"Total a pagar (cuenta + propina): ${total_a_pagar:.2f}")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    calcular_propina()



