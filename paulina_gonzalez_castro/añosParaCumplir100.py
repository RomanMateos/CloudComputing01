#añosParaCumplir100

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
faltaPara100 = 100 - edad

if edad < 100:
    print(f"Le faltan {faltaPara100} años para llegar a los 100' .")
else:
    print("Ya cumplió los 100 años")


with open("edad.txt", "w") as archivo:
    archivo.write(f"Te faltan {faltaPara100} años para cumplir 100.\n")

with open("edad.txt", "r") as archivo:
    print(archivo.read())
