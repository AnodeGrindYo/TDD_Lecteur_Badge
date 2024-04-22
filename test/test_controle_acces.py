import pytest
from src.moteur_ouverture import MoteurOuverture
from utilities.porteSpy import PorteSpy
from utilities.lecteurFake import LecteurFake

## Cas nominal 
def lecteur_detecte_badge_et_ouvre_porte():
# ETANT DONNE une porte reliée à un lecteur, ayant détecté un badge
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()

    lecteur_fake.simuler_detection_badge()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(porte_spy, lecteur_fake)
# QUAND le Moteur d'ouverture effectue une interrogation des lecteurs
    moteur_ouverture.interroger()
# ALORS le signal d'ouverture est envoyé à la porte
    assert porte_spy.ouverte