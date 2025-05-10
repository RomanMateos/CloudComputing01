print("Noemi Bello")
edad = int(input("Ingresa tu edad:"))

años_faltantes = 100 - edad
Total_años_faltantes=años_faltantes

print (f"Te faltan {Total_años_faltantes:.0f} para cumplir 100 años")

with open("edad.txt", "w") as archivo:
    archivo.write(f"Te faltan {Total_años_faltantes:.0f} para cumplir 100 años")

