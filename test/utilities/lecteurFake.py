from lecteur_carte import LecteurCarte
import winsound
import time

class LecteurFake (LecteurCarte):
    def __init__(self):
        super().__init__()
        self.badge_detecte = False
        self.badge = None
        self.bip_amount = 0

    def simuler_detection_badge(self, badge):
        self.badge_detecte = True
        self.badge = badge

    def reset(self):
        self.badge_detecte = False
        self.badge = None

    def bip(self, authorized=False):
        self.bip_amount = 0
        if authorized:
            winsound.Beep(880, 125)
            self.bip_amount = 1
        else:
            winsound.Beep(880, 125)
            # attendre 500ms
            time.sleep(0.25)
            winsound.Beep(784, 125)
            self.bip_amount = 2
