class Contrat:
    def __init__(self, numero, date, client, montantContrat, interventions):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = interventions
        self.nbIntervention = len(interventions)

    def montant(self):
        return self.montantContrat

    def ecart(self):
        cout_total = sum([intervention.fraisKm(intervention.client.distance()) + intervention.fraisMo() for intervention in self.interventions])
        return cout_total - self.montantContrat
