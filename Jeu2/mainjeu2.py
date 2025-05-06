import pygame
import random
import os
import subprocess 
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

road_height = 200
scroll_speed = 4
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
player_img = pygame.image.load("jeu2/img/player_deux.png").convert_alpha()
player_x, player_y = (100, screen_y / 2) 
speed_player = 2.5  
player_img = pygame.transform.scale(player_img, (200, 200))

# Initialisation du méchant
mechant_img = pygame.image.load("jeu2/img/scientifique_fou.png")
mechant_x, mechant_y = (screen_x - 80, 50)
mechant_img = pygame.transform.scale(mechant_img, (100, 100))  
speed_mechant = 1.5

# Ne pas suivre le joueur à la trace
time_att = 50
dernier_deplacement = pygame.time.get_ticks()

# Initialisation des tonneaux à éviter
tonneau_img = pygame.image.load("jeu2/img/poubelle.png")
tonneau_x, tonneau_y = screen_x - 50, screen_y / 2
tonneau_lance = False  # Savoir si le tonneau est lancé
tonneau_img = pygame.transform.scale(tonneau_img, (40, 40))
dechet_mask = pygame.mask.from_surface(tonneau_img)



# Initialisation des obstacles à éviter
dechets = []
dernier_dechet = -1000
intervalle_dechet = 400 # Intervalle entre les déchets en millisecondes

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
        tonneau_x, tonneau_y = mechant_x, mechant_y 
        tonneau_lance = True
        dernier_tire = pygame.time.get_ticks()

#fonction de fin du jeu
def game_over(message):
    screen.fill(BLACK)
    font = pygame.font.SysFont("Arial", 30)
    texte = font.render(message, True, WHITE)
    screen.blit(texte, (screen_x // 2 - texte.get_width() // 2, screen_y // 2 - texte.get_height() // 2))
    pygame.display.flip()


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
        player_x += speed_player
    if touches[K_UP] and player_y > 0:
        player_y -= speed_player
    if touches[K_DOWN] and player_y < screen_y - player_taille_y:
        player_y +=  speed_player

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
        dechet[0] -= 5  # Vitesse de déplacement des déchets  
        if dechet[0] < 0:
            dechets.remove(dechet)
    

    # Tir de tonneau
    if abs(player_y - mechant_y) < 20:
        ini_du_tire()
    if tonneau_lance:
        tonneau_x -= 2  
        if tonneau_x < 0:
            tonneau_lance = False
    
    #collision entre le tonneau et le player
    if player_mask.overlap(tonneau_mask, (tonneau_x - player_x, tonneau_y - player_y)):
        #game_over("tu t'es manger un grosse poubelle")
        #pygame.time.delay(1000)
        win = False
        running = False

    for dechet in dechets:
        if player_mask.overlap(dechet_mask, (dechet[0] - player_x, dechet[1] - player_y)):
            #game_over("tu t'es manger un grosse poubelle")
            #pygame.time.delay(1000)
            win = False
            running = False


    #fin du jeu après 30 secondes
    if pygame.time.get_ticks() > 30000 :
        win = True
        running = False

        

    # Affichage
    
    screen.fill(BLACK)

    # routes
    line_x -= scroll_speed
    if line_x <= -(line_length + line_spacing):
        line_x = 0

    for i in range(nb_routes):
        road_top = start_y + i * road_height
        pygame.draw.rect(screen, GRAY, (0, road_top, screen_x, road_height))

        x = line_x
        while x < screen_x:
            pygame.draw.rect(screen, WHITE, (x, road_top + road_height // 2 - line_width // 2, line_length, line_width))           
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



if win:
    chemin = os.path.abspath('../projet_info_Becile/Cinematique/Dialogues/Dialogue-3.py')
    subprocess.run(['python', chemin]) 
else:
    chemin = os.path.abspath('../projet_info_Becile/Cinematique/Dialogues/Dialogue-4.py')
    subprocess.run(['python', chemin])