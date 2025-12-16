from datetime import datetime, timedelta
import os
import time
import winsound

# ----------------------
# VEHICLE
# ----------------------
class Vehicule:
    _compteur_Vehicule = 0 # COmpteur d'instance de Véhicule
    #Constructeur
    def __init__(self, brand: str, model: str, category: str, tarif: int, state: str):
        Vehicule._compteur_Vehicule += 1
        self.id = Vehicule._compteur_Vehicule # Chaque ID est unique
        self.brand = brand
        self.model = model
        self.category = category
        self.tarif = tarif
        self.state = state
        self.historic = {}  # historique des réservations
        self.profit = 0
    
    # Affiche l'historique du véhicule
    def historique(self) :
        print(f"Historique des réservations pour {self.brand} {self.model}:")
        print(f"{'Date':<8} | {'Durée (jours)':<13} | {'ID Client':<9} | {'Nom & Prénom Client':<30} | {'Profit':<7} |")
        print("=========+===============+===========+================================+=========+")
        for d, info in self.historic.items():
            id_client = info["client_Id"]
            index_Client = trouver_Vehicule_Par_Id(id_client)
            client = liste_Client[index_Client]
            client_Nom_Prenom = client.first_Name + " " + client.last_Name
            prix = self.tarif * info['duree']
            print(f"{d:<8} | {info['duree']:<13} | {id_client:<9} | {client_Nom_Prenom:<30} | {prix:<6}€ |")
        print("=========+===============+===========+================================+=========+")
        print(f"Ce véhicule a fait un profit total de {self.profit}€")
        return self.historic

# ----------------------
# CUSTOMER
# ----------------------
class Customer :
    _compteur_Customer = 0 # Compte le nombre d'instance de Client

    # Constructeur
    def __init__(self, first_Name, last_Name, age, licence=False):
        Customer._compteur_Customer += 1
        self.id = Customer._compteur_Customer # Chaque ID est unique
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.age = int(age)
        self.licence = licence
        self.historic = {}  # historique des réservations
        self.profit = 0

    # Sert a réserver un véhicule
    def reserver_Vehicule(self, id_Vehicule, date_Reservation, duree) :
        # On retrouve la place du véhicule
        index_Vehicule = trouver_Vehicule_Par_Id(id_Vehicule)
        if index_Vehicule == None :
            return
        date_format = "%d/%m/%y"

        # Vérification client
        if self.age < 17:
            print("Le client est trop jeune pour conduire")
            return
        if not self.licence:
            print("Le client n'a pas de permis de conduire")
            return

        # Convertir la date en datetime
        date_debut = datetime.strptime(date_Reservation, date_format)
        date_fin = date_debut + timedelta(days=duree)

        # Vérifier disponibilité du véhicule
        for d, info in liste_Vehicule[index_Vehicule].historic.items():
            ancien_debut = datetime.strptime(d, date_format)
            ancien_fin = ancien_debut + timedelta(days=info["duree"])
            if date_debut < ancien_fin and date_fin > ancien_debut:
                print(f"Le véhicule n'est pas disponible entre {ancien_debut.strftime(date_format)} et {ancien_fin.strftime(date_format)}")
                return

        # Ajouter la réservation dans l'historique
        self.historic[date_Reservation] = {
            "vehicule_Id": id_Vehicule,
            "category": liste_Vehicule[index_Vehicule].category,
            "duree": duree
        }
        liste_Vehicule[index_Vehicule].historic[date_Reservation] = {
            "client_Id": self.id,
            "duree": duree
        }

        print(f"Véhicule réservé du {date_debut.strftime(date_format)} au {date_fin.strftime(date_format)}")
        print(f"Le cout de la location est de {liste_Vehicule[index_Vehicule].tarif * duree}€")
        liste_Vehicule[index_Vehicule].profit += liste_Vehicule[index_Vehicule].tarif * duree
        self.profit += liste_Vehicule[index_Vehicule].tarif * duree
        return
    
    def historique(self) :
        profit_Total = 0
        print(f"Historique des réservations pour {self.first_Name} {self.last_Name}:")
        print(f"{'Id':<5} | {'Véhicule':<40} | {'Catégorie':<10} | {'Début':<8} | {'Durée (jours)':<13} | {'Coût':<7} |")
        print("======+==========================================+============+==========+===============+=========+")
        for d, info in self.historic.items():
            index_Vehicule = trouver_Vehicule_Par_Id(info["vehicule_Id"])
            vehicule = liste_Vehicule[index_Vehicule]
            nom_vehicule = vehicule.brand + " " + vehicule.model

            prix = vehicule.tarif * info['duree']
            profit_Total += prix
            print(f"{vehicule.id:<5} | {nom_vehicule:<40} | {vehicule.category:<10} | {d:<8} | {info['duree']:<13} | {prix:<6}€ |")
        print("======+==========================================+============+==========+===============+=========+")
        print(f"Cette personne a dépensée {profit_Total}€")
        return self.historic

