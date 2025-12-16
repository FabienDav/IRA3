# application_Data.py
from Customer import Customer
from Vehicule import Vehicule
import winsound
import os
import json

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

def trouver_Client_Par_Id(id: int):
    for j, client in enumerate(liste_Client):
        if client.id == id:
            return j
    print("Id client non trouvé")
    return None

def trouver_Vehicule_Par_Id(id: int):
    for j, vehicule in enumerate(liste_Vehicule):
        if vehicule.id == id:
            return j
    print("Id véhicule non trouvé")
    return None

def play_sound_async(sound_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(base_path, sound_name)
    winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def simuler_Activite():
    # Janvier 2025 (15 réservations)
    liste_Client[0].reserver_Vehicule(1, "02/01/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[1].reserver_Vehicule(2, "03/01/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[2].reserver_Vehicule(3, "05/01/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[3].reserver_Vehicule(4, "07/01/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[5].reserver_Vehicule(5, "10/01/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[6].reserver_Vehicule(6, "12/01/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[7].reserver_Vehicule(7, "15/01/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[8].reserver_Vehicule(8, "17/01/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[9].reserver_Vehicule(9, "20/01/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[10].reserver_Vehicule(10, "22/01/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[11].reserver_Vehicule(11, "24/01/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[12].reserver_Vehicule(12, "26/01/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[13].reserver_Vehicule(13, "28/01/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[14].reserver_Vehicule(14, "30/01/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[15].reserver_Vehicule(15, "31/01/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)

    # Février 2025 (15)
    liste_Client[16].reserver_Vehicule(16, "02/02/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[17].reserver_Vehicule(17, "04/02/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[18].reserver_Vehicule(18, "06/02/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[19].reserver_Vehicule(19, "08/02/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[20].reserver_Vehicule(20, "10/02/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[21].reserver_Vehicule(21, "12/02/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[22].reserver_Vehicule(22, "14/02/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[23].reserver_Vehicule(23, "16/02/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[24].reserver_Vehicule(24, "18/02/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[25].reserver_Vehicule(25, "20/02/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[26].reserver_Vehicule(1, "22/02/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[27].reserver_Vehicule(2, "24/02/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[28].reserver_Vehicule(3, "25/02/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[29].reserver_Vehicule(4, "27/02/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[0].reserver_Vehicule(5, "28/02/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)

    # Mars 2025 (15)
    liste_Client[1].reserver_Vehicule(6, "02/03/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[2].reserver_Vehicule(7, "04/03/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[3].reserver_Vehicule(8, "06/03/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[5].reserver_Vehicule(9, "08/03/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[6].reserver_Vehicule(10, "10/03/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[7].reserver_Vehicule(11, "12/03/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[8].reserver_Vehicule(12, "14/03/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[9].reserver_Vehicule(13, "16/03/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[10].reserver_Vehicule(14, "18/03/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[11].reserver_Vehicule(15, "20/03/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[12].reserver_Vehicule(16, "22/03/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[13].reserver_Vehicule(17, "24/03/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[14].reserver_Vehicule(18, "26/03/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[15].reserver_Vehicule(19, "28/03/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
    liste_Client[16].reserver_Vehicule(20, "30/03/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)


# ----------------------
# Préchargement des données
# ----------------------

liste_Client[0].reserver_Vehicule(1, "01/01/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
liste_Client[1].reserver_Vehicule(2, "03/01/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)
liste_Client[2].reserver_Vehicule(3, "10/01/25", 6, liste_Vehicule, trouver_Vehicule_Par_Id)
liste_Client[3].reserver_Vehicule(4, "05/01/25", 3, liste_Vehicule, trouver_Vehicule_Par_Id)
liste_Client[0].reserver_Vehicule(2, "15/01/25", 5, liste_Vehicule, trouver_Vehicule_Par_Id)
liste_Client[1].reserver_Vehicule(1, "20/01/25", 4, liste_Vehicule, trouver_Vehicule_Par_Id)

# ======================
# Persistance des données en JSON
# ======================

CLIENTS_JSON = "clients.json"
VEHICULES_JSON = "vehicules.json"


def sauvegarder_Donnees():
    """Sauvegarde clients, véhicules et historiques en JSON"""

    clients_data = []
    for c in liste_Client:
        clients_data.append({
            "id": c.id,
            "first_Name": c.first_Name,
            "last_Name": c.last_Name,
            "age": c.age,
            "licence": c.licence,
            "historic": c.historic,
            "profit": c.profit
        })

    vehicules_data = []
    for v in liste_Vehicule:
        vehicules_data.append({
            "id": v.id,
            "brand": v.brand,
            "model": v.model,
            "category": v.category,
            "tarif": v.tarif,
            "state": v.state,
            "historic": v.historic,
            "profit": v.profit
        })

    with open(CLIENTS_JSON, "w", encoding="utf-8") as f:
        json.dump(clients_data, f, indent=4)

    with open(VEHICULES_JSON, "w", encoding="utf-8") as f:
        json.dump(vehicules_data, f, indent=4)



def charger_Donnees():
    """Charge les données depuis les fichiers JSON si existants"""

    global liste_Client, liste_Vehicule

    if os.path.exists(CLIENTS_JSON) and os.path.exists(VEHICULES_JSON):

        with open(CLIENTS_JSON, "r", encoding="utf-8") as f:
            clients_data = json.load(f)

        with open(VEHICULES_JSON, "r", encoding="utf-8") as f:
            vehicules_data = json.load(f)

        liste_Client.clear()
        liste_Vehicule.clear()

        # Recréation véhicules (important pour les ID)
        for v in vehicules_data:
            veh = Vehicule(v["brand"], v["model"], v["category"], v["tarif"], v["state"])
            veh.id = v["id"]
            veh.historic = v["historic"]
            veh.profit = v["profit"]
            liste_Vehicule.append(veh)

        # Recréation clients
        for c in clients_data:
            cli = Customer(c["first_Name"], c["last_Name"], c["age"], c["licence"])
            cli.id = c["id"]
            cli.historic = c["historic"]
            cli.profit = c["profit"]
            liste_Client.append(cli)

        # Réajustement des compteurs statiques
        Customer._compteur_Customer = max(c.id for c in liste_Client)
        Vehicule._compteur_Vehicule = max(v.id for v in liste_Vehicule)

        return True

    return False
