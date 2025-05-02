import pygame
import pygame_gui
import os
import subprocess
import time as time

pygame.init()

def lancement():
    #print("Lancement du jeu 1")
    chemin = os.path.abspath('../projet_info_Becile/Jeu1/Main_Jeu_1.py')
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

# Création buton oui
button1_width = 100
button1_height = 30
button1_x = dialogue_box_x + dialogue_box_width*0.05
button1_y = dialogue_box_y + dialogue_box_height*0.95 - button1_height
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button1_x, button1_y, button1_width, button1_height),
                                      text='Oui',
                                      manager=manager)

# Création buton Non
button2_width = 100
button2_height = 30
button2_x = dialogue_box_x + dialogue_box_width*0.95 - button2_width
button2_y = dialogue_box_y + dialogue_box_height*0.95 - button2_height
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button2_x, button2_y, button2_width, button2_height),
                                      text='Non',
                                      manager=manager)

#création du background
background = pygame.image.load("Cinematique/img/ruelle_sombre.jpg").convert_alpha()
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()

# Création du personnage
becile = pygame.image.load("Cinematique/img/tete_robot_capute.png").convert_alpha()
becile = pygame.transform.scale(becile, (100, 100))
becile = pygame.transform.rotate(becile, 25)
becile.set_alpha(175)  # 0-255, 0 = transparent, 255 = opaque
becile_rect = becile.get_rect()

# Création du joeur
Joueur = pygame.image.load("Cinematique/img/creature_jeu.png").convert_alpha()
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


        text = "Veux tu aider Bécile ?"
        rendered_text = pygame.font.Font(None, 24).render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))

        screen.blit(rendered_text, text_rect)
    
        # Check if the buttons are clicked
        if button1.check_pressed():
            lancement()
            time.sleep(1)
            running = False
            
        if button2.check_pressed():
            pass

        # Draw the character
        screen.blit(becile, (609,418))
        screen.blit(Joueur, (dialogue_box_x + dialogue_box_width*0.95 - button2_width, dialogue_box_y - 100))    




    pygame.display.flip()
    clock.tick(60)

pygame.quit()