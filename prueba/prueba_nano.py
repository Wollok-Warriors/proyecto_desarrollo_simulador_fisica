##El goat va a ir aprendiendo como todo en la vida
##Por eso es que se crea este archivo, para que mientras se aprende
##todos puedan ver que fue lo que hizo, y quizas.... inspirarse.
##Nazareno José Rodriguez Moyano    17/04/2026

import numpy as np
import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Fondo
    screen.fill("white")

    #Particula y sus movimientos
    pygame.draw.circle(screen, "red", player_pos,400)
    

    #Poner el trabajo en la pantalla
    pygame.display.flip()
    #Delta t mide cuanto tiempo pasa entre cada frame
    dt = clock.tick(60) / 1000
pygame.quit()

