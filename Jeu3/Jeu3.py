import pygame
import random
import os
import subprocess
import threading
from pygame import mixer
from pygame.locals import *

# === Lancement de l'audio en fond ===
def jouer_audio():
    mixer.music.load(os.path.abspath('Jeu3\Eiffel 65 - Blue (Flume Remix) - Official Visualiser.mp3'))
    mixer.music.play()

def lancement_suite():
    #print("Lancement du Dialogue 5")
    chemin = os.path.abspath('../projet_info_Becile/Cinematique/Dialogues/Dialogue-5.py')
    subprocess.run(['python', chemin])

def lancement_relance():
    #print("Lancement du Dialogue 6")
    chemin = os.path.abspath('../projet_info_Becile/Cinematique/Dialogues/Dialogue-6.py')
    subprocess.run(['python', chemin])

pygame.init()

audio_thread = threading.Thread(target=jouer_audio)
audio_thread.start()

W, H = 1000, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Jeu 3')

#--musique--


PLAYER_SPEED = 4.5
GRAVITY = 0.75
JUMP_STRENGTH = -18
SOL_HEIGHT = 50

# --- Chargement des images ---
try:
    player_surf_orig = pygame.image.load(r"../projet_info_Becile/Cinematique/img/creature_jeu.png").convert_alpha()
    barre_surf = pygame.image.load('Jeu3/img/barre.png').convert_alpha()
    bg_surf = pygame.image.load('Jeu3/img/Backgrnd.png').convert()
    obj_surf_orig = pygame.image.load(r"../projet_info_Becile/Cinematique/img/jambe_du_robot.png").convert_alpha()
    mechant_surf_orig = pygame.image.load(r"../projet_info_Becile/Cinematique/img/scientifique_fou.png").convert_alpha()
    poubelle_orig = pygame.transform.scale(pygame.image.load(r"../projet_info_Becile/Jeu2/img/poubelle.png").convert_alpha(), (40, 40))
except pygame.error as e:
    print(f"Erreur de chargement d'image: {e}")
    pygame.quit()
    exit()

# --- Joueur ---
player_w, player_h = 50, 25
player_img_scaled = pygame.transform.scale(player_surf_orig, (player_w, player_h))
player_img_left = player_img_scaled
player_img_right  = pygame.transform.flip(player_img_scaled, True, False)
player_surf = player_img_right
player_rect = player_surf.get_rect(x=946, y=703)
player_mask = pygame.mask.from_surface(player_surf)
vy = 0 # Vitesse verticale du joueur
on_ground = False
facing_right = True

# --- Éléments du décor ---
obj_surf = pygame.transform.scale(obj_surf_orig, (75, 75))
obj_rect = obj_surf.get_rect(topleft=(30, 100))

mechant_surf = pygame.transform.scale(mechant_surf_orig, (120, 120))
mechant_rect = mechant_surf.get_rect(topleft=(113, 60))

barre_rect = barre_surf.get_rect(topleft=(0, 0))
barre_mask = pygame.mask.from_surface(barre_surf)

sol_rect = pygame.Rect(0, H - SOL_HEIGHT, W, SOL_HEIGHT)
sol_surf = pygame.Surface((W, SOL_HEIGHT))
sol_surf.fill((100, 100, 100))
sol_surf.set_alpha(100) 
sol_mask = pygame.mask.from_surface(sol_surf)

# --- Liste de chemins pour les poubelles ---
trajectoire_principale = [(204, 105), (202, 165), (600, 200), (615, 370), (450, 370),(450, 381), (430, 546), (586, 561), (597, 734), (994, 739)]

trajectoire_alternative = [(204, 105), (202, 165), (600, 200), (615, 370), (450, 370), (450, 381), (430, 546), (282, 530), (270, 734), (994, 739)]

trajectoire_alternative2 = [(204, 105), (194,523), (282,530), (270, 734), (994, 739)]

trajectoire_alternative3 = [(204, 105), (202, 165), (600, 200), (1000, 343) ]


defined_paths = [
    trajectoire_principale,
    trajectoire_alternative,
    trajectoire_alternative2,
    trajectoire_alternative3 # Décommenter pour avoir plusieurs types de chemins
]

# --- Poubelles ---
poubelles = []
last_spawn_time = 0
poubelle_spawn_interval = 0
poubelle_rotation_delay = 0.2
poubelle_vitesse = 4.5

clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000

    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
            mixer.music.stop()
        #if e.type == MOUSEBUTTONDOWN:
        #    print("Clic souris en", e.pos)

    # --- Contrôles Joueur ---
    keys = pygame.key.get_pressed()
    player_dx = 0
    if keys[K_LEFT]:
        player_dx = -PLAYER_SPEED
        facing_right = False
    if keys[K_RIGHT]:
        player_dx = PLAYER_SPEED
        facing_right = True
    if keys[K_UP] and on_ground:
        vy = JUMP_STRENGTH
        on_ground = False
    
    if facing_right:
        player_surf = player_img_right
    elif not facing_right:
        player_surf = player_img_left
    player_mask = pygame.mask.from_surface(player_surf)

    # --- Physique Joueur ---
    vy += GRAVITY
    if vy > 10: vy = 10
    on_ground = False # Réinitialiser avant les tests de collision verticale

    # Déplacement horizontal et collision
    player_rect.x += player_dx
    offset_h = (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)
    overlap_h = player_mask.overlap(barre_mask, offset_h)
    if overlap_h:
        y_mask_collision = overlap_h[1]
        cutoff_collision = int(player_h * 0.75)
        if y_mask_collision < cutoff_collision:
            player_rect.x -= player_dx 

    # Déplacement vertical et collision
    player_rect.y += int(vy)
    offset_v_barre = (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)
    overlap_v_barre = player_mask.overlap(barre_mask, offset_v_barre)
    if overlap_v_barre: # Collision avec une barre
        if vy > 0: # Tombe sur la barre
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.y -= 1
            vy = 0
            on_ground = True
        elif vy < 0: # Heurte la barre par le dessous
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.y += 1
            vy = 0
    else: # Pas de collision avec une barre, vérifier le sol
        offset_v_sol = (sol_rect.x - player_rect.x, sol_rect.y - player_rect.y)
        if player_mask.overlap(sol_mask, offset_v_sol) and vy >= 0: # Tombe sur le sol
            while player_mask.overlap(sol_mask, (sol_rect.x - player_rect.x, sol_rect.y - player_rect.y)):
                player_rect.y -= 1
            vy = 0
            on_ground = True

    # --- Spawning Poubelles ---
    last_spawn_time += dt
    if last_spawn_time > poubelle_spawn_interval:
        if not defined_paths:
            print("Attention: Aucun chemin n'est défini pour les poubelles !")
        else:
            chosen_path_points = random.choice(defined_paths)
            if not chosen_path_points:
                print("Attention: Un chemin vide a été choisi pour une poubelle !")
            else:
                start_x, start_y = chosen_path_points[0]
                poubelles.append({
                    "x": start_x, "y": start_y,
                    "angle": 0,
                    "surf": poubelle_orig.copy(),
                    "rotation_timer": 0,
                    "path_points": chosen_path_points,
                    "current_target_idx": 0 
                })
        last_spawn_time = 0
        poubelle_spawn_interval = random.uniform(0.9, 1.5)

    # --- Mise à jour des Poubelles ---
    for p in poubelles[:]:
        p["rotation_timer"] += dt
        if p["rotation_timer"] > poubelle_rotation_delay:
            p["angle"] = (p["angle"] + 90) % 360
            p["surf"] = pygame.transform.rotate(poubelle_orig, p["angle"])
            p["rotation_timer"] = 0

        assigned_path = p["path_points"]
        current_idx = p["current_target_idx"]

        if current_idx + 1 < len(assigned_path):
            current_pos_x, current_pos_y = p["x"], p["y"]
            target_pos_x, target_pos_y = assigned_path[current_idx + 1]
            
            vec_dx = target_pos_x - current_pos_x
            vec_dy = target_pos_y - current_pos_y
            dist = (vec_dx**2 + vec_dy**2)**0.5

            if dist == 0: # Déjà à la cible ou point dupliqué
                p["current_target_idx"] += 1
            elif dist < poubelle_vitesse:
                p["x"], p["y"] = target_pos_x, target_pos_y
                p["current_target_idx"] += 1
            else:
                p["x"] += poubelle_vitesse * vec_dx / dist
                p["y"] += poubelle_vitesse * vec_dy / dist
        else:
            p["x"] += poubelle_vitesse # Fin du chemin, continue à droite

        # Collision poubelle avec joueur
        poubelle_rect_coll = p["surf"].get_rect(center=(p["x"], p["y"]))
        poubelle_mask_coll = pygame.mask.from_surface(p["surf"])
        offset_collision = (int(poubelle_rect_coll.x - player_rect.x), int(poubelle_rect_coll.y - player_rect.y))
        if player_mask.overlap(poubelle_mask_coll, offset_collision):
            pygame.quit()
            lancement_relance()
            running = False
            mixer.music.stop()
            break

        # Suppression des poubelles hors écran
        if p["y"] > H + p["surf"].get_height() or \
           p["x"] > W + p["surf"].get_width() or \
           p["x"] < -p["surf"].get_width():
            poubelles.remove(p)
            
    if not running: # Si une condition de fin de jeu a été rencontrée plus tôt
        break


    

    # --- Limites écran Joueur ---
    if player_rect.left < 0: player_rect.left = 0
    if player_rect.right > W: player_rect.right = W
    if player_rect.top > H :
        pygame.quit()
        lancement_relance()
        running = False
        mixer.music.stop()


    # --- Affichage ---
    screen.blit(bg_surf, (0, 0))
    screen.blit(barre_surf, barre_rect)
    screen.blit(sol_surf, sol_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(obj_surf, obj_rect)
    screen.blit(mechant_surf, mechant_rect)

    for p in poubelles:
        draw_x = p["x"] - p["surf"].get_width() // 2
        draw_y = p["y"] - p["surf"].get_height() // 2
        screen.blit(p["surf"], (draw_x, draw_y))

    pygame.display.flip()

    # --- Objectif ---
    if player_rect.colliderect(obj_rect):
        pygame.quit()
        lancement_suite() # Lancer le dialogue 5
        running = False
        mixer.music.stop()

pygame.quit()
mixer.music.stop()