# ============================================================
# LIBRAIRIE : Fonctions pour le mini-jeu 1 avec Pygame
# ============================================================
# Ce module contient des fonctions pour gérer les boutons,
# les événements, les réponses, la barre de progression,
# et le mélange des positions dans le mini-jeu 1.
# ============================================================

import pygame
import random

# ------------------------------------------------------------
# CONSTANTES
# ------------------------------------------------------------
DEFAULT_BUTTON_COLOR = (200, 200, 200)  # Couleur par défaut des boutons
DEFAULT_TEXT_COLOR = (0, 0, 0)          # Couleur par défaut du texte

# ------------------------------------------------------------
# FONCTIONS DE GESTION DES BOUTONS
# ------------------------------------------------------------

def create_button(
        screen,
        rect,
        button_color=DEFAULT_BUTTON_COLOR,
        text="",
        font=None,
        image_path=None,
        scale_factor=1.0,
        outline_color=None,
        is_clicked=False,
        outline_width=2,
        ):
    """
    Crée et dessine un bouton sur l'écran. Peut utiliser une image comme bouton.
    Dessine un contour si le bouton est cliqué.

    :param screen: Surface Pygame sur laquelle dessiner le bouton.
    :param rect: Rectangle définissant la position initiale et la taille du bouton.
    :param button_color: Couleur du bouton (utilisée si aucune image n'est fournie).
    :param text: Texte à afficher sur le bouton.
    :param font: Police de texte à utiliser. Si None, utilise la police par défaut.
    :param image_path: Chemin de l'image à utiliser comme bouton.
    :param scale_factor: Facteur d'échelle pour redimensionner l'image et le rectangle du bouton.
    :param outline_color: Couleur du contour à dessiner lorsque le bouton est cliqué.
    :param is_clicked: Indique si le bouton est cliqué.
    :param outline_width: Largeur du contour à dessiner lorsque le bouton est cliqué.
    """
    if image_path:
        # Charger et redimensionner l'image
        image = pygame.image.load(image_path)
        image_rect = image.get_rect()
        rect.width, rect.height = int(image_rect.width * scale_factor), int(image_rect.height * scale_factor)
        image = pygame.transform.scale(image, (rect.width, rect.height))
        screen.blit(image, rect.topleft)
    else:
        # Dessiner le rectangle du bouton
        pygame.draw.rect(screen, button_color, rect)

    # Dessiner le texte au centre du bouton
    if font is None:
        font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, DEFAULT_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    # Dessiner le contour si le bouton est cliqué
    if is_clicked and outline_color:
        pygame.draw.rect(screen, outline_color, rect, outline_width)

