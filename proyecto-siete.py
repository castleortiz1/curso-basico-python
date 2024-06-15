# Proyecto 7: Juego de Laberinto
# Descripción: Crear un laberinto donde el usuario debe mover un personaje
# desde el inicio hasta la salida.

import pygame

# Inicializar Pygame
pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((600, 400))

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Posición inicial del jugador
player_pos = [50, 50]

# Loop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Mover esta línea aquí
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player_pos[0] < 550:
        player_pos[0] += 5
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN] and player_pos[1] < 350:
        player_pos[1] += 5

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (*player_pos, 50, 50))
    pygame.display.flip()

pygame.quit()

