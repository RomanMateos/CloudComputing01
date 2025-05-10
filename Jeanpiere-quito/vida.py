print ("Jeanpiere quito")  
edad_usuaio = int(input("ingrese su edad:"))
dias_vividos = edad_usuaio * 365

with open("dias.txt", "w" ) as archivo: 
    archivo.write (f"usted a vivido  {dias_vividos} dias\n")

with open("dias.txt", "r" ) as archivo:
    print(archivo.read())

