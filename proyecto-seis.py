# Proyecto 6: Juego de Memoria
# Descripción: Un juego de memoria donde el usuario tiene que encontrar parejas de cartas iguales.

import pygame
import random

# Inicializar Pygame
pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((1200, 900))

# Cargar imágenes de las cartas
imagenes_cartas = {i: pygame.transform.scale(pygame.image.load(f'carta_{i}.jpg'), (100, 100)) for i in range(1, 9)}

# Crear tablero de cartas
def crear_tablero():
    cartas = list(range(1, 9)) * 2
    random.shuffle(cartas)
    tablero = []
    for i in range(4):
        fila = cartas[i*4:(i+1)*4]
        tablero.append(fila)
    return tablero

tablero = crear_tablero()

# Variables para el juego
cartas_seleccionadas = []
puntos = 0
intentos = 0

# Loop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            fila = y // 100
            columna = x // 100
            if fila < len(tablero) and columna < len(tablero[0]) and len(cartas_seleccionadas) < 2:
                cartas_seleccionadas.append((fila, columna))
                intentos += 1

    # Comprobar si las cartas seleccionadas coinciden
    if len(cartas_seleccionadas) == 2:
        fila1, columna1 = cartas_seleccionadas[0]
        fila2, columna2 = cartas_seleccionadas[1]
        if tablero[fila1][columna1] == tablero[fila2][columna2]:
            puntos += 1
            cartas_seleccionadas = []
        else:
            pygame.time.wait(1000)  # Espera un segundo antes de ocultar las cartas nuevamente
            cartas_seleccionadas = []

    # Rellenar la pantalla con un color de fondo
    screen.fill((255, 255, 255))

    # Dibujar las cartas en la pantalla
    for i, fila in enumerate(tablero):
        for j, carta in enumerate(fila):
            if (i, j) in cartas_seleccionadas:
                screen.blit(imagenes_cartas[carta], (j*100, i*100))
            else:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(j*100, i*100, 100, 100))

    # Mostrar puntuación e intentos
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"Puntos: {puntos}, Intentos: {intentos}", True, (0, 0, 0))
    screen.blit(texto, (20, 560))

    pygame.display.flip()

pygame.quit()
