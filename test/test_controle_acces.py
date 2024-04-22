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

## Cas aucune interrogation
def test_aucune_interrogation():
# ETANT DONNE une porte reliée à un lecteur
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
# QUAND le Moteur d'ouverture n'effectue pas d'interrogation des lecteurs
# ALORS le signal d'ouverture n'est pas envoyé à la porte
    assert not porte_spy.porte_ouverte

## Cas non badgé
def test_non_badge():
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

## Cas deux portes, mais c'est le deuxième lecteur qui détecte le badge
def test_deux_portes_un_seul_lecteur_detecte_badge_inverse():
    # ETANT DONNE un Lecteur ayant détecté un Badge
    # ET un autre Lecteur n'ayant rien détecté
    # ET une Porte reliée chacune à un Lecteur
    porte_spy1 = PorteSpy()
    porte_spy2 = PorteSpy()

    lecteur_fake1 = LecteurFake()
    lecteur_fake2 = LecteurFake()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake1, porte_spy1)
    moteur_ouverture.associer(lecteur_fake2, porte_spy2)

    lecteur_fake2.simuler_detection_badge()
    # QUAND le Moteur d'ouverture effectue une interrogation des lecteurs
    moteur_ouverture.interroger()
    # ALORS la première porte est ouverte
    # ET la deuxième porte reste fermée
    assert not porte_spy1.porte_ouverte
    assert porte_spy2.porte_ouverte

## Cas deux portes, deux lecteurs, deux badges
def test_deux_portes_deux_lecteurs_deux_badges():
    # ETANT DONNE un Lecteur ayant détecté un Badge
    # ET un autre Lecteur ayant détecté un Badge
    # ET une Porte reliée chacune à un Lecteur
    porte_spy1 = PorteSpy()
    porte_spy2 = PorteSpy()

    lecteur_fake1 = LecteurFake()
    lecteur_fake2 = LecteurFake()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake1, porte_spy1)
    moteur_ouverture.associer(lecteur_fake2, porte_spy2)

    lecteur_fake1.simuler_detection_badge()
    lecteur_fake2.simuler_detection_badge()
    # QUAND le Moteur d'ouverture effectue une interrogation des lecteurs
    moteur_ouverture.interroger()
    # ALORS la première porte est ouverte
    # ET la deuxième porte est ouverte
    assert porte_spy1.porte_ouverte
    assert porte_spy2.porte_ouverte