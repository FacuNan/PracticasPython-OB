secreto = 50


numero = 0
while numero != secreto:
    numero= int(input("Ingrese unnumero: "))
    if(numero > secreto):
        print("Muy alto")
        continue
    if numero < secreto:
        print("Muy bajo")
        continue
print("Acertaste")