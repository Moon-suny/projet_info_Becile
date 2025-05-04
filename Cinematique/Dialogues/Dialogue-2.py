import pygame
import pygame_gui
import subprocess
import os
import time

def lancementJ2():
    print("Lancement du jeu 2")
    chemin = os.path.abspath('../projet_info_Becile/Jeu2/mainjeu2.py')
    subprocess.run(['python', chemin])



pygame.init()

# Set up the game window
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

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


#création du background
background = pygame.image.load("Cinematique/img/ruelle_sombre.jpg").convert_alpha()
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()

running = True
clock = pygame.time.Clock()
indice = 0
dialogue_box = True

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


        bank = ["HAAAAA j’ai plus de corps. Pourquoi ma jambe se trouve à 2 années lumière.\n\n                     VA CHERCHER LE RESTE MAINTENANT!!",
                "Ok je monte sur ton dos ! Puis je te guide.\n\n                     Je suis un génie !"]
        text = bank[indice]
        rendered_text = pygame.font.Font(None, 24).render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))

        screen.blit(rendered_text, text_rect)
    
        # Check if the buttons are clicked
        if button1.check_pressed():
            print("Button *frappe* clicked")
            indice = 0
            

        if button2.check_pressed():
            print("Button *hmm* clicked")
            indice = 1
            button2.hide()
            button1.hide()
            button3.show()

        if button3.check_pressed() and indice == 1:
            lancementJ2()
            time.sleep(1)
            running = False
            
            


        
        

    pygame.display.flip()
    clock.tick(60)

pygame.quit()