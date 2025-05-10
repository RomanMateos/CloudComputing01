nombre_completo = input(print("Escriba su nombre completo"))
edad = input(print("Bienvenido" , {nombre_completo} ," Ingresa tu edad" ))
diasvividos = edad * 365
with open ("dias.txt" , "w") as archivo:
    archivo.write (f"Hola {nombre_completo} has vivido aproximadamente {diasvividos}.")
with open ("dias.txt", "r") as archivo:
    print (archivo.read ())

