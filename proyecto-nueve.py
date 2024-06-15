# Proyecto 9: Generador de Poemas
# Descripción: Un programa que genera poemas aleatorios a partir de palabras suministradas por el usuario.

import random

def generar_poema():
    sustantivos = ["estrella", "mar", "amor", "flor"]
    adjetivos = ["brillante", "profundo", "dulce", "hermoso"]
    verbos = ["brilla", "canta", "baila", "sueña"]
    
    poema = f"La {random.choice(sustantivos)} {random.choice(verbos)} {random.choice(adjetivos)}.\n" \
            f"Un {random.choice(sustantivos)} {random.choice(adjetivos)} {random.choice(verbos)}.\n"
    
    print(poema)

generar_poema()
