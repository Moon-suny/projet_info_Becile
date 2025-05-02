import pygame
import pygame_gui
import subprocess
import os
import time

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
background = pygame.image.load("Cinematique/img/ruelle_sombre.jpg").convert_alpha()
background = pygame.transform.scale(background, (screen_width, screen_height))
background_rect = background.get_rect()


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


        text = "NANNNN ON A LAISSER MES BRAS AVEC CE FOU !\n\n On y retourne !"
        rendered_text = pygame.font.Font(None, 24).render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                   dialogue_box_y + dialogue_box_height // 2))

        screen.blit(rendered_text, text_rect)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()