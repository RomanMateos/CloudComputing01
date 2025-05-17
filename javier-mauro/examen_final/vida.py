print("Javier Ignacio Mauro Corrales")

edad = int(input("Ingrese su edad: "))

diasvividos = edad * 365

with open("dias.txt", "w") as f:

	print("Has vivido un estimado de", diasvividos, "dias")
with open("dias.txt", "r") as f:

	print(f.read())
