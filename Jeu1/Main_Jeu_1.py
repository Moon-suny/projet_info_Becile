import pygame
import sys
from lib_jeu1_pygame import create_button, check_button_clicked

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jeu 1")

# Initialisation image de fond
fond = pygame.image.load("Jeu1/Fond_Screen/Fond_screen_cable_jeu_1.png")
fond = pygame.transform.scale(fond, (window_size))
fond = fond.convert()

# Couleurs
white = (255, 255, 255)

# Propriétés des boutons
button1_rect = pygame.Rect(530, 520, 200, 50)  # Taille initiale, sera ajustée à celle de l'image
button1_text = ""  # Si image, ne pas mettre de texte
button1_image = "Jeu1/Img_Button/Logo_Cable_D/A.png"
button1_scale_factor = 0.1  # Facteur d'échelle pour le bouton 1

def main():
    while True:
        for event in pygame.event.get():
            # Vérifier si la croix est cliqué pour fermer la fenêtre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Vérifier si un bouton est cliqué
            if check_button_clicked(button1_rect, event):
                print("Bouton 1 cliqué !")

        # Remplir l'écran avec une couleur de fond
        screen.blit(fond, (0, 0))

        # Dessiner les boutons
        create_button(screen, button1_rect, text=button1_text, image_path=button1_image, scale_factor=button1_scale_factor)

        # Mettre à jour l'affichage
        pygame.display.flip()


if __name__ == "__main__":
    main()