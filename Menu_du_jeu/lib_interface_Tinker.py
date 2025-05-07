# ============================================================
# LIBRAIRIE : Gestion des interfaces Tinker
# ============================================================
# # Ce module permet de gérer les interfaces graphiques
# ============================================================

import tkinter as tk



def sound_interface_tinker():
    """
    Interface pour régler le son du jeu.
    Permet de choisir entre son activé ou désactivé.
    """
    def valider_action():
        """
        Fonction de validation de l'action choisie.
        Récupère la valeur sélectionnée et ferme la fenêtre.
        """
        nonlocal action
        action = var.get()
        fenetre.destroy()

    action = None
    fenetre = tk.Tk()
    fenetre.title("Réglage du son")

    # Dimensions de la fenêtre
    largeur_fenetre = 300
    hauteur_fenetre = 150

    # Obtenir les dimensions de l'écran
    largeur_ecran = fenetre.winfo_screenwidth()
    hauteur_ecran = fenetre.winfo_screenheight()

    # Calculer la position x et y pour centrer la fenêtre
    position_x = (largeur_ecran // 2) - (largeur_fenetre // 2)
    position_y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

    # Définir la géométrie de la fenêtre
    fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{position_x}+{position_y}")

    tk.Label(fenetre, text="Régler le son :").pack(pady=10)

    var = tk.BooleanVar(value=True)  # Valeur par défaut : True (son activé)
    tk.Radiobutton(fenetre, text="Activé (Demande plus de performance)", variable=var, value=True).pack(anchor="w", padx=20)
    tk.Radiobutton(fenetre, text="Désactivé", variable=var, value=False).pack(anchor="w", padx=20)

    tk.Button(fenetre, text="Valider", command=valider_action).pack(pady=10)

    fenetre.mainloop()

    return action


def sauvegarde_interface():
    """
    Interface de gestion des sauvegardes.
    Permet de charger, supprimer ou créer une sauvegarde.
    """
    def charger_action():
        """
        Fonction de chargement d'une sauvegarde.
        """
        print("Charger action exécutée")
        # Ajoutez ici le code pour charger une sauvegarde

    def supprimer_action():
        """
        Fonction de suppression d'une sauvegarde.
        """
        print("Supprimer action exécutée")
        # Ajoutez ici le code pour supprimer une sauvegarde

    def nouvelle_action():
        """
        Fonction de création d'une nouvelle sauvegarde.
        """
        print("Nouvelle action exécutée")
        # Ajoutez ici le code pour créer une nouvelle sauvegarde

    fenetre = tk.Tk()
    fenetre.title("Sauvegarde")

    # Dimensions de la fenêtre
    largeur_fenetre = 400
    hauteur_fenetre = 200

    # Obtenir les dimensions de l'écran
    largeur_ecran = fenetre.winfo_screenwidth()
    hauteur_ecran = fenetre.winfo_screenheight()

    # Calculer la position x et y pour centrer la fenêtre
    position_x = (largeur_ecran // 2) - (largeur_fenetre // 2)
    position_y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

    # Définir la géométrie de la fenêtre
    fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{position_x}+{position_y}")

    # Titre
    tk.Label(fenetre, text="Gestion des sauvegardes", font=("Arial", 14)).pack(pady=10)

    # Barre de recherche
    tk.Label(fenetre, text="Rechercher une sauvegarde :").pack(pady=5)
    barre_recherche = tk.Entry(fenetre, width=40)
    barre_recherche.pack(pady=5)

    # Boutons
    boutons_frame = tk.Frame(fenetre)
    boutons_frame.pack(pady=10)

    tk.Button(boutons_frame, text="Charger", command=charger_action).pack(side="left", padx=10)
    tk.Button(boutons_frame, text="Supprimer", command=supprimer_action).pack(side="left", padx=10)
    tk.Button(boutons_frame, text="Nouvelle", command=nouvelle_action).pack(side="left", padx=10)

    fenetre.mainloop()

    return None  # Ou une valeur par défaut si nécessaire