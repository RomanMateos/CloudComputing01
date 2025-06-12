print('Julian Hidalgo')
edad = int(input ('Ingresa tu edad: '))
anios = 100 - edad
print(f'Te faltan: {anios} para llegar a los 100')

with open('edad.txt','w') as archivo:
    archivo.write(f'Te faltan: {anios} para llegar a los 100')