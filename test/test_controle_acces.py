import pytest
from moteur_ouverture import MoteurOuverture
from utilities.porteSpy import PorteSpy
from utilities.lecteurFake import LecteurFake

## Cas nominal 
def test_lecteur_detecte_badge_et_ouvre_porte():
# ETANT DONNE une porte reliée à un lecteur, ayant détecté un badge
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()

    lecteur_fake.simuler_detection_badge()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
# QUAND le Moteur d'ouverture effectue une interrogation des lecteurs
    moteur_ouverture.interroger()
# ALORS le signal d'ouverture est envoyé à la porte
    assert porte_spy.porte_ouverte


## Cas d'erreur
def test_lecteur_non_detecte_badge_et_ne_pas_ouvrir_porte():
# ETANT DONNE une porte reliée à un lecteur, n'ayant pas détecté de badge
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
# QUAND le Moteur d'ouverture effectue une interrogation des lecteurs
    moteur_ouverture.interroger()
# ALORS le signal d'ouverture n'est pas envoyé à la porte
    assert not porte_spy.porte_ouverte

## Cas deux portes
def test_deux_portes_un_seul_lecteur_detecte_badge():
    # ETANT DONNE un Lecteur ayant détecté un Badge
    # ET un autre Lecteur n'ayant rien détecté
    # ET une Porte reliée chacune à un Lecteur
    porte_spy1 = PorteSpy()
    porte_spy2 = PorteSpy()

    lecteur_fake = LecteurFake()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy1)

    lecteur_fake.simuler_detection_badge()
    # QUAND le Moteur d'ouverture effectue une interrogation des lecteurs
    moteur_ouverture.interroger()
    # ALORS la première porte est ouverte
    # ET la deuxième porte reste fermée
    assert porte_spy1.porte_ouverte
    assert not porte_spy2.porte_ouverte