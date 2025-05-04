import sys
import pygame
import random
import os
import time as time
import subprocess
from lib_jeu1_pygame import create_button, check_button_clicked, check_response, draw_progress_bar, shuffle_positions, handle_cable_animation, DEFAULT_BUTTON_COLOR

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Répare le cerveau !")

# Initialisation image de fond
fond = pygame.image.load("Jeu1/Fond_Screen/Fond_screen_cable_jeu_1.png")
fond = pygame.transform.scale(fond, (window_size))
fond = fond.convert()

# Couleur
vert = (0, 255, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
blanc = (255, 255, 255)

# Dictionnaire initial des positions
positions = {
    "pos_1": (190, 20, 0, 0),
    "pos_2": (190, 145, 0, 0),
    "pos_3": (190, 270, 0, 0),
    "pos_4": (190, 395, 0, 0),
    "pos_5": (190, 520, 0, 0),
    "pos_A": (530, 20, 0, 0),
    "pos_B": (530, 145, 0, 0),
    "pos_C": (530, 270, 0, 0),
    "pos_D": (530, 395, 0, 0),
    "pos_E": (530, 520, 0, 0)
}

# Mélanger les positions
shuffle_output_positions = shuffle_positions(positions)

# Liste des boutons avec leurs propriétés
buttons = [
    {   # Bouton 1
        "name" : "1",
        "rect": pygame.Rect(shuffle_output_positions["pos_1"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_G/1.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton 2
        "name" : "2",
        "rect": pygame.Rect(shuffle_output_positions["pos_2"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_G/2.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton 3
        "name" : "3",
        "rect": pygame.Rect(shuffle_output_positions["pos_3"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_G/3.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton 4
        "name" : "4",
        "rect": pygame.Rect(shuffle_output_positions["pos_4"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_G/4.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton 5
        "name" : "5",
        "rect": pygame.Rect(shuffle_output_positions["pos_5"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_G/5.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton A
        "name" : "A",
        "rect": pygame.Rect(shuffle_output_positions["pos_A"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_D/A.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton B
        "name" : "B",
        "rect": pygame.Rect(shuffle_output_positions["pos_B"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_D/B.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton C
        "name" : "C",
        "rect": pygame.Rect(shuffle_output_positions["pos_C"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_D/C.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton D
        "name" : "D",
        "rect": pygame.Rect(shuffle_output_positions["pos_D"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_D/D.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
    {   # Bouton E
        "name" : "E",
        "rect": pygame.Rect(shuffle_output_positions["pos_E"]),  # Taille initiale, sera ajustée à celle de l'image
        "text": "",  # Texte (vide si image)
        "image_path": "Jeu1/Img_Button/Logo_Cable_D/E.png", # Chemin/nom de l'image (vide si texte)
        "scale_factor": 0.1,  # Facteur d'échelle pour le bouton 1
        "outline_color": bleu,  # Couleur du contour
        "is_clicked": False,  # Indique si le bouton est cliqué
        "outline_width": 2,  # Largeur du contour
    },
]

# variables de stockage des boutons cliqués
First_button_use = None
Second_button_use = None

# liste de validation des reponses
Liste_reponse = ["A", "B", "C", "D", "E"]
random.shuffle(Liste_reponse) # Mélanger la liste de réponses pour le jeu

# variables de stockage des réponses
Rep_give = set()

# Liste pour stocker les connexions entre les boutons
connections = []

# fonction principale
def main():
    global First_button_use, Second_button_use
    waiting_for_second_click = False
    first_button_center = None  # Stocke le centre du premier bouton cliqué

    # Boucle principale du jeu
    while True:

        # Gestion des événements
        for event in pygame.event.get():

            # Vérifier si la croix est cliquée pour fermer la fenêtre
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Vérifier si un bouton est cliqué
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:

                    # Vérifier si le bouton a été cliqué
                    if check_button_clicked(button["rect"], event):
                        button["is_clicked"] = True  # Mettre à jour l'état du bouton cliqué

                        if not waiting_for_second_click:
                            # Premier clic détecté
                            First_button_use = button["name"]
                            first_button_center = button["rect"].center  # Stocker le centre du premier bouton
                            print("Premier bouton cliqué :", First_button_use)
                            waiting_for_second_click = True

                        else:
                            # Deuxième clic détecté
                            Second_button_use = button["name"]
                            second_button_center = button["rect"].center  # Stocker le centre du deuxième bouton
                            print("Deuxième bouton cliqué :", Second_button_use)

                            # Vérifier si les boutons cliqués correspondent à la réponse
                            if check_response(First_button_use, Second_button_use, Liste_reponse) is True:
                                # Vérifier si la réponse n'a pas déjà été donnée
                                if ((First_button_use + Second_button_use) and (Second_button_use + First_button_use)) not in Rep_give:
                                    Rep_give.add(First_button_use + Second_button_use)
                                    # Ajouter la connexion entre les deux boutons uniquement si la réponse est correcte
                                    connections.append((first_button_center, second_button_center))
                            else:
                                # Réinitialiser l'état des boutons cliqués si la réponse est incorrecte
                                for button in buttons:
                                    if button["name"] == First_button_use or button["name"] == Second_button_use:
                                        button["is_clicked"] = False

                            # Réinitialiser les boutons pour un nouveau tour
                            First_button_use = None
                            Second_button_use = None
                            first_button_center = None  # Réinitialiser le centre du premier bouton
                            waiting_for_second_click = False

        # Remplir l'écran avec une couleur de fond
        screen.blit(fond, (0, 0))

        # Dessiner les boutons
        for button in buttons:
            create_button(
                screen, button["rect"],
                text=button["text"],
                image_path=button["image_path"],
                scale_factor=button["scale_factor"],
                font=button.get("font"),
                button_color=button.get("button_color", DEFAULT_BUTTON_COLOR),
                outline_color=button.get("outline_color"),
                is_clicked=button.get("is_clicked"),
                outline_width=button.get("outline_width")
            )

        # Dessiner toutes les connexions existantes
        for connection in connections:
            pygame.draw.line(screen, bleu, connection[0], connection[1], 3)

        # Gérer l'animation des câbles
        handle_cable_animation(
            screen=screen,
            connections=connections,
            first_button_center=first_button_center,
            waiting_for_second_click=waiting_for_second_click,
            cable_color=bleu,
            cable_width=3
        )

        # Calcul et dessiner la barre de progression
        draw_progress_bar(
            screen,
            current_progress=len(Rep_give),
            total_progress=len(Liste_reponse),
            x=380,
            y=50,
            width=40,
            height=500,
            color_1=rouge,
            color_2=vert,
            completed_colors=(rouge, vert),
            message="Cerveau réparer !",
            message_color=blanc
        )

        # Mettre à jour l'affichage
        pygame.display.flip()

        if len(Rep_give) == len(Liste_reponse):
            time.sleep(12)
            print("je suis passer par ici")
            pygame.quit()
            # Lancer le script Dialogue-2.py
            chemin = os.path.abspath('Cinematique\Dialogues\Dialogue-2.py')
            subprocess.run(['python', chemin])


if __name__ == "__main__":
    main()