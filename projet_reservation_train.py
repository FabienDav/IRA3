# Sert à afficher tout les trains
def afficherTrain(trains) :
    listeClef = trains.keys()
    for i in listeClef :
        nbrPlaceTotal = trains[i]["places_total"]
        nbrPlaceRestante = trains[i]["places_restantes"]
        print(i, "->", nbrPlaceRestante, "place restante sur", nbrPlaceTotal)
    return None

# Permet de réserver une place
def reserverPlace(trains) :

    nomPassager = str(input("Quel est votre nom ?"))
    nomDestination = str(input("Où voulez vous aller ?"))

    listeDestination = trains.keys()
    # Vérifie si la destination est valide
    if nomDestination not in listeDestination :
        print("ERREUR : Destination invalide")
        return None

    # Vérifie si le passager n' pas déja prit un billet pour cette destination
    if nomPassager in trains[nomDestination]["passagers"] :
        print("ERREUR : ", nomPassager, "est déjà dans le train", nomDestination)
        return None

    # Vérifie si le train n'est pas plein
    if trains[nomDestination]["places_restantes"] < 1 :
        print("ERREUR : Nombre de place pour", nomDestination, "insuffisante")
    else :
        # Inscrit le passager si tout est OK
        trains[nomDestination]["passagers"].add(nomPassager)
        trains[nomDestination]["places_restantes"] = trains[nomDestination]["places_restantes"] - 1
        print("SUCCES : Ajout de ",nomPassager, "dans", nomDestination)

    return None

# Permet d'annuler la réservation d'une place
def annulerReservation(trains) :
    
    nomPassager = str(input("Quel est votre nom ?"))
    nomDestination = str(input("Où voulez vous aller ?"))

    listeDestination = trains.keys()
    # Vérifie si la destination est valide
    if nomDestination not in listeDestination :
        print("ERREUR : Destination invalide")
        return None

    # Vérifie si le passager n' pas déja prit un billet pour cette destination
    if nomPassager in trains[nomDestination]["passagers"] :
        trains[nomDestination]["passagers"].remove(nomPassager)
        trains[nomDestination]["places_restantes"] = trains[nomDestination]["places_restantes"] + 1
        print("SUCCES : ", nomPassager, "a bien retirer sa place du train", nomDestination)
    else :
        print("ERREUR : ", nomPassager, "n'a pas rézserver de billet dans le train", nomDestination)
    return None

# Affiche un train spécifique
def afficherTrainSpecifique(trains) :
   
    nomDestination = str(input("Quel train vous intéresse ?"))

    listeDestination = trains.keys()
    if nomDestination not in listeDestination :
        print("ERREUR : Destination invalide")
    else :
        print("Les passagers dans le train ",nomDestination,"sont :")
        for voyageur in trains[nomDestination]["passagers"] :
            print(voyageur)

    return None

# Affiche les trains complets
def afficherTrainComplet(trains) :
    listeDestination = trains.keys()
    print("Voici la liste des trains complet :")
    for i in listeDestination :
        if trains[i]["places_restantes"] == 0 :
            print (i)
    return None

trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}

Entree = 6

while True and Entree != 0 :
    print("\n MENU")
    print("-----------------------------------------------")
    print("1 - Afficher les trains")
    print("2 - Réserver une place")
    print("3 - Annuler une réservation")
    print("4 - Afficher les passagers d'un train")
    print("5 - Afficher les trains complets")
    print("0 - Quitter")
    print("-----------------------------------------------")
    Entree = int(input("Que souhaitez vous faire ?\n"))
    print("")

    if Entree == 1 :
        afficherTrain(trains)
    if Entree == 2 :
        reserverPlace(trains)
    if Entree == 3 :
        annulerReservation(trains)
    if Entree == 4 :
        afficherTrainSpecifique(trains)
    if Entree == 5 :
        afficherTrainComplet(trains)
    