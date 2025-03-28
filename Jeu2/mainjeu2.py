import pygame
from pygame.locals import *

pygame.init()

# écran principal
screen_x, screen_y = 1000, 600
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Jeu 2 : Enfuis-toi !")

# Initialisation du player
player_img = pygame.image.load("jeu2/img/10581090.png").convert_alpha()
player_x, player_y = 100, screen_y/2  # Position initiale
speed_player = 2  # Vitesse du joueur
player_img = pygame.transform.scale (player_img,(100,100))

#initialisation du mechant
mechant_img = pygame.image.load("jeu2/img/Logo_cable_test.png")
mechant_x, mechant_y = screen_x - 60 , screen_y # position initiale du mechant
mechant_img = pygame.transform.scale(mechant_img,(50,50)) #taille du méchant

#initialisation des tonneau à éviter
tonneau_img = pygame.image.load("jeu2/img/Roue.gif")
tonneau_x, tonneau_y = screen_x - 50, screen_y/2
tonneau_img = pygame.transform.scale(tonneau_img,(30,30))

# coordonner du joueur
player_cord_x, player_cord_y = player_img.get_width(), player_img.get_height()

#coordonner du mechant
mechant_cord_x, mechant_cord_y =  mechant_img.get_width(), mechant_img.get_height()

#coordonner du tonneau
tonneau_cord_x, tonneau_cord_y =  tonneau_img.get_width(), tonneau_img.get_height()




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
        player_x += speed_player - 1.25
    if touches[K_UP] and player_y > 0:
        player_y -= speed_player - 0.5
    if touches[K_DOWN] and player_y < screen_y - player_cord_y:
        player_y += speed_player -0.5

    
    #action de danger
    if touches:
        
        while tonneau_cord_x >= 0 :
            tonneau_cord_x -= 5
        mechant_y = player_cord_y



    # Affichage
    screen.fill((224, 176, 255 ))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(mechant_img,(mechant_x,mechant_y))
    screen.blit(tonneau_img,(tonneau_x, tonneau_y))
    pygame.display.update()  

pygame.quit()