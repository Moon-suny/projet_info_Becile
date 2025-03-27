import pygame
from pygame.locals import *

pygame.init()

# écran principal
screen_x, screen_y = 1000, 600
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Jeu 2 : Enfuis-toi !")

# Initialisation du player
player_img = pygame.image.load("jeu2/img/10581090.png").convert_alpha()
player_x, player_y = 50, screen_y/2  # Position initiale
speed_player = 3  # Vitesse du joueur
player_img = pygame.transform.scale (player_img,(50,50))

# coordonner du joueur
player_cord_x, player_cord_y = player_img.get_width(), player_img.get_height()





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvement
    touches = pygame.key.get_pressed()
    if touches[K_LEFT] and player_x > 0:
        player_x -= speed_player
    if touches[K_RIGHT] and player_x < screen_x - player_cord_x:
        player_x += speed_player
    if touches[K_UP] and player_y > 0:
        player_y -= speed_player
    if touches[K_DOWN] and player_y < screen_y - player_cord_y:
        player_y += speed_player

    # Affichage
    screen.fill((224, 176, 255 ))
    screen.blit(player_img, (player_x, player_y))

    pygame.display.update()  

pygame.quit()