def check_button_clicked(rect, event):
    """
    Vérifie si le bouton a été cliqué.

    :param rect: Rectangle définissant la position et la taille du bouton.
    :param event: Événement Pygame à vérifier.
    :return: True si le bouton a été cliqué, sinon False.
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        return rect.collidepoint(event.pos)
    return False

# ------------------------------------------------------------
# FONCTIONS DE GESTION DES RÉPONSES
# ------------------------------------------------------------

def check_response(first_button, second_button, response_list):
    """
    Vérifie si les boutons cliqués correspondent à la réponse correcte.

    :param first_button: Nom ou identifiant du premier bouton cliqué.
    :param second_button: Nom ou identifiant du deuxième bouton cliqué.
    :param response_list: Liste des réponses correctes.
    :return: True si la réponse est correcte, sinon False.
    """
    try:
        i = int(first_button) - 1
        if response_list[i] == second_button:
            print("Réponse correcte !")
            return True
    except (ValueError, IndexError):
        try:
            i = int(second_button) - 1
            if response_list[i] == first_button:
                print("Réponse correcte !")
                return True
        except (ValueError, IndexError):
            pass

    print("Réponse incorrecte !")
    return False

# ------------------------------------------------------------
# FONCTIONS DE GESTION DE LA BARRE DE PROGRESSION
# ------------------------------------------------------------

def draw_progress_bar(
    screen, 
    current_progress, 
    total_progress, 
    x, 
    y, 
    width, 
    height, 
    color_1=(255, 0, 0), 
    color_2=(0, 255, 0), 
    completed_colors=((0, 255, 0), (255, 255, 0)), 
    message=None, 
    message_color=(255, 255, 255), 
    font=None
):
    """
    Dessine une barre de progression. Si elle est complétée, elle clignote entre deux couleurs
    et affiche un message verticalement superposé à la barre.

    :param screen: Surface Pygame sur laquelle dessiner la barre.
    :param current_progress: Progression actuelle (nombre de réponses correctes).
    :param total_progress: Progression totale (nombre total de réponses).
    :param x: Coordonnée x de la position de la barre.
    :param y: Coordonnée y de la position de la barre.
    :param width: Largeur de la barre.
    :param height: Hauteur totale de la barre.
    :param color_1: Couleur de la barre de fond (rouge).
    :param color_2: Couleur de la barre de remplissage (vert).
    :param completed_colors: Tuple de deux couleurs pour le clignotement lorsque la barre est complétée.
    :param message: Message à afficher verticalement superposé à la barre.
    :param message_color: Couleur du message.
    :param font: Police de texte à utiliser pour le message. Si None, utilise la police par défaut.
    """
    # Dessiner la barre de fond
    pygame.draw.rect(screen, color_1, (x, y, width, height))

    # Calculer la hauteur de la barre de progression
    hauteur_verte = height * current_progress / total_progress

    # Si la barre est complétée, clignoter entre deux couleurs
    if current_progress >= total_progress:
        # Alterner entre les deux couleurs en fonction du temps
        clignotement_color = completed_colors[int(pygame.time.get_ticks() / 500) % 2]
        pygame.draw.rect(screen, clignotement_color, (x, y, width, height))

        # Afficher le message superposé à la barre si défini
        if message:
            if font is None:
                font = pygame.font.SysFont(None, 36)
            text_surface = font.render(message, True, message_color)
            text_rect = text_surface.get_rect(center=(x + width * 2.65, y + height // 3))
            
            # Afficher le texte verticalement (rotation)
            rotated_text = pygame.transform.rotate(text_surface, 90)
            screen.blit(rotated_text, text_rect.topleft)

    else:
        # Dessiner la barre de progression normale
        pygame.draw.rect(screen, color_2, (x, y + height - hauteur_verte, width, hauteur_verte))

# ------------------------------------------------------------
# FONCTIONS DE MÉLANGE DES POSITIONS
# ------------------------------------------------------------

def shuffle_positions(positions):
    """
    Mélange les positions des chiffres et des lettres séparément.

    :param positions: Dictionnaire contenant les positions avec des clés comme 'pos_1', 'pos_2', ..., 'pos_A', 'pos_B', ...
    :return: Dictionnaire avec les positions mélangées.
    """
    number_positions = [positions[f"pos_{i}"] for i in range(1, 6)]
    letter_positions = [positions[f"pos_{letter}"] for letter in "ABCDE"]

    random.shuffle(number_positions)
    random.shuffle(letter_positions)

    shuffle_output_positions = {}
    number_keys = [f"pos_{i}" for i in range(1, 6)]
    for key, pos in zip(number_keys, number_positions):
        shuffle_output_positions[key] = pos

    for letter, pos in zip("ABCDE", letter_positions):
        shuffle_output_positions[f"pos_{letter}"] = pos

    return shuffle_output_positions

# ------------------------------------------------------------
# FONCTIONS D'ANIMATION
# ------------------------------------------------------------

def handle_cable_animation(
    screen, 
    connections, 
    first_button_center, 
    waiting_for_second_click, 
    cable_color=(0, 0, 255), 
    cable_width=3
):
    """
    Gère l'animation des câbles entre les boutons.

    :param screen: Surface Pygame sur laquelle dessiner.
    :param connections: Liste des connexions existantes entre les boutons.
    :param first_button_center: Centre du premier bouton cliqué.
    :param waiting_for_second_click: Booléen indiquant si on attend un deuxième clic.
    :param cable_color: Couleur du câble.
    :param cable_width: Largeur du câble.
    """
    # Dessiner toutes les connexions existantes
    for connection in connections:
        pygame.draw.line(screen, cable_color, connection[0], connection[1], cable_width)

    # Dessiner une ligne entre le premier bouton et la souris
    if waiting_for_second_click and first_button_center:
        mouse_pos = pygame.mouse.get_pos()  # Obtenir la position actuelle de la souris
        pygame.draw.line(screen, cable_color, first_button_center, mouse_pos, cable_width)  # Dessiner une ligne

# ============================================================
# FIN DU MODULE
# ============================================================