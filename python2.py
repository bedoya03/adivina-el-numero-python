import random

numero_aleatorio = random.randint(1,50)
intentos = 0
max_intentos = 5

while intentos < max_intentos:
    print("------Adivina el numero del 1 al 50-------")
    numero = int(input("Ingresa el numero:"))
    intentos = intentos + 1

    if numero == numero_aleatorio:
     print("GANASTE!! Adivinaste en", intentos, "intentos")
     break

    elif numero > numero_aleatorio:
       print("El numero es menor")

    else:
       print("El numero es mayor")

if numero != numero_aleatorio:
   print("Perdiste, te quedaste sin intentos. EL numero era: ", numero_aleatorio)