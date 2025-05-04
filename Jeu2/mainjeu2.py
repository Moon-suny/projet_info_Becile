import pygame
import random
from pygame.locals import *

pygame.init()

# écran principal
screen_x, screen_y = 1000, 800
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Jeu 2 : Enfuis-toi !")

# couleurs
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen.fill(BLACK)
road_height = 200
scroll_speed = 1.5
nb_routes = 3
line_length = 50
line_width = 10
line_spacing = 50
total_road_width = road_height * nb_routes
start_y = (screen_y - total_road_width) // 2

# Initialisation du défilement des lignes blanches
line_x = 0  # Initialiser la position de la ligne

# routes côte à côte horizontalement
for i in range(nb_routes):
    road_top = start_y + i * road_height
    pygame.draw.rect(screen, GRAY, (0, road_top, screen_x, road_height))

    # Lignes blanches centrales sur chaque route
    x = line_x
    while x < screen_x:
        pygame.draw.rect(screen, WHITE, (
            x, road_top + road_height // 2 - line_width // 2,
            line_length, line_width
        ))
        x += line_length + line_spacing

clock = pygame.time.Clock()

# Initialisation du joueur
player_img = pygame.image.load("jeu2/img/le_nainbecile.png").convert_alpha()
player_x, player_y = 100, screen_y / 2  # Position initiale
speed_player = 1  # Vitesse du joueur
player_img = pygame.transform.scale(player_img, (100, 100))
zone_d_insertitude = 10

# Initialisation du méchant
mechant_img = pygame.image.load("jeu2/img/scientifique_fou.png")
mechant_x, mechant_y = screen_x - 80, 50  # Position initiale du méchant
mechant_img = pygame.transform.scale(mechant_img, (100, 100))  # Taille du méchant
speed_mechant = 1.5

# Ne pas suivre le joueur à la trace
time_att = 50
dernier_deplacement = pygame.time.get_ticks()

# Initialisation des tonneaux à éviter
tonneau_img = pygame.image.load("jeu2/img/poubelle.png")
tonneau_x, tonneau_y = screen_x - 50, screen_y / 2
tonneau_lance = False  # Savoir si le tonneau est lancé
tonneau_img = pygame.transform.scale(tonneau_img, (40, 40))
dechets_mask = pygame.mask.from_surface(tonneau_img)


# Initialisation des obstacles à éviter
dechets = []
dernier_dechet = -1000
intervalle_dechet = 1500

# Variables de temps pour le tir du projectile
chargement_tire = 1000
dernier_tire = 0

# Coordonnées du joueur
player_taille_x, player_taille_y = player_img.get_width(), player_img.get_height()
# Coordonnées du méchant
mechant_taille_x, mechant_taille_y = mechant_img.get_width(), mechant_img.get_height()
# Coordonnées du tonneau
tonneau_taille_x, tonneau_taille_y = tonneau_img.get_width(), tonneau_img.get_height()

# Fonction de mise à feu
def ini_du_tire():
    global tonneau_x, tonneau_y, tonneau_lance, dernier_tire
    if not tonneau_lance and pygame.time.get_ticks() - dernier_tire > chargement_tire:
        tonneau_x, tonneau_y = mechant_x, mechant_y  # Position initiale sur le méchant
        tonneau_lance = True
        dernier_tire = pygame.time.get_ticks()

# Création des masques
player_mask = pygame.mask.from_surface(player_img)
tonneau_mask = pygame.mask.from_surface(tonneau_img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvement
    touches = pygame.key.get_pressed()
    if touches[K_LEFT] and player_x > 0:
        player_x -= speed_player
    if touches[K_RIGHT] and player_x < screen_x - player_taille_x:
        player_x += speed_player + 0.25
    if touches[K_UP] and player_y > 0:
        player_y -= speed_player - 0.5
    if touches[K_DOWN] and player_y < screen_y - player_taille_y:
        player_y += speed_player - 0.5

    # Suivi du joueur
    time_act = pygame.time.get_ticks()
    if time_act - dernier_deplacement > time_att:
        if abs(mechant_y - player_y) > 20:
            if mechant_y > player_y:
                mechant_y -= speed_mechant
            elif mechant_y < player_y:
                mechant_y += speed_mechant
        dernier_deplacement = time_act

    # Apparition aléatoire de déchets
    if pygame.time.get_ticks() - dernier_dechet > intervalle_dechet:
        aleatoire_y = random.randint(50, screen_y - 50)
        dechets.append([screen_x, aleatoire_y])
        dernier_dechet = pygame.time.get_ticks()

    for dechet in dechets:
        dechet_x, dechet_y = dechet[0], dechet[1]
        dechet[0] -= 1.5  
        if dechet[0] < 0:
            dechets.remove(dechet)
    
    offset_x = player_x - dechet_x
    offset_y = player_y - dechet_y

    # Tir de tonneau
    if abs(player_y - mechant_y) < 20:
        ini_du_tire()
    if tonneau_lance:
        tonneau_x -= 2  
        if tonneau_x < 0:
            tonneau_lance = False
    
    #collision entre le tonneau et le player
    if player_mask.overlap(dechets_mask, (offset_x + zone_d_insertitude, offset_y + zone_d_insertitude)):
        print("game over - collision avec un déchet")
        pygame.time.delay(1000)
        running = False
    
    # Fin du jeu après 30 secondes
    if pygame.time.get_ticks() > 30000:
        print("win")
        pygame.time.delay(1000)
        running = False

    # Affichage
    screen.fill(BLACK)

    #  plusieurs routes côte à côte 
    line_x -= scroll_speed
    if line_x <= -(line_length + line_spacing):
        line_x = 0

    for i in range(nb_routes):
        road_top = start_y + i * road_height
        pygame.draw.rect(screen, GRAY, (0, road_top, screen_x, road_height))

        x = line_x
        while x < screen_x:
            pygame.draw.rect(screen, WHITE, (
                x, road_top + road_height // 2 - line_width // 2,
                line_length, line_width
            ))
            x += line_length + line_spacing

    # Blit au-dessus de la route
    screen.blit(player_img, (player_x, player_y))
    screen.blit(mechant_img, (mechant_x, mechant_y))

    if tonneau_lance:
        screen.blit(tonneau_img, (tonneau_x, tonneau_y))

    for dechet in dechets:
        screen.blit(tonneau_img, (dechet[0], dechet[1]))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
