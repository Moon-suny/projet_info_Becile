import pygame
import pygame_gui
import os
import subprocess
import time as time

pygame.init()

def lancement():
    #print("Lancement du jeu 3")
    chemin = os.path.abspath('../projet_info_Becile/Jeu3/Jeu3.py')
    subprocess.run(['python', chemin])


# Set up the game window
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bécile contre attaque !")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


# Dialogue box properties
dialogue_box_width = 800
dialogue_box_height = 200
dialogue_box_x = (screen_width - dialogue_box_width) // 2
dialogue_box_y = screen_height - screen_height*0.05 - dialogue_box_height
dialogue_box = False

# Pygame GUI manager
manager = pygame_gui.UIManager((screen_width, screen_height))



#création du background
background = pygame.image.load("Cinematique/img/intérieur-navire.png").convert_alpha()
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()

# Création du personnage
becile = pygame.image.load("../projet_info_Becile/Cinematique/img/le_nain_becile.png").convert_alpha()
becile = pygame.transform.scale(becile, (450, 450))
becile_rect = becile.get_rect()

# Création du joeur
Joueur = pygame.image.load("../projet_info_Becile/Cinematique/img/creature_jeu.png").convert_alpha()
Joueur = pygame.transform.scale(Joueur, (200, 100))
Joeur_rect = Joueur.get_rect()

# Création disque
disque = pygame.image.load("../projet_info_Becile/Cinematique/img/Disque De bécile.jpg").convert_alpha()
disque = pygame.transform.scale(disque, (100, 100))
disque_rect = disque.get_rect()


# Création button
button2_width = 150
button2_height = 30
button2_x = dialogue_box_x + dialogue_box_width*0.95 - button2_width
button2_y = dialogue_box_y + dialogue_box_height*0.95 - button2_height
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button2_x, button2_y, button2_width, button2_height),
                                      text='Ce réjouire !',
                                      manager=manager)

# Création button
button3_width = 100
button3_height = 30
button3_x = dialogue_box_x + dialogue_box_width*0.95 - button3_width
button3_y = dialogue_box_y + dialogue_box_height*0.95 - button3_height
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button3_x, button3_y, button3_width, button3_height),
                                      text='Suivant',
                                      manager=manager)

# Création button
button4_width = 100
button4_height = 30
button4_x = dialogue_box_x + dialogue_box_width*0.95 - button4_width
button4_y = dialogue_box_y + dialogue_box_height*0.95 - button4_height
button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button4_x, button4_y, button4_width, button4_height),
                                      text='Générique !!!',
                                      manager=manager)


# Initialisation des variables
running = True
clock = pygame.time.Clock()
indice = 0
dialogue_box = True
bank = ["YOUPIIIIIIII !!!\n\nJ'AI RECUPERER MES MEMBRES !\n\nJe suis un génie !",
                "Je dois quand même te remercier, sans toi je serais\ntoujours dans les poubelle du casino.\n\nJe vais t'offrire un cadeau pour te remercier !",
                "Tiens, voici MON CHEF D'OEUVRE !\n\nJe te dédicace mon Disque\n\nTu écoute déjà surement '404 Not Found' !\n\n",]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    keys = pygame.key.get_pressed()
   

    # Draw the background
    screen.blit(background, background_rect)
    if indice == 0 :
        button2.show()
        button3.hide()
        button4.hide()
    
    if indice == 1:
        button2.hide()
        button3.show()
        button4.hide()

    if indice == 2:
        button2.hide()
        button3.hide()
        button4.show()


    if dialogue_box:
        pygame.draw.rect(screen, GRAY, (dialogue_box_x, 
                                        dialogue_box_y, 
                                        dialogue_box_width, 
                                        dialogue_box_height), 
                                        border_bottom_right_radius=20, 
                                        border_bottom_left_radius=20, 
                                        border_top_right_radius=20, 
                                        border_top_left_radius=20)
        
        manager.update(pygame.time.get_ticks() / 1000.0)
        manager.draw_ui(screen)


        
        text = bank[indice]
        rendered_text = pygame.font.Font(None, 24).render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))


        # Draw the text on the screen
        screen.blit(rendered_text, text_rect)

        #draw the character
        screen.blit(becile, (dialogue_box_x + dialogue_box_width*0.05, dialogue_box_y - 350))
        screen.blit(Joueur, (dialogue_box_x + dialogue_box_width*0.95 - button2_width, dialogue_box_y - 100))  
        if indice == 2 :
            screen.blit(disque, (dialogue_box_x + dialogue_box_width*0.95 - button2_width - 200, dialogue_box_y - 100))

        pygame.display.flip()
        
        # Check if the buttons are clicked
            
        if button2.check_pressed():
            indice += 1

        if button3.check_pressed():
            indice += 1
        
        if button4.check_pressed():
            
            chemin = os.path.abspath('../projet_info_Becile/Cinematique/script/Générique.py')
            subprocess.run(['python', chemin])
            pygame.quit()
            running = False
            
    clock.tick(60)

pygame.quit()