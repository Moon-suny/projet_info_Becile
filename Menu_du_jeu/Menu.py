import sys
import os
import pygame
import tkinter

# Chemin vers le répertoire parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Jeu1")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Fch_Save")))

# Importer les modules nécessaires
from lib_jeu1_pygame import create_button, check_button_clicked, DEFAULT_BUTTON_COLOR # Importer les fonctions de gestion des boutons
from lib_save_jeu import * # Importer les fonctions de sauvegarde et de chargement de partie
from lib_interface_Tinker import sound_interface_tinker, save_interface_tinker # Importer les fonctions d'interface utilisateur

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Bécile contre attaque !")

# Chargement de l'image de fond
fond = pygame.image.load("Menu_du_jeu\Img_menu\Menu_principale_Becile_contre_attaque.png")
fond = pygame.transform.scale(fond, window_size)  # Redimensionner l'image de fond pour s'adapter à la fenêtre
fond = fond.convert()

# Couleurs
or_color = (234, 184, 41)


# Définition des boutons du menu
buttons = [
    {
        "name": "Nouvelle Partie",
        "rect": pygame.Rect(160, 320, 490, 40),
        "text": "Nouvelle Partie",
        "button_color": or_color,
    },
    {
        "name": "Charger Partie",
        "rect": pygame.Rect(160, 380, 490, 40),
        "text": "Charger Partie",
        "button_color": or_color,
    },
    {
        "name": "Options",
        "rect": pygame.Rect(280, 445, 240, 40),
        "text": "Options",
        "button_color": or_color,
    },
    {
        "name": "Quitter",
        "rect": pygame.Rect(280, 500, 240, 40),
        "text": "Quitter",
        "button_color": or_color,
    },
]

# Fonction principale du menu
def menu():
    while True:

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Vérifier si un bouton est cliqué
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if check_button_clicked(button["rect"], event):

                        if button["name"] == "Nouvelle Partie":
                            #print("Nouvelle Partie sélectionnée.")
                            save_interface_tinker()  # Appel de l'interface de sauvegarde

                        elif button["name"] == "Charger Partie":
                            #print("Charger Partie sélectionnée.")
                            save_interface_tinker()  # Appel de l'interface de sauvegarde

                        elif button["name"] == "Options":
                            #print("Options sélectionnées. (pas d'options pour l'instant)")
                            sound_interface_tinker()  # Appel de l'interface de son

                        elif button["name"] == "Quitter":
                            print("Bye bye !")
                            pygame.quit()
                            sys.exit()

        # Affichage de l'image de fond
        screen.blit(fond, (0, 0))

        # Dessiner les boutons
        for button in buttons:
            create_button(
                screen, 
                button["rect"], 
                text=button["text"], 
                button_color=button.get("button_color", DEFAULT_BUTTON_COLOR),
            )

        # Mettre à jour l'affichage
        pygame.display.flip()

# Lancer le menu si le script est exécuté directement
if __name__ == "__main__":
    menu()