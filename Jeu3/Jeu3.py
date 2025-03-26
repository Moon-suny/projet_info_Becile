import pygame 
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jeu')

# Chargement des images
barre_img = pygame.image.load('Jeu3/img/barre.png')
Background_img = pygame.image.load('Jeu3/img/Backgrnd.png')
roue_img = pygame.image.load('Jeu3/img/Roue.gif')

# Création du sol (blanc pour le masque, invisible pour l'affichage)
sol_x, sol_y = 0, screen_height - 50  # Position en bas de l'écran
sol_surface = pygame.Surface((1000, 50), pygame.SRCALPHA)
sol_surface.fill((255, 255, 255))  # Blanc = partie solide pour le masque
sol_mask = pygame.mask.from_surface(sol_surface)

# Chargement du joueur
player_img = pygame.image.load("Jeu3/img/10581090.png").convert_alpha()
player_x, player_y = 100, 100  # Position initiale
player_speed = 5  # Vitesse de déplacement
player_img = pygame.transform.scale(player_img, (50, 50))

# Création des masques
player_mask = pygame.mask.from_surface(player_img)
barre_mask = pygame.mask.from_surface(barre_img)

# Boucle de jeu
running = True
while running:
    screen.blit(Background_img, (0, 0))
    screen.blit(barre_img, (0, 0))
    screen.blit(sol_surface, (sol_x, sol_y))  # Dessiner le sol en bas

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Commande du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: 
        player_x -= player_speed
    if keys[pygame.K_RIGHT]: 
        player_x += player_speed
    if keys[pygame.K_UP]: 
        player_y -= player_speed
    if keys[pygame.K_DOWN]: 
        player_y += player_speed

    # Collision 
    offset_x = sol_x - player_x  # Décalage horizontal entre le sol et le joueur
    offset_y = sol_y - player_y  # Décalage vertical entre le sol et le joueur

    if barre_mask.overlap(player_mask, (player_x, player_y)) != None:
        collision = True
        if (player_x, player_y) < barre_mask.overlap(player_mask, (player_x, player_y)) :
            player_x -= player_speed
            player_y -= player_speed
    elif player_mask.overlap(sol_mask, (offset_x, offset_y)):
        collision = True
        player_y -= player_speed
    else:
        collision = False
        player_y += player_speed


    # Afficher le joueur
    screen.blit(player_img, (player_x, player_y))

    pygame.display.update()
