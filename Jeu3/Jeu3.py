import pygame
from pygame.locals import *

# --- Initialisation de Pygame ---
pygame.init()

# --- Constantes de l'écran ---
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jeu 3')

# --- Constantes du jeu ---
PLAYER_SPEED = 3
GRAVITY = 0.6 
JUMP_STRENGTH = -21 
SOL_HAUTEUR = 50    

# Joueur
player_img_orig = pygame.image.load("Jeu3/img/10581090.png").convert_alpha()
# Barre (UNE SEULE image maintenant)
barre_img = pygame.image.load('Jeu3/img/barre.png').convert_alpha()
# Fond d'écran
Background_img = pygame.image.load('Jeu3/img/Backgrnd.png').convert()


# --- Configuration du Joueur ---
player_width = 55
player_height = 75
player_img = pygame.transform.scale(player_img_orig, (player_width, player_height))
player_rect = player_img.get_rect()
player_rect.x = 100
player_rect.y = 100
player_vy = 0
player_mask = pygame.mask.from_surface(player_img)
on_ground = False

# --- Configuration de la Barre ---

barre_rect = barre_img.get_rect(topleft=(0, 0))
barre_mask = pygame.mask.from_surface(barre_img) # Masque de collision pour la barre

# --- Création du Sol ---
sol_y = screen_height - SOL_HAUTEUR

sol_surface = pygame.Surface((screen_width, SOL_HAUTEUR)) 
sol_surface.fill((255, 255, 255)) # Remplir en blanc
sol_surface.set_alpha(100)

sol_rect = sol_surface.get_rect()
sol_rect.x = 0 
sol_rect.y = sol_y

# mask du sol
sol_mask = pygame.mask.from_surface(sol_surface)


# Boucle de Jeu
running = True
clock = pygame.time.Clock()

while running:
    # --- Gestion des Événements ---
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

            

    # --- Gestion des Entrées ---
    keys = pygame.key.get_pressed()

    move_x = 0
    if keys[pygame.K_LEFT]:
        move_x = PLAYER_SPEED* (-1)
    if keys[pygame.K_RIGHT]:
        move_x = PLAYER_SPEED
    if keys[pygame.K_UP] and on_ground:
        player_vy = JUMP_STRENGTH
        on_ground = False

    # --- Mise à jour de la Physique ---
    player_vy += GRAVITY
    max_fall_speed = 10  # Limite de vitesse de chute
    if player_vy > max_fall_speed:
        player_vy = max_fall_speed

    on_ground = False # Réinitialiser avant les vérifications

    # --- Détection et Réponse aux Collisions ---
    player_rect.x += move_x
    offset_barre_x = barre_rect.x - player_rect.x
    offset_barre_y = barre_rect.y - player_rect.y


    if player_mask.overlap(barre_mask, (offset_barre_x, offset_barre_y)):
        if move_x > 0: # Allait à droite
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.x -= 1
                player_rect.y -= 1
        elif move_x < 0: # Allait à gauche
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.y -= 1
                player_rect.x += 1

    # Mouvement Vertical et Collisions Verticales
    player_rect.y += int(player_vy)

    collided_vertically_barre = False # Indicateur spécifique pour la barre

    # Collision verticale avec la BARRE
    offset_barre_x = barre_rect.x - player_rect.x
    offset_barre_y = barre_rect.y - player_rect.y
    if player_mask.overlap(barre_mask, (offset_barre_x, offset_barre_y)):
        if player_vy > 0:
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.y -= 1
            player_vy = 0
            on_ground = True
            collided_vertically_barre = True
        elif player_vy < 0:
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.y += 1
            player_vy = 0


    if not collided_vertically_barre:
        offset_sol_x = sol_rect.x - player_rect.x
        offset_sol_y = sol_rect.y - player_rect.y

        if player_mask.overlap(sol_mask, (offset_sol_x, offset_sol_y)):

            if player_vy >= 0:

                while player_mask.overlap(sol_mask, (sol_rect.x - player_rect.x, sol_rect.y - player_rect.y)):
                    player_rect.y -= 1

                    if sol_rect.y - player_rect.bottom > 5:
                         print("Ajustement excessif collision sol, arrêt.")
                         break

                player_vy = 0
                on_ground = True

    # --- Limites de l'écran ---
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > screen_width:
        player_rect.right = screen_width


    # --- Affichage ---
    screen.blit(Background_img, (0, 0))
    screen.blit(barre_img, barre_rect)
    screen.blit(sol_surface, sol_rect) 
    screen.blit(player_img, player_rect)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
exit()