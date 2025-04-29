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

SAVE_FILE = os.path.join(os.path.dirname(__file__), "sauvegardes_bécile_contre_attaque.json")  # Chemin du fichier JSON pour sauvegarder les données utilisable par tous

# ------------------------------------------------------------
# FONCTIONS PRINCIPALES
# ------------------------------------------------------------

def load_save():
    """
    Charge les données du fichier JSON.
    :return: Un dictionnaire contenant les données des sauvegardes.
    """
    if not os.path.exists(SAVE_FILE):
        # Si le fichier n'existe pas, on retourne une structure vide
        return {"sauvegardes": {}}
    
    with open(SAVE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_to_file(data):
    """
    Sauvegarde les données dans le fichier JSON.
    :param data: Dictionnaire contenant les données à sauvegarder.
    """
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def make_save(save_name):
    """
    Crée une nouvelle sauvegarde.
    :param save_name: Nom de la sauvegarde à créer.
    :raises ValueError: Si la sauvegarde existe déjà ou si le nombre maximum est atteint.
    """
    data = load_save()
    
    if save_name in data["sauvegardes"]:
        raise ValueError(f"La sauvegarde '{save_name}' existe déjà.")
    
    if len(data["sauvegardes"]) >= 3:
        raise ValueError("Le nombre maximum de sauvegardes (3) est atteint.")
    
    data["sauvegardes"][save_name] = {
        "mini_jeu1": {"niv_finish": False},
        "mini_jeu2": {"niv_finish": False},
        "mini_jeu3": {"niv_finish": False}
    }
    
    save_to_file(data)

def save_advance(save_name, mini_game):
    """
    Met à jour l'état de progression d'un mini-jeu dans une sauvegarde.
    :param save_name: Nom de la sauvegarde.
    :param mini_game: Nom du mini-jeu (e.g., "mini_jeu1").
    :raises ValueError: Si la sauvegarde ou le mini-jeu n'existe pas.
    """
    data = load_save()
    
    if save_name not in data["sauvegardes"]:
        raise ValueError(f"La sauvegarde '{save_name}' n'existe pas.")
    
    if mini_game not in data["sauvegardes"][save_name]:
        raise ValueError(f"Le mini-jeu '{mini_game}' n'existe pas dans la sauvegarde '{save_name}'.")
    
    # Marquer le mini-jeu comme terminé (True)
    data["sauvegardes"][save_name][mini_game]["niv_finish"] = True
    
    save_to_file(data)

def delete_save(save_name):
    """
    Supprime une sauvegarde.
    :param save_name: Nom de la sauvegarde à supprimer.
    :raises ValueError: Si la sauvegarde n'existe pas.
    """
    data = load_save()
    
    if save_name not in data["sauvegardes"]:
        raise ValueError(f"La sauvegarde '{save_name}' n'existe pas.")
    
    del data["sauvegardes"][save_name]
    
    save_to_file(data)

# ============================================================
# FIN DU MODULE
# ============================================================