# ----------------------
# Listes globales
# ----------------------
liste_Client = [
    Customer("DAVID", "Fabien", 20, True),
    Customer("METAIS", "Mory", 20, True),
    Customer("AGBINKO", "Emmanuel", 20, True),
    Customer("DARWICHE","Ahmad", 31, True),
    Customer("TOTO", "Tintin", 17, False),
    Customer("MARTIN", "Luc", 25, True),
    Customer("DUPONT", "Sophie", 30, True),
    Customer("JUSTIN", "Jean", 22, True),
    Customer("MOREAU", "Claire", 28, True),
    Customer("ROUSSEAU", "Antoine", 35, True),
    Customer("FONTAINE", "Emma", 21, True),
    Customer("GIRAUD", "Louis", 27, True),
    Customer("BLANCHET", "Julie", 24, True),
    Customer("LEROY", "Nicolas", 32, True),
    Customer("VINCENT", "Camille", 29, True),
    Customer("RENAUD", "Bastien", 26, True),
    Customer("MARCHAND", "Elise", 34, True),
    Customer("PICARD", "Hugo", 22, True),
    Customer("MATHIEU", "Sarah", 29, True),
    Customer("BARRET", "Quentin", 31, True),
    Customer("NOEL", "Alicia", 28, True),
    Customer("LEMAIRE", "Thomas", 33, True),
    Customer("PERRIN", "Laura", 24, True),
    Customer("JACQUOT", "Adrien", 27, True),
    Customer("POTTIER", "Maeva", 30, True),
    Customer("RIVIERE", "Clement", 23, True),
    Customer("CHARLET", "Oceane", 32, True),
    Customer("GRANGER", "Lucas", 35, True),
    Customer("BOUCHER", "Manon", 26, True),
    Customer("TERRIER", "Julien", 28, True)
]

liste_Vehicule = [
    Vehicule("Citroen", "C2", "Car", 50, "Used"),
    Vehicule("Citroen", "H VAN", "Truck", 100, "New"),
    Vehicule("Yamaha", "600 Diversion","Motorcycle",60,"Destroyed"),
    Vehicule("Renault", "Clio IV", "Car", 45, "Used"),
    Vehicule("Peugeot", "3008", "Car", 80, "New"),
    Vehicule("Ford", "Focus", "Car", 55, "Used"),
    Vehicule("Mercedes", "Actros", "Truck", 150, "Used"),
    Vehicule("Volvo", "FH16", "Truck", 180, "New"),
    Vehicule("MAN", "TGX", "Truck", 160, "Used"),
    Vehicule("Honda", "CB500F", "Motorcycle", 50, "New"),
    Vehicule("Kawasaki", "Z900", "Motorcycle", 70, "Used"),
    Vehicule("Suzuki", "GSX-R750", "Motorcycle", 90, "New"),
    Vehicule("Harley-Davidson", "Iron 883", "Motorcycle", 85, "Used"),
    Vehicule("Audi", "A3", "Car", 75, "New"),
    Vehicule("BMW", "X1", "Car", 90, "Used"),
    Vehicule("Tesla", "Model 3", "Car", 120, "New"),
    Vehicule("Renault", "Master", "Truck", 140, "Used"),
    Vehicule("DAF", "XF", "Truck", 170, "New"),
    Vehicule("Scania", "R500", "Truck", 190, "Used"),
    Vehicule("Yamaha", "MT-07", "Motorcycle", 65, "New"),
    Vehicule("KTM", "Duke 890", "Motorcycle", 85, "New"),
    Vehicule("Ducati", "Monster", "Motorcycle", 95, "Used"),
    Vehicule("Honda", "Civic", "Car", 60, "Used"),
    Vehicule("Peugeot", "208", "Car", 50, "New"),
    Vehicule("Mercedes", "Sprinter", "Truck", 130, "New")
]

