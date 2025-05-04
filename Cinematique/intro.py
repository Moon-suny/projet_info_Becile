import pygame
import pygame_gui
import os
import subprocess
import time as time
import cv2

chemin_video = os.path.abspath('../projet_info_Becile/Cinematique/vidéo/star_wars.mp4')

video = cv2.VideoCapture(chemin_video)

if not video.isOpened():
    print("Erreur lors de l'ouverture de la vidéo")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        break  # Fin de la vidéo
    
    # Affiche image par image
    cv2.imshow("Lecture vidéo", frame)

    # Quitter si touche 'q' est pressée
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()