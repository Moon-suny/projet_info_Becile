import pygame
import threading

def play_music_in_parallel(screen, path_music):
    """
    Fonction pour jouer de la musique sur une fenêtre Pygame déjà ouverte.
    La fonction s'exécute en parallèle et s'arrête lorsque la musique est terminée.

    :param screen: Surface Pygame sur laquelle afficher.
    :param path_music: Chemin du fichier audio à jouer.
    """
    def music_thread():
        pygame.mixer.init()

        # Chargement du son
        try:
            pygame.mixer.music.load(path_music)
        except pygame.error as e:
            print(f"Erreur de chargement du son : {e}")
            return

        # Lecture de la musique
        pygame.mixer.music.play()

        # Attendre que la musique se termine
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Attendre un court instant pour éviter de bloquer

        # Libération des ressources
        pygame.mixer.music.unload()

    # Lancer la musique dans un thread séparé
    thread = threading.Thread(target=music_thread)
    thread.start()