# Proyecto 5: Generador de Historias
# Descripción: Un programa que genera historias aleatorias
# usando plantillas y palabras suministradas por el usuario.

def generar_historia():
    lugar = input("Ingresa un lugar: ")
    personaje = input("Ingresa un personaje: ")
    objeto = input("Ingresa un objeto: ")
    
    historia = f"Había una vez en {lugar}, un/a {personaje} que encontró un/a {objeto} mágico."
    print(historia)

generar_historia()
