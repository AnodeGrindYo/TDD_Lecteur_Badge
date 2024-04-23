from porteSpy import PorteSpy

class PorteDummy(PorteSpy):
    def __init__(self):
        super().__init__()

    def ouvrir(self):
        raise 666