# ----------------------
# Création client et véhicules
# ----------------------
def creer_Client() :
    os.system('cls')
    print("Création d'un client")
    first_Name = input("Quel est votre nom ?\n")
    last_Name = input("Quel est votre prénom ?\n")
    age = input("Quel est votre âge ?\n")
    if not age.isdigit() :
        play_sound_async("Windows_7_critical_stop.wav")
        print("Age entré invalide")
        input()
        return
    age = int(age)
    licence = False
    if age > 17 :
        reponse = ""
        while reponse not in ["O", "n"]:
            reponse = input("Avez-vous un permis de conduire ? [O/n]\n")
        licence = reponse == "O"
    liste_Client.append(Customer(first_Name, last_Name, age, licence))
    print("Client créé avec succès !")

def creer_Vehicule() :
    os.system('cls')
    print("Création d'un véhicule")
    brand = input("Marque : ")
    model = input("Modèle : ")
    category = input("Catégorie : ")
    tarif = input("Tarif : ")
    if not tarif.isdigit() :
        play_sound_async("Windows_7_critical_stop.wav")
        print("Tarif invalide")
        input()
        return
    tarif = int(tarif)
    state = input("Etat :\n")
    liste_Vehicule.append(Vehicule(brand, model, category, tarif, state))
    print("Véhicule créé avec succès !")

# ----------------------
# Fonctions utilitaires
# ----------------------
def trouver_Client_Par_Id(id: int):
    for j, client in enumerate(liste_Client):
        if client.id == id:
            return j
    play_sound_async("Windows_7_critical_stop.wav")
    print("Id client non trouvé")
    input()
    return None

def trouver_Vehicule_Par_Id(id: int):
    for j, vehicule in enumerate(liste_Vehicule):
        if vehicule.id == id:
            return j
    play_sound_async("Windows_7_critical_stop.wav")
    print("Id véhicule non trouvé")
    input()
    return None

# ----------------------
# Reservation véhicule
# ----------------------
def reservation_Vehicule(passer_Question=False, arguments=[]):
    os.system('cls')
    if not passer_Question:
        print("Vous allez réserver un véhicule, veuillez répondre aux questions suivantes")
        id_Client = input("Quel est votre id client ?\n")
        if not id_Client.isdigit() :
            play_sound_async("Windows_7_critical_stop.wav")
            print("Id Client invalide")
            input()
            return
        id_Client = int(id_Client)
        id_Vehicule = input("Quel est l'id du véhicule que vous souhaitez réserver ?\n")
        if not id_Vehicule.isdigit() :
            play_sound_async("Windows_7_critical_stop.wav")
            print("Id Vehicule invalide")
            input()
            return
        id_Vehicule = int(id_Vehicule)
        date_Reservation = input("Quand voulez-vous cette voiture ? (dd/mm/yy)\n")
        duree = input("Pour combien de jours voulez-vous ce véhicule ?\n")
        if not duree.isdigit() :
            play_sound_async("Windows_7_critical_stop.wav")
            print("La durée saise est invalide")
            input()
            return
        duree = int(duree)
    else:
        id_Client = arguments[0]
        id_Vehicule = arguments[1]
        date_Reservation = arguments[2]
        duree = arguments[3]
    
    index_Client = trouver_Client_Par_Id(id_Client)
    if index_Client == None :
        return

    liste_Client[index_Client].reserver_Vehicule(id_Vehicule, date_Reservation, duree)

    if not passer_Question :
        input()
    return

# ----------------------
# Affichage des clients et véhicules
# ----------------------
def afficher_Client():
    os.system('cls')
    print(f"{'Id':<5} | {'Nom':<20} | {'Prénom':<20} | {'Âge':<3} | {'Permis':<6} | {'Profit':<9} |")
    print("======+======================+======================+=====+========+===========+")
    for c in liste_Client:
        print(f"{c.id:<5} | {c.first_Name:<20} | {c.last_Name:<20} | {c.age:<3} | {c.licence:<6} | {c.profit:<8}€ |")
    print("======+======================+======================+=====+========+===========+")
    input()
    return

def afficher_Vehicule():
    os.system('cls')

    profit_Total = 0

    print(f"{'Id':<5} | {'Marque':<15} | {'Modèle':<25} | {'Catégorie':<10} | {'Tarif':<5} | {'Etat':<10} | {'Profit':<8} |")
    print("======+=================+===========================+============+=======+============+==========+")
    for v in liste_Vehicule:
        print(f"{v.id:<5} | {v.brand:<15} | {v.model:<25} | {v.category:<10} | {v.tarif:<4}€ | {v.state:<10} | {v.profit:<7}€ |")
        profit_Total += v.profit
    print("======+=================+===========================+============+=======+============+==========+")
    print(f"Profit total : {profit_Total}€")
    print(f"Nombre de véhicule : {len(liste_Vehicule)}")
    print(f"Profit moyen par véhicule : {int((profit_Total/len(liste_Vehicule)))}€")
    input()
    return

