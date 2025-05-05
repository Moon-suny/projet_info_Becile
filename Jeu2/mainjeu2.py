import pygame
import random 
import os
import subprocess
from pygame.locals import *
#from PIL import Image, ImageSequence

pygame.init()

# écran principal
screen_x, screen_y = 1000, 800
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Enfuis-toi !")

# Initialisation du player
player_img = pygame.image.load("jeu2/img/10581090.png").convert_alpha()
player_x, player_y = 100, screen_y/2  # Position initiale
speed_player = 1.5  # Vitesse du joueur
player_img = pygame.transform.scale (player_img,(100,100))

#initialisation du mechant
mechant_img = pygame.image.load("jeu2/img/Logo_cable_test.png")
mechant_x, mechant_y = screen_x - 60 , 50 # position initiale du mechant
mechant_img = pygame.transform.scale(mechant_img,(50,50)) #taille du méchant
speed_mechant = 3

# ne pas suivre le joueur a la trace
time_att = 50
dernier_deplacement = pygame.time.get_ticks()

#initialisation des tonneaux à éviter
tonneau_img = pygame.image.load("jeu2/img/Logo_cable_test.png")
tonneau_x, tonneau_y = screen_x - 50, screen_y/2
tonneau_lance = False # savoir si le tonneau est lancer
tonneau_img = pygame.transform.scale(tonneau_img,(40,40))


# initialisation des obsatcles a éviter
dechets= []
dernier_dechet = -1000
intervalle_dechet = 1500

 # toute les variables de temps pour le tire du projectile
chargement_tire = 1000
dernier_tire = 0


# coordonner du joueur
player_taille_x, player_taille_y = player_img.get_width(), player_img.get_height()
#coordonner du mechant
mechant_taille_x, mechant_taille_y =  mechant_img.get_width(), mechant_img.get_height()
#coordonner du tonneau
tonneau_taille_x, tonneau_taille_y =  tonneau_img.get_width(), tonneau_img.get_height()


#fonction de mise a feu
def ini_du_tire():
    global tonneau_x, mechant_x, tonneau_y, tonneau_lance, dernier_tire
    if not tonneau_lance and pygame.time.get_ticks() - dernier_tire > chargement_tire :
        tonneau_x, tonneau_y = mechant_x, mechant_y #position initiale sur le mechant
        tonneau_lance = True
        dernier_tire = pygame.time.get_ticks()

#création des mask
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
        player_x += speed_player - 1.25
    if touches[K_UP] and player_y > 0:
        player_y -= speed_player - 0.5
    if touches[K_DOWN] and player_y < screen_y - player_taille_y:
        player_y += speed_player -0.5

    
    # suivit du joueur
    time_act = pygame.time.get_ticks()
    if time_act - dernier_deplacement > time_att :
        if abs ( mechant_y - player_y ) > 20 :
            if mechant_y > player_y :
                mechant_y -= speed_mechant
            elif mechant_y < player_y :
                mechant_y += speed_mechant
        dernier_deplacement = time_act
    
    #apparition alétatoire de dechet
    if pygame.time.get_ticks() - dernier_dechet > intervalle_dechet :
        aleatoire_y = random.randint(50, screen_y-50)
        dechets.append([screen_x, aleatoire_y])
        dernier_dechet = pygame.time.get_ticks()
    
    for dechet in dechets :
        dechet[0] -= 1.5 # vitesse de dechet
        if dechet[0] < 0 :
            dechets.remove(dechet)
    
    # tire de tonneau
    if abs(player_y - mechant_y) < 20 :
        ini_du_tire()
    if tonneau_lance :
        tonneau_x -= 2 # vitesse du tonneau
        if tonneau_x < 0 :
            tonneau_lance = False
    if tonneau_lance and player_mask.overlap(tonneau_mask, (player_x - tonneau_x, player_y - tonneau_y)) :
        print("game over")
        win = False
        running = False


 #fin du jeu après 30 secondes
    if pygame.time.get_ticks() > 30000 :
        print("win")
        win = True
        running = False

        

    # Affichage
    screen.fill((224, 176, 255 ))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(mechant_img,(mechant_x,mechant_y))
    if tonneau_lance :
        screen.blit(tonneau_img,(tonneau_x, tonneau_y))
    for dechet in dechets :
        screen.blit(tonneau_img,(dechet[0], dechet[1]))
    pygame.display.update()  

pygame.quit()

if win:
    chemin = os.path.abspath('../projet_info_Becile/Cinematique/Dialogues/Dialogue-3.py')
    subprocess.run(['python', chemin]) 
else:
    chemin = os.path.abspath('../projet_info_Becile/Cinematique/Dialogues/Dialogue-4.py')
    subprocess.run(['python', chemin])
