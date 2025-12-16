# Vehicule.py

class Vehicule:
    _compteur_Vehicule = 0

    def __init__(self, brand: str, model: str, category: str, tarif: int, state: str):
        Vehicule._compteur_Vehicule += 1
        self.id = Vehicule._compteur_Vehicule
        self.brand = brand
        self.model = model
        self.category = category
        self.tarif = tarif
        self.state = state
        self.historic = {}
        self.profit = 0

    def historique(self, liste_Client, trouver_Client_Par_Id):
        print(f"Historique des réservations pour {self.brand} {self.model}:")
        print("+==========+===============+===========+================================+=========+")
        print(f"| {'Date':<8} | {'Durée (jours)':<13} | {'ID Client':<9} | {'Nom & Prénom Client':<30} | {'Profit':<7} |")
        print("+==========+===============+===========+================================+=========+")
        for d, info in self.historic.items():
            id_client = info["client_Id"]
            index_Client = trouver_Client_Par_Id(id_client)
            client = liste_Client[index_Client]
            nom = client.first_Name + " " + client.last_Name
            prix = self.tarif * info['duree']
            print(f"| {d:<8} | {info['duree']:<13} | {id_client:<9} | {nom:<30} | {prix:<6}€ |")
        print("+==========+===============+===========+================================+=========+")
        nbr_Emprunts = len(self.historic)
        print(f"Ce véhicule a fait un profit total de {self.profit}€")
        print(f"Il fait en moyenne {int(self.profit/nbr_Emprunts)}€ par emprunt")
