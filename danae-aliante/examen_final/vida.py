print("Mi nombre es: Noemi Bello")  

edad = int(input("¿Cuántos años tienes? "))

dias_vividos = edad * 365

with open("dias.txt", "w") as archivo:
    archivo.write(f"Has vivido aproximadamente {dias_vividos} días.")

with open("dias.txt", "r") as archivo:
    print(archivo.read())
