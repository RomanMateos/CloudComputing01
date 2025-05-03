#Holis
total_pagar = 0

cuenta = int(input("INGRESE EL TOTAL A PAGAR: "))
print(" ")
propina = int(input("INGRESE EL PORCENTAJE DE PROPINA: 10% / 15% / 20%: "))

if propina == 10:

    total_pagar = cuenta * 0.10

    print(f"EL TOTAL A PAGAR ES DE: ${int(total_pagar + cuenta)}")

elif propina == 15:

    total_pagar = cuenta * 0.15

    print(f"EL TOTAL A PAGAR ES DE: ${int(total_pagar + cuenta)}")

elif propina == 20:

    total_pagar = cuenta * 0.20

    print(f"EL TOTAL A PAGAR ES DE: ${int(total_pagar + cuenta)}")

else:
    print("MONTO DE PROPINA MAL INGRESADO!!!!")

