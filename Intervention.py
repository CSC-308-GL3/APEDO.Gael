from datetime import datetime


class Intervention:
    def __init__(self, numero, date, duree, tarifKm, technicien):
        self.numero = numero
        self.date = datetime.strptime(date, "%d/%m/%Y").date()
        self.duree = duree
        self.tarifKm = tarifKm
        self.technicien = technicien
    
    def affiche(self):
        print("Intervention n°{} du {} :".format(self.numero, self.date.strftime("%d/%m/%Y")))
        print("- Durée : {} heures".format(self.duree))
        print("- Frais kilométriques : {} €".format(self.fraisKm()))
        print("- Frais de main-d'oeuvre : {} €".format(self.fraisMo()))
        print("Technicien :")
        print("- Nom : {}".format(self.technicien.getNom()))
        print("- Qualification : {}".format(self.technicien.getQualification().getLibelle()))
        print("- Coût horaire : {} €".format(self.technicien.coutHoraire()))
    


    def fraisKm(self, dist):
        return self.tarifkm * dist

    def fraisMo(self):
        return self.technicien.coutHoraire() * self.duree