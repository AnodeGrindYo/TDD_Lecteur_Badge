import pytest
from lecteur_carte import LecteurCarte
from badge import Badge

## Histoire : Quand un badge est présenté au lecteur de carte, le lecteur de carte détecte la présence du badge
# **FONCTIONNALITÉ** : Detection du badge
def test_detection_badge():
#   **SCÉNARIO** : Un badge est présenté au lecteur de carte
#   **ÉTANT DONNÉ** un badge
    badge = Badge()
#   **ET** un lecteur de carte
    lecteur_carte = LecteurCarte()
#   **QUAND** le badge est présenté au lecteur de carte
    lecteur_carte.presenter_badge(badge)
#   **ALORS** le lecteur de carte doit détecter la présence du badge
    assert lecteur_carte.badge_detecte == True #
