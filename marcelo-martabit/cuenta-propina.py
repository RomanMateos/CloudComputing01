cuenta = int(input("Ingresa el total e tu cuenta: "))
propina = int(input("Ingresa porcentaje de propina: "))

total_propina = cuenta * propina / 100
print("Monto de propina: ",int(total_propina))

total_pagar = cuenta + total_propina
print("Total a pagar: ",int(total_pagar))
