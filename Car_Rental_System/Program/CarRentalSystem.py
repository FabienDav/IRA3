# CarRentalSystem.py
# Fichier principal de l'application de location de véhicules

import os
import time
from Application_Data import (
    liste_Client,
    liste_Vehicule,
    trouver_Client_Par_Id,
    trouver_Vehicule_Par_Id,
    play_sound_async,
    simuler_Activite,
    charger_Donnees,
    sauvegarder_Donnees
)

if not charger_Donnees():
    # Première exécution uniquement
    simuler_Activite()

# ----------------------
# Création client et véhicule
# ----------------------

def creer_Client():
    os.system('cls')
    print("Création d'un client")
    first_Name = input("Nom : ")
    last_Name = input("Prénom : ")
    age = input("Âge : ")

    if not age.isdigit():
        play_sound_async("Windows_7_critical_stop.wav")
        print("Âge invalide")
        input()
        return

    age = int(age)
    licence = False
    if age > 17:
        reponse = ""
        while reponse not in ["O", "n"]:
            reponse = input("Avez-vous un permis de conduire ? [O/n] : ")
        licence = reponse == "O"

    from Customer import Customer
    liste_Client.append(Customer(first_Name, last_Name, age, licence))
    print("Client créé avec succès")
    input()


def creer_Vehicule():
    os.system('cls')
    print("Création d'un véhicule")
    brand = input("Marque : ")
    model = input("Modèle : ")
    category = input("Catégorie : ")
    tarif = input("Tarif : ")

    if not tarif.isdigit():
        play_sound_async("Windows_7_critical_stop.wav")
        print("Tarif invalide")
        input()
        return

    state = input("État : ")

    from Vehicule import Vehicule
    liste_Vehicule.append(Vehicule(brand, model, category, int(tarif), state))
    print("Véhicule créé avec succès")
    input()


# ----------------------
# Réservation
# ----------------------

def reservation_Vehicule():
    os.system('cls')
    print("Réservation d'un véhicule")

    id_Client = input("Id client : ")
    id_Vehicule = input("Id véhicule : ")
    date_Reservation = input("Date (dd/mm/yy) : ")
    duree = input("Durée (jours) : ")

    if not (id_Client.isdigit() and id_Vehicule.isdigit() and duree.isdigit()):
        play_sound_async("Windows_7_critical_stop.wav")
        print("Entrées invalides")
        input()
        return

    index_Client = trouver_Client_Par_Id(int(id_Client))
    if index_Client is None:
        input()
        return

    liste_Client[index_Client].reserver_Vehicule(
        int(id_Vehicule),
        date_Reservation,
        int(duree),
        liste_Vehicule,
        trouver_Vehicule_Par_Id
    )
    input()


# ----------------------
# Affichages
# ----------------------

def afficher_Client():
    os.system('cls')
    print("+=======+======================+======================+=====+========+===========+")
    print(f"| {'Id':<5} | {'Nom':<20} | {'Prénom':<20} | {'Âge':<3} | {'Permis':<6} | {'Profit':<9} |")
    print("+=======+======================+======================+=====+========+===========+")
    for c in liste_Client:
        print(f"{c.id:<5} | {c.first_Name:<20} | {c.last_Name:<20} | {c.age:<3} | {c.licence!s:<6} | {c.profit:<8}€ |")
    print("+=======+======================+======================+=====+========+===========+")
    input()


def afficher_Vehicule():
    os.system('cls')
    profit_total = 0
    print("+=======+=================+===========================+============+=======+============+==========+")
    print(f"| {'Id':<5} | {'Marque':<15} | {'Modèle':<25} | {'Catégorie':<10} | {'Tarif':<5} | {'État':<10} | {'Profit':<8} |")
    print("+=======+=================+===========================+============+=======+============+==========+")
    for v in liste_Vehicule:
        print(f"{v.id:<5} | {v.brand:<15} | {v.model:<25} | {v.category:<10} | {v.tarif:<4}€ | {v.state:<10} | {v.profit:<7}€ |")
        profit_total += v.profit

    print("+=======+=================+===========================+============+=======+============+==========+")
    print(f"Profit total : {profit_total}€")
    input()


def renseignement_Client():
    os.system('cls')
    id_Client = input("Id du client : ")
    if not id_Client.isdigit():
        return

    index = trouver_Client_Par_Id(int(id_Client))
    if index is None:
        input()
        return

    liste_Client[index].historique(liste_Vehicule, trouver_Vehicule_Par_Id)
    input()


def renseignement_Vehicule():
    os.system('cls')
    id_Vehicule = input("Id du véhicule : ")
    if not id_Vehicule.isdigit():
        return

    index = trouver_Vehicule_Par_Id(int(id_Vehicule))
    if index is None:
        input()
        return

    liste_Vehicule[index].historique(liste_Client, trouver_Client_Par_Id)
    input()


# ----------------------
# Menu
# ----------------------

def afficher_Menu():
    print("\n========================= MENU ==========================")
    print("1 - Créer un client")
    print("2 - Créer un véhicule")
    print("3 - Réserver un véhicule")
    print("4 - Afficher tous les clients")
    print("5 - Afficher tous les véhicules")
    print("6 - Détails d'un client")
    print("7 - Détails d'un véhicule")
    print("0 - Quitter")
    print("=========================================================\n")


def activer_Session() :
    users = ["root","user","Fabien"]
    passwords = ["root","user","Fabien"]

    point = "."
    
    for i in range (0,9) :
        os.system('cls')
        print(f"Initlialisation système{point}")
        point += "."
        if point == "...." :
            point = "."
        time.sleep(0.1)

    play_sound_async("Windows_7_startup_sound.wav")

    user = ""
    while user not in users :
        os.system('cls')
        user = str(input("User : "))
    
    for u in range (0,len(users)) :
        if users[u] == user :
            index = u

    valid_password = passwords[index]
    password = ""
    while password != valid_password :
        os.system('cls')
        print(f"User : {user}")
        password = str(input("Password : "))

# ----------------------
# Lancement application
# ----------------------

activer_Session()
simuler_Activite()

entree = "999"
while entree != "0":
    os.system('cls')
    afficher_Menu()
    entree = input("Votre choix : ")

    if entree == "1":
        play_sound_async("Mouse_Click.wav")
        creer_Client()
    elif entree == "2":
        play_sound_async("Mouse_Click.wav")
        creer_Vehicule()
    elif entree == "3":
        play_sound_async("Mouse_Click.wav")
        reservation_Vehicule()
    elif entree == "4":
        play_sound_async("Mouse_Click.wav")
        afficher_Client()
    elif entree == "5":
        play_sound_async("Mouse_Click.wav")
        afficher_Vehicule()
    elif entree == "6":
        play_sound_async("Mouse_Click.wav")
        renseignement_Client()
    elif entree == "7":
        play_sound_async("Mouse_Click.wav")
        renseignement_Vehicule()
    elif entree == "0" :
        sauvegarder_Donnees()
