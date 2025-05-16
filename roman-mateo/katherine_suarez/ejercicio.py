
print("Nombre completo: Juan Pérez")  


edad = int(input("Introduce tu edad en años: "))


dias_vividos = edad * 365 


with open("dias.txt", "w") as archivo:
    archivo.write(f"Has vivido aproximadamente {dias_vividos} días.\n")


with open("dias.txt", "r") as archivo:
    contenido = archivo.read()
    print("\nContenido de 'dias.txt':")
    print(contenido)
