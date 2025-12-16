# Customer.py
from datetime import datetime, timedelta

class Customer:
    _compteur_Customer = 0

    def __init__(self, first_Name, last_Name, age, licence=False):
        Customer._compteur_Customer += 1
        self.id = Customer._compteur_Customer
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.age = int(age)
        self.licence = licence
        self.historic = {}
        self.profit = 0

    def reserver_Vehicule(self, id_Vehicule, date_Reservation, duree,
                          liste_Vehicule, trouver_Vehicule_Par_Id):

        index_Vehicule = trouver_Vehicule_Par_Id(id_Vehicule)
        if index_Vehicule is None:
            return

        if self.age < 17:
            print("Le client est trop jeune pour conduire")
            return
        if not self.licence:
            print("Le client n'a pas de permis de conduire")
            return

        date_format = "%d/%m/%y"
        date_debut = datetime.strptime(date_Reservation, date_format)
        date_fin = date_debut + timedelta(days=duree)

        vehicule = liste_Vehicule[index_Vehicule]

        for d, info in vehicule.historic.items():
            ancien_debut = datetime.strptime(d, date_format)
            ancien_fin = ancien_debut + timedelta(days=info["duree"])
            if date_debut < ancien_fin and date_fin > ancien_debut:
                print("Le véhicule n'est pas disponible à ces dates")
                return

        self.historic[date_Reservation] = {
            "vehicule_Id": id_Vehicule,
            "category": vehicule.category,
            "duree": duree
        }

        vehicule.historic[date_Reservation] = {
            "client_Id": self.id,
            "duree": duree
        }

        cout = vehicule.tarif * duree
        vehicule.profit += cout
        self.profit += cout

        print(f"Véhicule réservé – coût : {cout}€")

    def historique(self, liste_Vehicule, trouver_Vehicule_Par_Id):
        profit_Total = 0
        print(f"Historique des réservations pour {self.first_Name} {self.last_Name}")
        print("+=======+==========================================+============+==========+===============+=========+")
        print(f"| {'Id':<5} | {'Véhicule':<40} | {'Catégorie':<10} | {'Début':<8} | {'Durée (jours)':<13} | {'Coût':<7} |")
        print("+=======+==========================================+============+==========+===============+=========+")
        for d, info in self.historic.items():
            index_Vehicule = trouver_Vehicule_Par_Id(info["vehicule_Id"])
            vehicule = liste_Vehicule[index_Vehicule]
            nom_vehicule = vehicule.brand + " " + vehicule.model

            prix = vehicule.tarif * info['duree']
            profit_Total += prix
            print(f"| {vehicule.id:<5} | {nom_vehicule:<40} | {vehicule.category:<10} | {d:<8} | {info['duree']:<13} | {prix:<6}€ |")
        print("+=======+==========================================+============+==========+===============+=========+")
        print(f"Cette personne a dépensée {profit_Total}€")
