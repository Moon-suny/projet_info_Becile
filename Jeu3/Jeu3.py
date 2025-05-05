import pygame
from pygame.locals import *

# --- Initialisation ---
pygame.init()
W, H = 1000, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Jeu 3')

# --- Constantes ---
PLAYER_SPEED  = 3
GRAVITY       = 0.6
JUMP_STRENGTH = -21
SOL_HEIGHT    = 50

# --- Chargement images ---
player_surf = pygame.image.load(r"..\projet_info_Becile\Cinematique\img\creature_jeu.png").convert_alpha()
barre_surf  = pygame.image.load('Jeu3/img/barre.png').convert_alpha()
bg_surf     = pygame.image.load('Jeu3/img/Backgrnd.png').convert()
obj_surf    = pygame.image.load(r"..\projet_info_Becile\Cinematique\img\jambe_du_robot.png").convert_alpha()

# --- Objectif en haut-gauche ---
obj_surf = pygame.transform.scale(obj_surf, (25, 25))
obj_rect = obj_surf.get_rect(topleft=(0,0))

# --- Joueur ---
player_w, player_h = 50, 25
player_surf = pygame.transform.scale(player_surf, (player_w, player_h))
player_rect = player_surf.get_rect(x=946, y=703)
player_mask = pygame.mask.from_surface(player_surf)
vy = 0
on_ground = False

# --- Barre (plateforme) ---
barre_rect = barre_surf.get_rect(topleft=(0,0))
barre_mask = pygame.mask.from_surface(barre_surf)

# --- Sol ---
sol_rect = pygame.Rect(0, H - SOL_HEIGHT, W, SOL_HEIGHT)
sol_surf = pygame.Surface((W, SOL_HEIGHT)); sol_surf.fill((255,255,255)); sol_surf.set_alpha(100)
sol_mask = pygame.mask.from_surface(sol_surf)

clock = pygame.time.Clock()
running = True

while running:
    # --- Événements ---
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False

    # --- Contrôles ---
    keys = pygame.key.get_pressed()
    dx = 0
    if keys[K_LEFT]:
        dx = -PLAYER_SPEED
    if keys[K_RIGHT]:
        dx =  PLAYER_SPEED
    if keys[K_UP] and on_ground:
        vy = JUMP_STRENGTH
        on_ground = False

    # --- Gravité ---
    vy += GRAVITY
    if vy > 10: vy = 10
    on_ground = False

    # --- Mouvement horizontal & collisions barre ---
    player_rect.x += dx
    offset = (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)
    pp = player_mask.overlap(barre_mask, offset)
    if pp:
        y_mask = pp[1]
        cutoff = int(player_h * 0.75)
        if y_mask < cutoff:
            # collision sur le corps → blocage horizontal total
            player_rect.x -= dx
        else:
            # collision sur les pieds → on gravite d'1px
            player_rect.y -= 1

    # --- Mouvement vertical & collisions barre/sol ---
    player_rect.y += int(vy)

    # collision barre verticale
    offset = (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)
    pp = player_mask.overlap(barre_mask, offset)
    if pp:
        if vy > 0:
            # on tombait → on remonte jusqu'à décoller
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.y -= 1
            vy = 0
            on_ground = True
        else:
            # on montait → on repousse
            while player_mask.overlap(barre_mask, (barre_rect.x - player_rect.x, barre_rect.y - player_rect.y)):
                player_rect.y += 1
            vy = 0
    else:
        # collision sol
        offset = (sol_rect.x - player_rect.x, sol_rect.y - player_rect.y)
        pp = player_mask.overlap(sol_mask, offset)
        if pp and vy >= 0:
            while player_mask.overlap(sol_mask, (sol_rect.x - player_rect.x, sol_rect.y - player_rect.y)):
                player_rect.y -= 1
            vy = 0
            on_ground = True

    # --- Objectif ---
    if player_rect.colliderect(obj_rect):
        print("Objectif atteint !")
        running = False

    # --- Limites écran ---
    if player_rect.left   < 0:         player_rect.left  = 0
    if player_rect.right  > W:         player_rect.right = W

    # --- Affichage ---
    screen.blit(bg_surf,      (0,0))
    screen.blit(barre_surf,   barre_rect)
    screen.blit(sol_surf,     sol_rect)
    screen.blit(player_surf,  player_rect)
    screen.blit(obj_surf,     obj_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
