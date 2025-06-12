nombre = input("Ingrese su nombre")
edad = int(input("Ingrese su edad"))
dias = edad * 364
with open("dias.txt", "w") as archivo:
    archivo.write(f"Haz vivido ", dias)

with open("dias.txt", "r") as archivo:
    print(archivo.read())

