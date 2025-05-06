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
button2_width = 150
button2_height = 30
button2_x = dialogue_box_x + dialogue_box_width*0.95 - button2_width
button2_y = dialogue_box_y + dialogue_box_height*0.95 - button2_height
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button2_x, button2_y, button2_width, button2_height),
                                      text='Ce réjouire !',
                                      manager=manager)

#création du background
background = pygame.image.load("Cinematique/img/intérieur-navire.png").convert_alpha()
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()

# Création du personnage
becile = pygame.image.load("../projet_info_Becile/Cinematique/img/le_nain_becile.png").convert_alpha()
becile = pygame.transform.scale(becile, (400, 400))
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


        text = "Let's GO on a réussi !\n\nJe suis le meilleur !\n\nJE SUIS ENTIER"
        rendered_text = pygame.font.Font(None, 24).render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))

        #Draw the character
        screen.blit(becile, (dialogue_box_x + dialogue_box_width*0.05 + 100, dialogue_box_y - 325))
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





'''A fusionner'''




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

# Création button
button1_width = 120
button1_height = 30
button1_x = dialogue_box_x + dialogue_box_width*0.05
button1_y = dialogue_box_y + dialogue_box_height*0.95 - button1_height
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button1_x, button1_y, button1_width, button1_height),
                                      text='*taper sa tête*',
                                      manager=manager)

# Création button
button2_width = 100
button2_height = 30
button2_x = dialogue_box_x + dialogue_box_width*0.95 - button2_width
button2_y = dialogue_box_y + dialogue_box_height*0.95 - button2_height
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button2_x, button2_y, button2_width, button2_height),
                                      text='*hmmmmm*',
                                      manager=manager)

# Création button
button3_width = 100
button3_height = 30
button3_x = dialogue_box_x + dialogue_box_width*0.95 - button3_width
button3_y = dialogue_box_y + dialogue_box_height*0.95 - button3_height
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button3_x, button3_y, button3_width, button3_height),
                                      text='Suivant',
                                      manager=manager)


# Initialisation des variables
running = True
clock = pygame.time.Clock()
indice = 0
dialogue_box = True
repetition = 0
bank = ["HAAAAA j’ai plus de corps. Pourquoi ma jambe se trouve à 2 années lumière.\n\nVA CHERCHER LE RESTE MAINTENANT!!",
                "Ok je monte sur ton dos ! Puis je te guide.\n\nJe suis un génie ! \n\nMais attention le voleur fétichiste nous lance des choses ! EVITE LES !",
                "Aïe, VA CHERCHER MES MEMBRES !!!"]
voyage = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    keys = pygame.key.get_pressed()
   

    # Draw the background
    screen.blit(background, background_rect)
    if indice == 0 :
        button3.hide()
        button1.show()
        button2.show()
    
    if indice == 1:
        if voyage == False:
            apparition_vaiseau()
            voyage = True
        button1.hide()
        button2.hide()
        button3.show()

    if indice == 2:
        button1.hide()
        button2.hide()
        button3.show()

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

        screen.blit(rendered_text, text_rect)
    
        # Check if the buttons are clicked
        if button1.check_pressed():
            #print("Button *frappe* clicked")
            indice = 2
            

        if button2.check_pressed():
            #print("Button *hmm* clicked")
            indice = 1
            button2.hide()
            button1.hide()
            button3.show()

        if button3.check_pressed():
            if indice == 1:
                pygame.quit()
                lancementJ2()
                running = False

            if indice == 2:
                repetition += 1
                if repetition == 42: #easter Egg
                    bank[0] = "Va chercher mes membres ! S'il te plaît ! \n\n Mon dieu de l'univers j'ai besoin de ton aide !"
                else:
                    bank[0] = "Va chercher mes membres !"
                indice = 0
        
            
        #draw the character
        screen.blit(becile, (dialogue_box_x + dialogue_box_width*0.05, dialogue_box_y - 100))
        screen.blit(Joueur, (dialogue_box_x + dialogue_box_width*0.95 - button2_width, dialogue_box_y - 100))  


        
        

    pygame.display.flip()
    clock.tick(60)

pygame.quit()