import pygame
from lib_music_pygame import play_music_in_parallel

# Initialisation de Pygame
pygame.init()

# Création de l'écran
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini-jeu avec musique")

# Lancer la musique en parallèle
play_music_in_parallel(screen, "Music\legends_never_die.mp3")

# Boucle principale du mini-jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Exemple : Dessiner un cercle qui suit la souris
    screen.fill((0, 0, 0))  # Remplir l'écran en noir
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 20)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()