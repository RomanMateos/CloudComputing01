nombre  = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

diff = 100 - edad

resultado = f"Hola {nombre} \nTe faltan {diff} anos para llegar a 100 anos de edad\n"

with open("edad.txt","w") as file:
    file.write(resultado)
