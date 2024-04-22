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

    def bip_rising(self):
        frequency = 37
        while True:
            while frequency < 32767:
                winsound.Beep(frequency, 100)
                frequency += 100
                time.sleep(0.00125)
            while frequency > 37:
                winsound.Beep(frequency, 100)
                frequency -= 100
                time.sleep(0.00125)
