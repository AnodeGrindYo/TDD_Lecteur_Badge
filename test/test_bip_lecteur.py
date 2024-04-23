import pytest
from moteur_ouverture import MoteurOuverture
from utilities.porteSpy import PorteSpy
from utilities.lecteurFake import LecteurFake
from badge import Badge

PorteTest = PorteSpy
LecteurTest = LecteurFake

## Cas teste si le lecteur bip une fois quand le badge est autorisé
def test_lecteur_bip_une_fois_si_badge_autorisé():
    # ETANT DONNE un lecteur associé à une porte
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    # ET que le badge est autorisé
    badge = Badge()
    # QUAND le badge est présenté au lecteur
    lecteur_fake.simuler_detection_badge(badge)
    moteur_ouverture.interroger()
    # ALORS le lecteur émet un bip
    assert lecteur_fake.bip_amount == 1

def test_lecteur_bip_deux_fois_si_badge_autorisé():
    # ETANT DONNE un lecteur associé à une porte
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    # ET que le badge est autorisé
    badge = Badge()
    moteur_ouverture.bloquer_badge(badge)
    # QUAND le badge est présenté au lecteur
    lecteur_fake.simuler_detection_badge(badge)
    moteur_ouverture.interroger()
    # ALORS le lecteur émet un bip
    assert lecteur_fake.bip_amount == 2

def test_lecteur_ne_bip_pas_si_aucun_badge_presente():
    # ETANT DONNE un lecteur associé à une porte
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    # QUAND aucun badge n'est présenté au lecteur
    moteur_ouverture.interroger()
    # ALORS le lecteur n'émet pas de bip
    assert lecteur_fake.bip_amount == 0
