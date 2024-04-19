
class LecteurCarte:
    def __init__(self):
        self.badge_autorise = "123456789"

    def presenter_badge(self, badge):
        if badge.identifiant == self.badge_autorise:
            return True
        else:
            return False