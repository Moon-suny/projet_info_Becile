import pygame
import cv2
import os
import subprocess
import threading
from pygame import mixer

# Initialisation de Pygame pour le son
pygame.init()
mixer.init()

# === Chemins ===
chemin_video = os.path.abspath('../projet_info_Becile/Cinematique/vidéo/blackpearl.mp4')
chemin_audio = os.path.abspath('C:../projet_info_Becile/Cinematique/music/Trompette.mp3')


# === Lancement de l'audio en fond ===
def jouer_audio():
    mixer.music.load(chemin_audio)
    mixer.music.play()

# === Lecture de la vidéo OpenCV (image uniquement) ===
def lire_video():
    video = cv2.VideoCapture(chemin_video)
    if not video.isOpened():
        print("Erreur lors de l'ouverture de la vidéo")
        return

    # Redimensionner la vidéo à une taille plus petite
    width, height = 800, 600

    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.resize(frame, (width, height))
        cv2.imshow("Cinématique", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

# === Exécution ===
# Lancer le son en parallèle
audio_thread = threading.Thread(target=jouer_audio)
audio_thread.start()

# Lire la vidéo
lire_video()
mixer.music.stop()
