print("******BIENVENIDO******")

edadFaltante = 0
edad = int(input("Introduce tu edad: "))

edadFaltante = 100 - edad

with open('edad.txt', 'w') as archivo:
    archivo.write(
        f'TE HACEN FALTA {edadFaltante} AÑOS PARA ALCANZAR HA CUMPLIR 100')

with open('edad.txt', 'r') as archivo:
    nuevoArchivo = archivo.read()

    print(nuevoArchivo)

