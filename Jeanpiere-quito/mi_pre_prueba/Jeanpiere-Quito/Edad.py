   
Nombre = input("Nombre Apellido:") 

edad = int(input("Cual es tu edad?"))
faltan = 100 - edad 

with open("edad.txt", "w" ) as archivo: 
    archivo.write (f"te faltan {faltan} años para cumplir 100.\n")

with open("edad.txt", "r" ) as archivo:
    print(archivo.read())
