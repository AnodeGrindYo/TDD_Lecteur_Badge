from porte import Porte
from lecteur_carte import LecteurCarte

class MoteurOuverture:
    def __init__(self):
        self.associations = {}

    def associer(self, lecteur: LecteurCarte, porte: Porte):
        self.associations[lecteur] = porte

    def interroger(self):
        for lecteur, porte in self.associations.items():
            if lecteur.badge_detecte:
                porte.ouvrir()
