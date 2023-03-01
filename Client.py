class Client:
    def __init__(self, numero, nom, adresse, codePostal, ville, nbKm):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostal = codePostal
        self.ville = ville
        self.nbKm = nbKm

    def distance(self):
        return self.nbKm