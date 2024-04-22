from lecteur_carte import LecteurCarte

class LecteurFake (LecteurCarte):
    def __init__(self):
        super().__init__()
        self.badge_detecte = False
        self.badge = None

    def simuler_detection_badge(self, badge):
        self.badge_detecte = True
        self.badge = badge

    def reset(self):
        self.badge_detecte = False
        self.badge = None