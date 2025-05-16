print("Alexander Simpertigue")

edad = int(input("Ingrese su edad: "))

dias = edad * 365 


with open ("dias.txt", "w") as archivo :
    archivo.write (f"has vivido {dias} dias.\n")

print(f"has vivido {dias} dias.")
