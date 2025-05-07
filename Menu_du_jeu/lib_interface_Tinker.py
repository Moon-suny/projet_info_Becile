# ============================================================
# LIBRAIRIE : Gestion des interfaces Tinker
# ============================================================
# # Ce module permet de gérer les interfaces graphiques
# ============================================================

import tkinter as tk
import json
import os
import subprocess
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Fch_Save")))
from lib_save_jeu import update_parameter_json, load_data_json, delete_save_json, add_new_save_json # Importer les fonctions de sauvegarde et de chargement de partie

action = True # Valeur par défaut pour le son (True = activé, False = désactivé)


def sound_interface_tinker():
    """
    Interface pour régler le son du jeu.
    Permet de choisir entre son activé ou désactivé.
    """
    global action

    def valider_action():
        """
        Fonction de validation de l'action choisie.
        Récupère la valeur sélectionnée (True ou False) et met à jour le paramètre JSON.
        Ferme la fenêtre après validation.
        """
        global action

        action = var.get()  # Récupère la valeur sélectionnée (True ou False)
        print(f"Action validée : {action}")
        update_parameter_json(etat_sound=action, save_use="")  # Met à jour l'état du son
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

    return None


def save_interface_tinker():
    """
    Interface de gestion des sauvegardes.
    Permet de charger, supprimer ou créer une sauvegarde.
    """

    def charger_action():
        """
        Fonction de chargement d'une sauvegarde.
        Vérifie si la sauvegarde existe et récupère le premier jeu non terminé.
        """
        texte_recherche = barre_recherche.get()
        print(f"Charger action exécutée pour : {texte_recherche}")

        # Charger les données du fichier JSON
        data = load_data_json()

        # Vérifier si la sauvegarde existe
        if texte_recherche not in data.get("sauvegardes", {}):
            print("Sauvegarde introuvable")

            fenetre.destroy()
            return save_interface_tinker()  # Rappeler l'interface de sauvegarde

        # Mettre à jour le paramètre JSON
        update_parameter_json(etat_sound=action, save_use=texte_recherche)

        # Récupérer les données de la sauvegarde
        sauvegarde = data["sauvegardes"][texte_recherche]

        # Vérifier l'avancement des jeux
        for jeu, details in sauvegarde.items():
            if not details.get("niv_finish", True):  # Si le niveau n'est pas terminé

                print(f"Premier jeu non terminé : {jeu}")

                if jeu == "mini_jeu1":
                    # Appeler la fonction de chargement du mini-jeu 1
                    print("Chargement du mini_jeu_1...")
                    # Ajoutez ici le code pour charger l'intro
                    chemin = os.path.abspath('..\projet_info_Becile\Cinematique\script\intro-p1.py')
                    subprocess.run(['python', chemin])

                    break # Sortir de la boucle après le premier jeu non terminé
                    
                elif jeu == "mini_jeu2":
                    # Appeler la fonction de chargement du mini-jeu 2
                    print("Chargement du mini_jeu_2...")
                    # Ajoutez ici le code pour charger dialogue avant le mini-jeu 2
                    chemin = os.path.abspath('..\projet_info_Becile\Cinematique\Dialogues\Dialogue-.py')
                    subprocess.run(['python', chemin])
                    break # Sortir de la boucle après le premier jeu non terminé
                
                elif jeu == "mini_jeu3":
                    # Appeler la fonction de chargement du mini-jeu 3
                    print("Chargement du mini_jeu_3...")
                    # Ajoutez ici le code pour charger dialogue avant le mini-jeu 3
                    chemin = os.path.abspath('..\projet_info_Becile\Cinematique\Dialogues\Dialogue-3.py')
                    subprocess.run(['python', chemin])
                    break # Sortir de la boucle après le premier jeu non terminé

            
        print(f"Toutes les étapes pour {texte_recherche} sont déjà terminées.")
        
        fenetre.destroy()


    def supprimer_action():
        """
        Fonction de suppression d'une sauvegarde.
        """
        texte_recherche = barre_recherche.get()
        print(f"Suppresion action exécutée pour : {texte_recherche}")
        delete_save_json(texte_recherche) # Appel de la fonction de suppression de sauvegarde
        fenetre.destroy()

    def nouvelle_action():
        """
        Fonction de création d'une nouvelle sauvegarde.
        """
        texte_recherche = barre_recherche.get()
        print(f"Nouvelle action exécutée pour : {texte_recherche}")
        add_new_save_json(texte_recherche) # Appel de la fonction d'ajout de nouvelle sauvegarde
        fenetre.destroy()

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

    return None