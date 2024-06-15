# Semana 4: Proyectos Divertidos
# Clase 7: Proyecto 1 - Adivina el Número
# Descripción: Crear un juego donde el usuario debe adivinar un número entre 1 y 10.
# Librería: random para generar números aleatorios.

import random

numero_secreto = random.randint(1, 10)
adivina = int(input("Adivina el número (entre 1 y 10): "))

if adivina == numero_secreto:
    print("¡Adivinaste!")
else:
    print(f"No adivinaste, el número era {numero_secreto}.")
