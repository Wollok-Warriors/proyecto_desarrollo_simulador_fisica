import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

g = 9.81

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
player_vel = pygame.Vector2(0, 0)
player_acc = pygame.Vector2(0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    radius = 64
    pygame.draw.circle(screen, "red", player_pos, radius)

    max_height = screen.get_height() - radius
    min_height = radius

    max_width = screen.get_width() - radius
    min_width = radius

    keys = pygame.key.get_pressed()
    if keys[pygame.K_k] and player_pos.y == max_height:
        player_vel.y = -1000
    if keys[pygame.K_j]:
        player_vel.y += 10
    if keys[pygame.K_h]:
        player_vel.x = -500
    elif keys[pygame.K_l]:
        player_vel.x = 500
    else:
        player_vel.x = 0

    player_acc.y += g

    if player_pos.y > max_height:
        player_acc.y = 0
        player_vel.y = 0
        player_pos.y = max_height
    if player_pos.y < min_height:
        player_acc.y = 0
        player_vel.y = 0
        player_pos.y = min_height

    if player_pos.x > max_width:
        player_acc.x = 0
        player_vel.x = 0
        player_pos.x = max_width
    if player_pos.x < min_width:
        player_acc.x = 0
        player_vel.x = 0
        player_pos.x = min_width


    player_vel += player_acc * dt
    player_pos += player_vel * dt

    pygame.display.flip()
    dt = clock.tick(344) / 1000
