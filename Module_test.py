# Importer les classes nécessaires
from Employe import Employe
from Intervention import Intervention

# Définir un jeu de données pour un employé
employe = Employe( 1, "Jean Dupont", "jdupont@example.com", "01/01/2019")
employe.montant_contrat = 1000.0

# Définir des jeux de données pour les interventions
interventions = [
    Intervention(1, "01/01/2023", "1h", 500.0, "ama"),
    Intervention(2,  "04/08/2013", "4h", 300.0, "koffi"),
    Intervention(3,  "03/04/2027", "10h", 700.0, "zglo")
]

# Calculer le coût total des interventions
total = sum([intervention.numero for intervention in interventions])

# Afficher l'écart entre le montant du contrat et le coût total des interventions
ecart = employe.montant_contrat - total
print(f"L'écart entre le montant du contrat et le coût total des interventions est de {ecart} euros.")
