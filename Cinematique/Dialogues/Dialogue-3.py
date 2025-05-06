import pygame
import pygame_gui
import subprocess
import os
import time

def lancementJ3():
    #print("Lancement du jeu 3")
    chemin = os.path.abspath('../projet_info_Becile/Jeu3/Jeu3.py')
    subprocess.run(['python', chemin])

pygame.init()

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
becile = pygame.image.load("Cinematique/img/Tete_et_bras.png").convert_alpha()
becile = pygame.transform.scale(becile, (250, 250))
becile_rect = becile.get_rect()

# Création du joeur
Joueur = pygame.image.load("Cinematique/img/creature_jeu.png").convert_alpha()
Joueur = pygame.transform.scale(Joueur, (200, 100))
Joeur_rect = Joueur.get_rect()


# creation button
button1_width = 100
button1_height = 30
button1_x = dialogue_box_x + dialogue_box_width*0.95 - button1_width
button1_y = dialogue_box_y + dialogue_box_height*0.95 - button1_height
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button1_x, button1_y, button1_width, button1_height),
                                      text='*Pffffffff*',
                                      manager=manager)


running = True
clock = pygame.time.Clock()
dialogue_box = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    keys = pygame.key.get_pressed()
   

    # Draw the background
    screen.blit(background, background_rect)

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


        text = "Yes mes bras! ...\n\n\n\nNANNNN ON A LAISSER MES JAMBES AVEC CE FOU !\n\n On y retourne !"
        rendered_text = pygame.font.Font(None, 24).render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))

        if button1.check_pressed():
            pygame.quit()
            lancementJ3()
            running = False
            

        # Draw the character
        screen.blit(becile, (dialogue_box_x + dialogue_box_width*0.05, dialogue_box_y - 250))
        screen.blit(Joueur, (dialogue_box_x + dialogue_box_width*0.95 - 200, dialogue_box_y - 100))  

        screen.blit(rendered_text, text_rect)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()