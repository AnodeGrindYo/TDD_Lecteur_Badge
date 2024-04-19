from porte import Porte
from lecteur_carte import LecteurCarte

class MoteurOuverture:
    def __init__(self):
        self.associations = {}

    def associer(self, lecteur: LecteurCarte, porte: Porte):
        if not isinstance(lecteur, LecteurCarte):
            raise TypeError("Le lecteur doit être une instance de LecteurCarte")
        if not isinstance(porte, Porte):
            raise TypeError("La porte doit être une instance de Porte")
        self.associations[lecteur] = porte

    def interroger(self):
        for lecteur, porte in self.associations.items():
            if lecteur.badges_detecte:
                porte.ouvrir()
