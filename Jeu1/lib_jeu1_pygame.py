import pygame

# Couleurs par défaut
DEFAULT_BUTTON_COLOR = (200, 200, 200)
DEFAULT_TEXT_COLOR = (0, 0, 0)

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