import pygame
import sys
from lib_jeu1_pygame import create_button, check_button_clicked

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Exemple de boutons avec images")

# Couleurs
white = (255, 255, 255)

# Propriétés des boutons
button1_rect = pygame.Rect(250, 200, 200, 50)  # Taille initiale, sera ajustée à celle de l'image
button1_text = ""  # Si image, ne pas mettre de texte
button1_image = "Button_img_pygame/Img_test/button_img_1_PNG.png"
button1_scale_factor = 0.5  # Facteur d'échelle pour le bouton 1

button2_rect = pygame.Rect(250, 300, 200, 50)
button2_text = "Bouton 2"
button2_image = ""  # Si texte, ne pas mettre le chemin/nom de l'image

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Vérifier si un bouton est cliqué
            if check_button_clicked(button1_rect, event):
                print("Bouton 1 cliqué !")
            elif check_button_clicked(button2_rect, event):
                print("Bouton 2 cliqué !")

        # Remplir l'écran avec une couleur de fond
        screen.fill(white)

        # Dessiner les boutons
        create_button(screen, button1_rect, text=button1_text, image_path=button1_image, scale_factor=button1_scale_factor)
        create_button(screen, button2_rect, text=button2_text, image_path=button2_image)

        # Mettre à jour l'affichage
        pygame.display.flip()

if __name__ == "__main__":
    main()