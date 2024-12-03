import random

numero_secreto = random.randint(1,100)
adivinado = False

print(numero_secreto)

print("¡BIENVENIDO AL JUEGO DE ADIVINAR EL NÚMERO SECRETO!!")

while not adivinado:
    numero = int(input("Indroduce un número de 1 al 99:")) # TODO: convertir a número

    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")