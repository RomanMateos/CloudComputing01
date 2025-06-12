print("Marcelo Martabit Donoso")
edad = int(input("Ingresa tu edad actual: "))

dias = edad * 365

resultado = str(dias)

with open("dias.txt", "w") as file:
    file.write(resultado)


