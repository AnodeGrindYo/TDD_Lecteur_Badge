import pytest
from moteur_ouverture import MoteurOuverture
from utilities.porteSpy import PorteSpy
from utilities.lecteurFake import LecteurFake
from badge import Badge

def test_lecteur_flash_vert_si_badge_autorisé():
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
    # ALORS le lecteur émet un flash vert
    assert lecteur_fake.compter_vert() == 1

def test_lecteur_flash_rouge_si_badge_bloque():
    # ETANT DONNE un lecteur associé à une porte
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    # ET un badge bloqué
    badge = Badge()
    moteur_ouverture.bloquer_badge(badge)

    # QUAND le badge est présenté au lecteur
    lecteur_fake.simuler_detection_badge(badge)
    moteur_ouverture.interroger()
    # ALORS le lecteur émet un flash rouge
    assert lecteur_fake.compter_rouge() == 1

def test_lecteur_flash_violet_si_porte_renvoie_exception():
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    # ET que le badge est bloqué
    badge = Badge()
    # ET que la porte renvoie une erreur
    porte_spy.set_exception_code(666)
    # QUAND le badge est présenté au lecteur
    lecteur_fake.simuler_detection_badge(badge)
    moteur_ouverture.interroger()
    # ALORS le lecteur émet un flash violet
    assert lecteur_fake.compter_violet() == 1


def test_lecteur_flash_rouge_si_porte_renvoie_exception_mais_quelqu_un_la_repare_avec_un_grand_coup_de_pied():
    porte_spy = PorteSpy()
    lecteur_fake = LecteurFake()
    moteur_ouverture = MoteurOuverture()
    moteur_ouverture.associer(lecteur_fake, porte_spy)
    # ET que le badge n'est pas bloqué
    badge = Badge()
    # ET que la porte renvoie une exception
    porte_spy.set_exception_code(42)
    # ET que quelqu'un la répare en donnant un grand coup de pied dedans
    porte_spy.set_exception_code(1)
    # QUAND le badge est présenté au lecteur
    lecteur_fake.simuler_detection_badge(badge)
    moteur_ouverture.interroger()
    # ALORS le lecteur émet un flash vert
    assert lecteur_fake.compter_vert() == 1