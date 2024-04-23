
from porte import Porte

class PorteSpy (Porte):
    def __init__(self):
        super().__init__()
        self.porte_ouverte = False
        self.exception_code = 1
    
    def set_exception_code(self, exception_code):
        self.exception_code = exception_code

    def ouvrir(self):
        self.porte_ouverte = True
        return self.exception_code

    def fermer(self):
        self.porte_ouverte = False