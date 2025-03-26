import pygame
from pygame.locals import *
 
#Initialisation de la bibliothèque Pygame
pygame.init()

screen_width = 1000
Screen_heigt = 800

screen = pygame.display.set_mode((screen_width, Screen_heigt))
pygame.display.set_caption('')


#Chargement des image
barre_img = pygame.image.load('img/barre.png')
Background_img = pygame.image.load('img/Backgrnd.png')


#boucle de jeu
while True:

    screen.blit(Background_img, (0,0))
    screen.blit(barre_img, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
 

    pygame.display.update()