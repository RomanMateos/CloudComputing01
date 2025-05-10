print("Jorge Uribe")
edad = int(input("¿Cuál es tu edad? "))
faltan = 100 - edad
with open("edad.txt", "w") as archivo:
    archivo.write(f"Te faltan {faltan} años para cumplir 100.\n")

with open("edad.txt", "r") as archivo:
    print(archivo.read())
