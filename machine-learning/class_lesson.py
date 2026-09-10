class Forfait:
    def __init__(self,prix):
        self.prix = prix
        
    def description(self):
        return f"Forfait à {self.prix}Ar"
        
class ForfaitJournalier(Forfait):
    def __init__(self, prix,duree_heure=24):
        super().__init__(prix)
        self.duree_heure = duree_heure

    def description(self):
        return f"{super().description()} - valable {self.duree_heure}h"
    
class ForfaitHebdomadaire(Forfait):
    def description(self):
        return f"Forfait hebdo à {self.prix} Ar"

forfait = [ForfaitJournalier(2500),ForfaitHebdomadaire(10000)]

for f in forfait:
    print(f.description())
    
