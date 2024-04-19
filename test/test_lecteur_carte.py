import pytest
from src.lecteur_carte import LecteurCarte
from src.badge import Badge

## Histoire 1 : Accès autorisé à la porte
# **FONCTIONNALITÉ** : Contrôle d'accès par badge
def test_controle_acces_par_badge():
# **FONCTIONNALITÉ** : Contrôle d'accès par badge
#   **SCÉNARIO** : Un porteur tente d'accéder à une porte
#   **ÉTANT DONNÉ** un badge avec un identifiant
    badge = Badge()
    badge.identifiant = "123456789"
#   **ET** un lecteur de carte
    lecteur_carte = LecteurCarte()
#   **ET** le lecteur de carte est configuré pour accepter ce badge
    lecteur_carte.badge_autorise = badge.identifiant
#   **QUAND** le badge est présenté au lecteur de carte
    lecteur_carte.presenter_badge(badge)
#   **ALORS** l'accès doit être autorisé
    assert lecteur_carte.acces_autorise == True #

# Histoire 2 :  contr