import pygame
from pygame.locals import *
 
def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((300, 50))
    pygame.display.set_caption('Programme Pygame de base')
 
    # Remplissage de l'arrière-plan
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
 
    # Affichage d'un texte
    font = pygame.font.Font(None, 36)
    text = font.render("Salut tout le monde", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)
 
    # Afficher le tout dans la fenêtre
    screen.blit(background, (0, 0))
    pygame.display.flip()
 
    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
 
        screen.blit(background, (0, 0))
        pygame.display.flip()
 
if __name__ == '__main__': main()