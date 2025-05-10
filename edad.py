name = input("Paulina Francisca Gonzalez Castro")
age = input("ingrese edad actual:")
diasVividos = age * 365

with open ("edad.txt", "w") as f:
    f.write(f"Has vivido {diasVividos} dias \n")
with open ("edad.txt", "r") as f:
    print(f.read())