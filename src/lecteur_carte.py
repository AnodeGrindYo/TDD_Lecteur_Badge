
class LecteurCarte:
    def __init__(self):
        self.badge_autorise = None
        self.acces_autorise = False

    def presenter_badge(self, badge):
        if badge.identifiant == self.badge_autorise:
            self.acces_autorise = True
        else:
            self.acces_autorise = False