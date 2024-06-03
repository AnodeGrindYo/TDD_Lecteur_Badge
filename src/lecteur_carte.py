from badge import Badge

class LecteurCarte:
    def __init__(self):
        self.badge_detecte = False
        self.badge = None

    def presenter_badge(self, badge: Badge):
        print("badge detecté : ")
        self.badge_detecte = True
        self.badge = badge

    def reset(self):
        self.badge_detecte = False
        self.badge = None