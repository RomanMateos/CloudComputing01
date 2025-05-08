nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

edad2 = 100 - edad

mensaje = (f'Hola {nombre}, en {edad2} años tendrás 100 años.')

print(mensaje)

with open('edad.txt', 'w') as archivo:
	archivo.write(mensaje)


