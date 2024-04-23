from lecteur_carte import LecteurCarte
import time
import pyttsx3

class LecteurFake (LecteurCarte):
    def __init__(self):
        super().__init__()
        self.badge_detecte = False
        self.badge = None
        self.bip_amount = 0
        self.flash_invocations = []
        self.initialize_biper()

    def initialize_biper(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices') 
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 350)

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

    def flash(self, r: bool, v: bool, b: bool):
        self.flash_invocations.append((r,v, b))

    def compter_rouge(self):
        return self.flash_invocations.count((True, False, False))

    def compter_vert(self):
        return self.flash_invocations.count((False, True, False))
    
    def compter_violet(self):
        return self.flash_invocations.count((True, False, True))
            
