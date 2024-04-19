
class LecteurFake:
    def __init__(self):
        self.badge_detecte = False

    def simuler_detection_badge(self):
        self.badge_detecte = True