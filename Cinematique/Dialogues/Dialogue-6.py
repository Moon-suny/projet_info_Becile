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



# Création buton suivant
button2_width = 200
button2_height = 30
button2_x = dialogue_box_x + dialogue_box_width*0.95 - button2_width
button2_y = dialogue_box_y + dialogue_box_height*0.95 - button2_height
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button2_x, button2_y, button2_width, button2_height),
                                      text='*RAWWWWWWW*',
                                      manager=manager)

#création du background
background = pygame.image.load("Cinematique/img/intérieur-navire.png").convert_alpha()
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()

# Création du personnage
becile = pygame.image.load("../projet_info_Becile/Cinematique/img/Tete_et_bras.png").convert_alpha()
becile = pygame.transform.scale(becile, (150, 150))
becile_rect = becile.get_rect()

# Création du joeur
Joueur = pygame.image.load("../projet_info_Becile/Cinematique/img/creature_jeu.png").convert_alpha()
Joueur = pygame.transform.scale(Joueur, (200, 100))
Joeur_rect = Joueur.get_rect()


running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    posmouse = pygame.mouse.get_pos()
        #    print(posmouse)
   
   
        manager.process_events(event)

    keys = pygame.key.get_pressed()
    dialogue_box = True

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


        text = "NAN J'ai besoin de ses Jambe !\n\nOn abandonne pas !\n\nOn va les chercher !"
        rendered_text = pygame.font.Font(None, 24).render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))

        #Draw the character
        screen.blit(becile, (dialogue_box_x + dialogue_box_width*0.05 + 100, dialogue_box_y - 150))
        screen.blit(Joueur, (dialogue_box_x + dialogue_box_width*0.95 - 300, dialogue_box_y - 100))  

    screen.blit(rendered_text, text_rect)
    pygame.display.flip()
    # Check if the buttons are clicked
    if button2.check_pressed():
        pygame.quit()
        lancement()
        running = False

    clock.tick(60)

pygame.quit()



