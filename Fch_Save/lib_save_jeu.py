# ============================================================
# LIBRAIRIE : Gestion des sauvegardes
# ============================================================
# Ce module permet de gérer les sauvegardes des mini-jeux.
# Il inclut des fonctions pour créer, charger, mettre à jour
# et supprimer des sauvegardes dans un fichier JSON.
# ============================================================

import json
import os

# ------------------------------------------------------------
# CONSTANTES
# ------------------------------------------------------------

fch_save_jeu = os.path.join(os.path.dirname(__file__), "sauvegardes_becile_contre_attaque.json")  # Chemin du fichier JSON pour sauvegarder les données utilisable par tous

# ------------------------------------------------------------
# FONCTIONS PRINCIPALES
# ------------------------------------------------------------

def load_data_json(chemin_fichier=fch_save_jeu):
    """
    Charge le contenu d'un fichier JSON dans un dictionnaire.

    :param chemin_fichier: Chemin vers le fichier JSON.
    :return: Dictionnaire contenant les données du fichier JSON.
    """
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        return donnees
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
        return {}

    except json.JSONDecodeError:
        print(f"Erreur : Le fichier '{chemin_fichier}' contient une erreur de format JSON.")
        return {}

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return {}
    

def update_parameter_json(etat_sound, save_use, chemin_fichier=fch_save_jeu):
    """
    Modifie les valeurs de 'etat_sound' et 'who_play' dans le fichier JSON, puis enregistre les modifications.

    :param etat_sound: Nouvelle valeur pour 'etat_sound' (booléen).
    :param save_use: Nouvelle valeur pour 'who_play' (chaîne de caractères).
    :param chemin_fichier: Chemin vers le fichier JSON.
    """
    # Charger les données existantes
    donnees = load_data_json(chemin_fichier)
    
    if not donnees:
        print("Erreur : Impossible de charger les données JSON.")
        return

    # Modifier les valeurs
    if "parametre" in donnees:
        donnees["parametre"]["etat_sound"] = etat_sound
        donnees["parametre"]["who_play"] = save_use

    else:
        print("Erreur : La clé 'parametre' est introuvable dans le fichier JSON.")
        return

    # Enregistrer les modifications
    try:
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)
        print("Les modifications ont été enregistrées avec succès.")

    except Exception as e:
        print(f"Erreur lors de l'enregistrement des données : {e}")


def load_parameter_json(chemin_fichier=fch_save_jeu):
    """
    Récupère les paramètres 'etat_sound' et 'who_play' depuis le fichier JSON et les retourne séparément.

    :param chemin_fichier: Chemin vers le fichier JSON.
    :return: Tuple contenant les valeurs de 'etat_sound' et 'who_play', ou (None, None) en cas d'erreur.
    """
    # Charger les données existantes
    donnees = load_data_json(chemin_fichier)
    
    if not donnees:
        print("Erreur : Impossible de charger les données JSON.")
        return None, None

    # Vérifier si la clé 'parametre' existe
    if "parametre" in donnees:
        etat_sound = donnees["parametre"].get("etat_sound")
        who_play = donnees["parametre"].get("who_play")
        return etat_sound, who_play
    
    else:
        print("Erreur : La clé 'parametre' est introuvable dans le fichier JSON.")
        return None, None
    

def save_current_backup_json(mini_jeu, niv_finish, chemin_fichier=fch_save_jeu):
    """
    Enregistre ou met à jour les données de sauvegarde pour la personne actuellement en train de jouer.

    :param mini_jeu: Nom du mini-jeu à mettre à jour (chaîne de caractères).
    :param niv_finish: État de fin du niveau (booléen).
    :param chemin_fichier: Chemin vers le fichier JSON.
    """
    # Récupérer les paramètres pour savoir qui joue
    _, who_play = load_parameter_json(chemin_fichier)
    
    if not who_play:
        print("Erreur : Impossible de déterminer qui joue actuellement.")
        return

    # Charger les données existantes
    donnees = load_data_json(chemin_fichier)
    
    if not donnees:
        print("Erreur : Impossible de charger les données JSON.")
        return

    # Vérifier si la clé 'sauvegardes' existe
    if "sauvegardes" not in donnees:
        print("Erreur : La clé 'sauvegardes' est introuvable dans le fichier JSON.")
        return

    # Vérifier si la personne existe dans les sauvegardes, sinon l'ajouter
    if who_play not in donnees["sauvegardes"]:
        donnees["sauvegardes"][who_play] = {}

    # Mettre à jour ou ajouter le mini-jeu pour la personne
    if mini_jeu not in donnees["sauvegardes"][who_play]:
        donnees["sauvegardes"][who_play][mini_jeu] = {}

    donnees["sauvegardes"][who_play][mini_jeu]["niv_finish"] = niv_finish

    # Enregistrer les modifications
    try:
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)
        print(f"Sauvegarde mise à jour pour {who_play} dans le mini-jeu '{mini_jeu}'.")

    except Exception as e:
        print(f"Erreur lors de l'enregistrement des données : {e}")


def add_new_save_json(nom_personne, chemin_fichier=fch_save_jeu):
    """
    Ajoute une nouvelle sauvegarde pour une personne spécifique dans le fichier JSON.

    :param nom_personne: Nom de la personne pour laquelle ajouter une sauvegarde (chaîne de caractères).
    :param chemin_fichier: Chemin vers le fichier JSON.
    """
    # Charger les données existantes
    donnees = load_data_json(chemin_fichier)
    
    if not donnees:
        print("Erreur : Impossible de charger les données JSON.")
        return

    # Vérifier si la clé 'sauvegardes' existe
    if "sauvegardes" not in donnees:
        donnees["sauvegardes"] = {}

    # Vérifier si la personne existe déjà
    if nom_personne in donnees["sauvegardes"]:
        print(f"Erreur : Une sauvegarde pour '{nom_personne}' existe déjà.")
        return

    # Ajouter une nouvelle sauvegarde pour la personne
    donnees["sauvegardes"][nom_personne] = {
        "mini_jeu1": {"niv_finish": False},
        "mini_jeu2": {"niv_finish": False},
        "mini_jeu3": {"niv_finish": False}
    }

    # Enregistrer les modifications
    try:
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)
        print(f"Nouvelle sauvegarde ajoutée pour '{nom_personne}'.")

    except Exception as e:
        print(f"Erreur lors de l'enregistrement des données : {e}")


def delete_save_json(nom_personne, chemin_fichier=fch_save_jeu):
    """
    Supprime la sauvegarde d'une personne spécifique dans le fichier JSON.

    :param nom_personne: Nom de la personne dont la sauvegarde doit être supprimée (chaîne de caractères).
    :param chemin_fichier: Chemin vers le fichier JSON.
    """
    # Charger les données existantes
    donnees = load_data_json(chemin_fichier)
    
    if not donnees:
        print("Erreur : Impossible de charger les données JSON.")
        return

    # Vérifier si la clé 'sauvegardes' existe
    if "sauvegardes" not in donnees:
        print("Erreur : La clé 'sauvegardes' est introuvable dans le fichier JSON.")
        return

    # Vérifier si la personne existe dans les sauvegardes
    if nom_personne not in donnees["sauvegardes"]:
        print(f"Erreur : Aucune sauvegarde trouvée pour '{nom_personne}'.")
        return

    # Supprimer la sauvegarde de la personne
    del donnees["sauvegardes"][nom_personne]

    # Enregistrer les modifications
    try:
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)
        print(f"Sauvegarde supprimée pour '{nom_personne}'.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement des données : {e}")


# ============================================================
# FIN DU MODULE
# ============================================================