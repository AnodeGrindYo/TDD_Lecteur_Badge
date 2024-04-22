from lecteur_carte import LecteurCarte
import time
import pyttsx3

class LecteurFake (LecteurCarte):
    def __init__(self):
        super().__init__()
        self.badge_detecte = False
        self.badge = None
        self.bip_amount = 0
        self.initialize_biper()

    def initialize_biper(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices') 
        self.engine.setProperty('voice', voices[1].id)

    def simuler_detection_badge(self, badge):
        self.badge_detecte = True
        self.badge = badge

    def reset(self):
        self.badge_detecte = False
        self.badge = None

    def bip(self, authorized=False):
        self.bip_amount = 0
        if authorized:
            self.engine.say("BEEP !")
            self.engine.runAndWait()
            self.bip_amount = 1
        else:
            self.engine.say("BEEP-BEEP !")
            self.engine.runAndWait()
            self.bip_amount = 2
