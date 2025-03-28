import pygame

# Couleurs par défaut
DEFAULT_BUTTON_COLOR = (200, 200, 200)
DEFAULT_TEXT_COLOR = (0, 0, 0)

# le texte en orange permet de voir des caracteristiques de la fonction lorsque l'on reste dessus dans le fichier d'appel 

################################################################################
#                       Fonction de création de boutons
################################################################################

def create_button(
        screen,
        rect,
        button_color=DEFAULT_BUTTON_COLOR,
        text="",
        font=None,
        image_path=None,
        scale_factor=1.0
        ):
    
    """
    Crée et dessine un bouton sur l'écran. Peut utiliser une image comme bouton.

    :param screen: Surface Pygame sur laquelle dessiner le bouton.
    :param rect: Rectangle définissant la position initiale et la taille du bouton.
    :param button_color: Couleur du bouton (utilisée si aucune image n'est fournie).
    :param text: Texte à afficher sur le bouton.
    :param font: Police de texte à utiliser. Si None, utilise la police par défaut.
    :param image_path: Chemin de l'image à utiliser comme bouton.
    :param scale_factor: Facteur d'échelle pour redimensionner l'image et le rectangle du bouton.
    """

    if image_path:

        # Charger l'image
        image = pygame.image.load(image_path)

        # Obtenir la taille de l'image
        image_rect = image.get_rect()

        # Mettre à jour la taille du rectangle pour correspondre à celle de l'image, en appliquant le facteur d'échelle
        rect.width, rect.height = int(image_rect.width * scale_factor), int(image_rect.height * scale_factor)

        # Redimensionner l'image
        image = pygame.transform.scale(image, (rect.width, rect.height))

        # Dessiner l'image
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

################################################################################
#               Fonction de vérification des clics sur les boutons
################################################################################

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

################################################################################
#      Fonctions de gestion des événements et de vérification des réponses
################################################################################

def check_response(first_button, second_button, response_list):
    """
    Vérifie si les boutons cliqués correspondent à la réponse correcte.

    :param first_button: Nom ou identifiant du premier bouton cliqué.
    :param second_button: Nom ou identifiant du deuxième bouton cliqué.
    :param response_list: Liste des réponses correctes.
    :return: True si la réponse est correcte, sinon False.
    """
   
    try:
        # Essayer de convertir le premier bouton en index
        i = int(first_button) - 1
        if response_list[i] == second_button:
            print("Réponse correcte !")
            return True
        
    except (ValueError, IndexError):
        # Si le premier bouton n'est pas un nombre, essayer avec le deuxième bouton
        try:
            i = int(second_button) - 1
            if response_list[i] == first_button:
                print("Réponse correcte !")
                return True
            
        except (ValueError, IndexError):
            pass

    print("Réponse incorrecte !")
    return False