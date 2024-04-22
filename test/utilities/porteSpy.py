
from porte import Porte

class PorteSpy (Porte):
    def __init__(self):
        super().__init__()
        self.porte_ouverte = False

    def ouvrir(self):
        self.porte_ouverte = True