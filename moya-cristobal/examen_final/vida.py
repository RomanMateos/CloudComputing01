print("CRISTOBAL GABRIEL MOYA FLORES")

edad = int(input("Ingresa tu edad: "))

dias_vividos = edad * 365


with open ("dias.txt", "w") as archivo :
    archivo.write (f"has vivido {dias_vividos} dias.\n")

print("Haz vivido Aproximandamente", dias_vividos, "Dias")
