import pygame
import random
import os

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()

# Fenêtre
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bécile Contre-Attaque - Générique de fin")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Chargement d'une police lisible et marrante
try:
    font = pygame.font.SysFont("Comic Sans MS", 32)
except:
    font = pygame.font.SysFont("Arial", 32)

# Son (boucle de tuyau métallique)
# Remplacer "tuyau.mp3" par le vrai fichier si nécessaire
if os.path.exists("../projet_info_Becile/Cinematique/music/404_NOT_FOUND.mp3"):
    pygame.mixer.music.load("../projet_info_Becile/Cinematique/music/404_NOT_FOUND.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # boucle infinie

# Texte du générique
credits_text = [
    "UN JEU FAIT AVEC AMOUR, PIXELS, ET UN PEU DE MALADRESSE PAR :",
    "MAXIME, PIERRE-ÉLOI ET CLÉMENT",
    "(qui ne savaient pas dans quoi ils s’embarquaient)",
    "",
    "REMERCIEMENTS SPÉCIAUX :",
    "- Le robot de Futurama, dont on a tout pompé sauf la voix",
    "- Le Mosstomper de LoL, qu’on a remplacé par un nain sans pouvoir",
    "- Les tuyaux de Mario, qui résonnent maintenant dans nos cauchemars",
    "- Les sabres lasers volés à Star Wars (merci George, on te les rend pas)",
    "- Jack Sparrow, qui aurait probablement poursuivi Bécile pour plagiat",
    "- La physique douteuse de Jetpack Joyride",
    "- Les câbles d’Among Us (sérieusement, pourquoi c’est si dur ?)",
    "",
    "",
    "UN HOMMAGE À :",
    "- TOUS LES JOUEURS QUI ONT ESSAYÉ DE COMPRENDRE L’HISTOIRE",
    "(désolé pour les 14 niveaux de flashback inutiles)",
    "- CEUX QUI ONT TROUVÉ LE NIVEAU CACHÉ EN TOMBANT PAR ERREUR",
    "- LES TESTEURS QUI ONT SIGNALÉ DES BUGS… IGNORÉS AVEC AMOUR",
    "",
    "BUG SYSTEM DETECTED...",
    "> Tentative de chargement du DLC “Bécile à la plage” échouée.",
    "> Erreur 404 : palmiers non trouvés.",
    "> Reboot dans 3… 2… *1.5*... *banane*",
    "",
    "\"Par les créateurs de Bécile Contre-Attaque, découvrez bientôt :",
    " Bécile 2 : La Revanche du Bug",
    " Bécile Kart Deluxe Moisi",
    " Super Bécile Maker : Crée ton propre désastre\"",
    "",
    "Bécile vous remercie.",
    "(Enfin… il vous observe. C’est déjà pas mal.)",
    "",
    "© 2025 - Nintendo n’a pas validé ce projet, mais on espère qu’ils riront quand même.",
    "",
    "CRÉÉ AVEC :",
    " Une touche d’humour",
    " Trois litres de café",
    " Un moteur de jeu instable",
    " Et un PowerPoint converti en PNG",
    "",
    "C’EST FINI.",
    "VOUS POUVEZ DÉSINSTALLER.",
    "OU RECOMMENCER.",
    "(Mais pourquoi feriez-vous ça ?)",
    "***FIN***"
]

# Création de la surface de texte
line_spacing = 75
def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

text_surfaces = []
margin = 80
for i, line in enumerate(credits_text):
    color = YELLOW if "***" in line or "BUG" in line else WHITE
    wrapped_lines = wrap_text(line, font, WIDTH - 2 * margin)
    for j, wrapped in enumerate(wrapped_lines):
        surface = font.render(wrapped, True, color)
        # Centrage horizontal
        pos_x = WIDTH // 2 - surface.get_width() // 2
        text_surfaces.append((surface, pos_x))


text_height = len(text_surfaces) * line_spacing
scroll_y = HEIGHT

# Boucle principale
running = True
clock = pygame.time.Clock()
bug_flash_timer = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

    # Effet bug flash aléatoire
    if random.randint(0, 300) == 1:
        bug_flash_timer = 5

    if bug_flash_timer > 0:
        screen.fill(WHITE)
        bug_flash_timer -= 1

    for i, (surface, pos_x) in enumerate(text_surfaces):
        y = scroll_y + i * line_spacing
        screen.blit(surface, (pos_x, y))

    scroll_y -= 1.5 #vitee de défilement

    if scroll_y + text_height < 0:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
