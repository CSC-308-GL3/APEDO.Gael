
from datetime import datetime

class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = datetime.strptime(dateEmbauche, "%d/%m/%Y").date()
    
    def coutHoraire(self):
        anciennete = self.getAnciennete()
        taux = self.qualification.tauxHoraire()
        if anciennete <= 5:
            coefficient = 1.0
        elif anciennete <= 10:
            coefficient = 1.05
        elif anciennete <= 15:
            coefficient = 1.08
        else:
            coefficient = 1.12
        return round(taux * coefficient, 2)
    
    def getNumero(self):
        return self.numero
    
    def getNom(self):
        return self.nom
    
    def getQualification(self):
        return self.qualification
    
    def getDateEmbauche(self):
        return self.dateEmbauche
    
    def getAnciennete(self):
        today = datetime.today().date()
        return today.year - self.dateEmbauche.year - ((today.month, today.day) < (self.dateEmbauche.month, self.dateEmbauche.day))
