import pytest
from lecteur_carte import LecteurCarte
from badge import Badge

## Histoire 1 : Accès autorisé à la porte
# **FONCTIONNALITÉ** : Contrôle d'accès par badge
def test_controle_acces_par_badge_acces_autorise():
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

# Histoire 2 :  Accès refusé à la porte (go home, you're not welcome)
# **FONCTIONNALITÉ** : Contrôle d'accès par badge
def test_controle_acces_par_badge_acces_refuse():
# **FONCTIONNALITÉ** : Contrôle d'accès par badge
#   **SCÉNARIO** : Un porteur tente d'accéder à une porte
#   **ÉTANT DONNÉ** un badge avec un identifiant
    badge = Badge()
    badge.identifiant = "123456789"
#   **ET** un lecteur de carte
    lecteur_carte = LecteurCarte()
#   **ET** le lecteur de carte n'est pas configuré pour accepter ce badge, parce qu'on ne l'aime pas
    lecteur_carte.badge_autorise = "987654321"
#   **QUAND** le badge est présenté au lecteur de carte
    lecteur_carte.presenter_badge(badge)
#   **ALORS** l'accès doit être refusé
    assert lecteur_carte.acces_autorise == False #