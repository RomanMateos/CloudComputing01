print("Nombre: Edixon ELias")

edad = int(input("Ingresa tu edad: "))

res = "Te faltan"
ult = 100-edad
ado = "años para llegar a 100"

with open("edad.txt", "w") as archivo:
  archivo.write(res+str(ult)+ado)
