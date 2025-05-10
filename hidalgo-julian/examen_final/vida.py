print('Julian Hidalgo')
edad = int(input('Ingrese su edad actual: '))
dias = 365
calculo = dias * edad

print(f'Usted ha vivido proximadamente unos: {calculo} dias')

with open('dias.txt','w') as archivo:
     archivo.write(f'Usted ha vivido proximadamente unos: {calculo} dias')
     