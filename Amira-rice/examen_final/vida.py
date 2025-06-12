
name = input('Ingrese su nombre: \n')
print('Bienvenid@ ' +name)
age = int(input('Ingrese su edad: \n'))

dias = age * 365

print('Usted ha vivido aproximadamente ' +str(dias)+ ' dias')

with open('dias.txt','w') as archivo:
    archivo.write('Usted ha vivido aproximadamente ' +str(dias)+ ' dias')
