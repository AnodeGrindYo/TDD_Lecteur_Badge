import pytest
from moteur_ouverture import MoteurOuverture
from utilities.porteSpy import PorteSpy
from utilities.lecteurFake import LecteurFake
from badge import Badge

PorteTest = PorteSpy
LecteurTest = LecteurFake

## Cas nominal 
def test_lecteur_detecte_badge_et_ouvre_porte():
    # ETANT DONNE une porte reliée à un lecteur, ayant détecté un badge
    porte_spy = PorteTest()
    lecteur_fake = LecteurTest()

    badge = Badge()

    lecteur_fake.simuler_detection_badge(badge)

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


## Cas deux portes
def test_deux_portes_un_seul_lecteur_detecte_badge():
    # ETANT DONNE un Lecteur ayant détecté un Badge
    # ET un autre Lecteur n'ayant rien détecté
    # ET une Porte reliée chacune à un Lecteur
    porte_spy1 = PorteSpy()
    porte_spy2 = PorteSpy()

    lecteur_fake = LecteurFake()

    badge = Badge()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy1)

    lecteur_fake.simuler_detection_badge(badge)
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

    badge = Badge()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake1, porte_spy1)
    moteur_ouverture.associer(lecteur_fake2, porte_spy2)

    lecteur_fake2.simuler_detection_badge(badge)
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

    badge1 = Badge()
    badge2 = Badge()

    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake1, porte_spy1)
    moteur_ouverture.associer(lecteur_fake2, porte_spy2)

    lecteur_fake1.simuler_detection_badge(badge1)
    lecteur_fake2.simuler_detection_badge(badge2)
    # QUAND le Moteur d'ouverture effectue une interrogation des lecteurs
    moteur_ouverture.interroger()
    # ALORS la première porte est ouverte
    # ET la deuxième porte est ouverte
    assert porte_spy1.porte_ouverte
    assert porte_spy2.porte_ouverte

## Cas badge bloqué
def test_badge_bloque():
    # ETANT DONNE un lecteur ayant détecté un badge
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    badge = Badge()

    moteur_ouverture.associer(lecteur_fake, porte_spy)
    lecteur_fake.simuler_detection_badge(badge)

    # ET que le badge a été bloqué
    moteur_ouverture.bloquer_badge(badge)
    # QUAND le moteur d'ouverture effectue une interrogation du lecteur
    moteur_ouverture.interroger()
    # ALORS la porte n'est pas ouverte
    assert not porte_spy.porte_ouverte

## Cas : un badge non bloque est detecte, la porte est ouverte, puis un autre badge bloque est detecte
def test_porte_est_ouverte_puis_badge_bloque_est_presente():
    # ETANT DONNE un lecteur ayant detecté un badge non bloqué
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    badge1 = Badge()

    moteur_ouverture.associer(lecteur_fake, porte_spy)
    lecteur_fake.simuler_detection_badge(badge1)
    # ET que le moteur d'ouverture a autorisé l'ouverture de la porte une premiere fois
    moteur_ouverture.interroger()
    assert porte_spy.porte_ouverte
    # ET que la porte est refermée
    porte_spy.fermer()
    # QUAND un badge bloqué est ensuite présenté au lecteur
    badge2 = Badge()
    moteur_ouverture.bloquer_badge(badge2)
    lecteur_fake.simuler_detection_badge(badge2)
    moteur_ouverture.interroger()
    # ALORS la porte n'est pas ouverte
    assert not porte_spy.porte_ouverte

## cas test badge bloqué puis débloqué
def test_badge_bloque_puis_debloque():
    # ETANT DONNE un badge bloqué
    badge = Badge()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.bloquer_badge(badge)
    # ET que le badge est ensuite débloqué
    moteur_ouverture.debloquer_badge(badge)
    # QUAND le badge est présenté à un lecteur associé à une porte
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    lecteur_fake.simuler_detection_badge(badge)
    moteur_ouverture.interroger()
    # ALORS la porte est ouverte
    assert porte_spy.porte_ouverte

## cas test un badge est bloque et un autre badge est présenté
def test_badge_bloque_autre_badge_presente_ouvre_porte():
    # ETANT DONNE un badge bloqué
    badge1 = Badge()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.bloquer_badge(badge1)
    # ET un autre badge non bloqué
    badge2 = Badge()
    # QUAND le badge non bloqué est présenté à un lecteur associé à une porte
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    lecteur_fake.simuler_detection_badge(badge2)
    moteur_ouverture.interroger()
    # ALORS la porte est ouverte
    assert porte_spy.porte_ouverte

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