def renseignement_Client():
    os.system('cls')
    id_Client = int(input("Quel est l'ID du client qui vous intéresse ?\n"))
    index_Client = trouver_Client_Par_Id(id_Client)
    if index_Client == None :
        return
    liste_Client[index_Client].historique()
    input()
    return

def renseignement_Vehicule() :
    os.system('cls')
    id_Vehicule = int(input("Quel est l'ID du véhicule qui vous intéresse ?\n"))
    index_Vehicule = trouver_Vehicule_Par_Id(id_Vehicule)
    if index_Vehicule == None :
        return
    liste_Vehicule[index_Vehicule].historique()
    input()
    return

# ----------------------
# Fonction Graphique et Sonore
# ----------------------

def play_sound_async(sound_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(base_path, sound_name)
    winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

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

def simuler_Activite():
    reservation_Vehicule(True, [1, 1, "05/01/25", 4])
    reservation_Vehicule(True, [3, 1, "10/01/25", 6])
    reservation_Vehicule(True, [5, 1, "18/01/25", 3])
    reservation_Vehicule(True, [2, 2, "03/01/25", 7])
    reservation_Vehicule(True, [4, 2, "12/01/25", 5])
    reservation_Vehicule(True, [6, 2, "16/01/25", 10])
    reservation_Vehicule(True, [7, 3, "01/02/25", 4])
    reservation_Vehicule(True, [8, 3, "06/02/25", 6])
    reservation_Vehicule(True, [10, 3, "15/02/25", 8])
    reservation_Vehicule(True, [9, 4, "22/01/25", 5])
    reservation_Vehicule(True, [11, 4, "28/01/25", 4])
    reservation_Vehicule(True, [12, 4, "05/02/25", 6])
    reservation_Vehicule(True, [4, 5, "10/02/25", 3])
    reservation_Vehicule(True, [1, 5, "13/02/25", 12])
    reservation_Vehicule(True, [8, 5, "28/02/25", 4])
    reservation_Vehicule(True, [6, 6, "02/03/25", 7])
    reservation_Vehicule(True, [7, 6, "10/03/25", 5])
    reservation_Vehicule(True, [3, 6, "18/03/25", 6])
    reservation_Vehicule(True, [10, 7, "05/03/25", 9])
    reservation_Vehicule(True, [11, 7, "16/03/25", 4])
    reservation_Vehicule(True, [12, 7, "22/03/25", 7])
    reservation_Vehicule(True, [1, 8, "01/04/25", 10])
    reservation_Vehicule(True, [2, 8, "15/04/25", 5])
    reservation_Vehicule(True, [5, 8, "22/04/25", 4])
    reservation_Vehicule(True, [3, 9, "03/04/25", 8])
    reservation_Vehicule(True, [6, 9, "13/04/25", 6])
    reservation_Vehicule(True, [9, 9, "20/04/25", 10])
    reservation_Vehicule(True, [4, 10, "07/05/25", 3])
    reservation_Vehicule(True, [7, 10, "10/05/25", 8])
    reservation_Vehicule(True, [8, 10, "19/05/25", 5])
    reservation_Vehicule(True, [11, 11, "01/05/25", 7])
    reservation_Vehicule(True, [12, 11, "10/05/25", 6])
    reservation_Vehicule(True, [10, 11, "18/05/25", 9])
    reservation_Vehicule(True, [5, 1, "01/06/25", 12])
    reservation_Vehicule(True, [7, 2, "04/06/25", 11])
    reservation_Vehicule(True, [9, 3, "06/06/25", 5])
    reservation_Vehicule(True, [11, 4, "08/06/25", 9])
    reservation_Vehicule(True, [1, 5, "10/06/25", 7])
    reservation_Vehicule(True, [3, 6, "11/06/25", 3])
    reservation_Vehicule(True, [6, 7, "12/06/25", 4])
    reservation_Vehicule(True, [8, 8, "15/06/25", 10])
    reservation_Vehicule(True, [10, 9, "17/06/25", 6])
    reservation_Vehicule(True, [12, 10, "19/06/25", 8])
    reservation_Vehicule(True, [2, 11, "21/06/25", 9])
    reservation_Vehicule(True, [4, 1, "01/07/25", 4])
    reservation_Vehicule(True, [6, 2, "04/07/25", 3])
    reservation_Vehicule(True, [8, 3, "07/07/25", 7])
    reservation_Vehicule(True, [10, 4, "10/07/25", 2])
    reservation_Vehicule(True, [12, 5, "12/07/25", 10])
    reservation_Vehicule(True, [1, 6, "14/07/25", 6])
    reservation_Vehicule(True, [3, 7, "16/07/25", 4])
    reservation_Vehicule(True, [5, 8, "18/07/25", 3])
    reservation_Vehicule(True, [7, 9, "21/07/25", 9])
    reservation_Vehicule(True, [9, 10, "23/07/25", 5])
    reservation_Vehicule(True, [11, 11, "26/07/25", 8])
    reservation_Vehicule(True, [2, 3, "01/08/25", 6])
    reservation_Vehicule(True, [4, 4, "04/08/25", 3])
    reservation_Vehicule(True, [6, 5, "06/08/25", 10])
    reservation_Vehicule(True, [8, 6, "09/08/25", 6])
    reservation_Vehicule(True, [10, 7, "12/08/25", 4])
    reservation_Vehicule(True, [12, 8, "14/08/25", 12])
    reservation_Vehicule(True, [1, 9, "17/08/25", 8])
    reservation_Vehicule(True, [3, 10, "20/08/25", 3])
    reservation_Vehicule(True, [5, 11, "23/08/25", 9])
    reservation_Vehicule(True, [15, 14, "04/01/26", 4])
    reservation_Vehicule(True, [16, 15, "05/01/26", 7])
    reservation_Vehicule(True, [17, 16, "06/01/26", 3])
    reservation_Vehicule(True, [18, 17, "07/01/26", 5])
    reservation_Vehicule(True, [19, 18, "08/01/26", 2])
    reservation_Vehicule(True, [20, 19, "10/01/26", 6])
    reservation_Vehicule(True, [21, 20, "11/01/26", 4])
    reservation_Vehicule(True, [22, 21, "12/01/26", 3])
    reservation_Vehicule(True, [23, 22, "13/01/26", 8])
    reservation_Vehicule(True, [24, 23, "14/01/26", 5])
    reservation_Vehicule(True, [25, 24, "16/01/26", 7])
    reservation_Vehicule(True, [26, 25, "17/01/26", 2])
    reservation_Vehicule(True, [27, 14, "20/01/26", 5])
    reservation_Vehicule(True, [28, 15, "21/01/26", 3])
    reservation_Vehicule(True, [29, 16, "22/01/26", 4]) 
    reservation_Vehicule(True, [15, 17, "23/01/26", 6])
    reservation_Vehicule(True, [16, 18, "24/01/26", 4])
    reservation_Vehicule(True, [17, 19, "25/01/26", 3])
    reservation_Vehicule(True, [18, 20, "26/01/26", 7])
    reservation_Vehicule(True, [19, 21, "27/01/26", 2])
    reservation_Vehicule(True, [20, 22, "01/02/26", 4])
    reservation_Vehicule(True, [21, 23, "02/02/26", 5])
    reservation_Vehicule(True, [22, 24, "03/02/26", 6])
    reservation_Vehicule(True, [23, 25, "04/02/26", 3])
    reservation_Vehicule(True, [24, 14, "05/02/26", 7])

def afficher_Menu():
    print("\n========================= MENU ===========================")
    print("1 - Créer un client")
    print("2 - Créer un véhicule")
    print("3 - Emprunter une voiture")
    print("4 - Afficher tout les clients")
    print("5 - Afficher tout les véhicules")
    print("6 - Renseignement sur un client précis")
    print("7 - Renseignement sur un véhicule précis")
    print("0 - Quitter")
    print("==========================================================\n")


# ----------------------
# Boucle principale
# ----------------------

activer_Session()

simuler_Activite()

entree = "999"

while entree != "0":
    os.system('cls')
    afficher_Menu()
    entree = input("Que souhaitez-vous faire ?\n")
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
    elif entree == "6" :
        play_sound_async("Mouse_Click.wav")
        renseignement_Client()
    elif entree == "7":
        play_sound_async("Mouse_Click.wav")
        renseignement_Vehicule()
