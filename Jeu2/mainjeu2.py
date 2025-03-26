import pygame
from pygame.locals import *

pygame.init()

# écran principal
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeu 2 : Enfuis-toi !")

#creation de mask (percution)



# Initialisation du player
player_img = pygame.image.load("jeu2/img/10581090.png").convert_alpha()
player_x, player_y = 250, 250  # Position initiale
speed_player = 5  # Vitesse du joueur
player_img = pygame.transform.scale (player_img,(100,100))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvement
    touches = pygame.key.get_pressed()
    if touches[K_LEFT]:
        player_x -= speed_player
    if touches[K_RIGHT]:
        player_x += speed_player
    if touches[K_UP]:
        player_y -= speed_player
    if touches[K_DOWN]:
        player_y += speed_player

    # Affichage
    screen.fill((255, 255, 255))
    screen.blit(player_img, (player_x, player_y))

    pygame.display.update()  

pygame.quit()