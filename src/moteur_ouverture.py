from porte import Porte
from lecteur_carte import LecteurCarte
from badge import Badge

class MoteurOuverture:
    def __init__(self):
        self.associations = {}
        self.liste_noire_badges = []

    def associer(self, lecteur: LecteurCarte, porte: Porte):
        self.associations[lecteur] = porte

    def interroger(self):
        for lecteur, porte in self.associations.items():
            if lecteur.badge_detecte:
                if not self.badge_est_bloque(lecteur.badge):
                    porte.ouvrir()
                    lecteur.reset()

    def bloquer_badge(self, badge):
        print("blocage du badge ", badge)
        if badge not in self.liste_noire_badges:
            self.liste_noire_badges.append(badge)
            print("badge bloqué : ", badge)

    def badge_est_bloque(self, badge):
        print("vérification liste noire pour le badge ", badge)
        if badge in self.liste_noire_badges:
            print("le badge est sur la liste noire")
            return True
        print("le badge n'est pas sur la liste noire")
        return False
