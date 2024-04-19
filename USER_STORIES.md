# User stories lecteur de badge

## Fonctionnalité 1 : Authentification de l'utilisateur par badge

SCÉNARIO: Authentification valide avec un badge
    ÉTANT DONNÉ un lecteur de badge actif
    ET un badge "<ID_badge>" enregistré dans le système
    QUAND je présente le badge "<ID_badge>" au lecteur
    ALORS l'accès doit être autorisé
    ET un enregistrement de l'accès est créé

    EXEMPLES:
    | ID_badge |
    | 12345678 |
    | 87654321 |

SCÉNARIO: Tentative d'authentification avec un badge non reconnu
    ÉTANT DONNÉ un lecteur de badge actif
    QUAND je présente un badge "99999999", non enregistré dans le système, au lecteur
    ALORS l'accès doit être refusé
    ET un message d'erreur "Badge non reconnu" est affiché


## Fonctionnalité 2 : Gestion des erreurs du lecteur de badge

SCÉNARIO: Présentation d'un badge endommagé
    ÉTANT DONNÉ un lecteur de badge actif
    QUAND je présente un badge endommagé au lecteur
    ALORS l'accès doit être refusé
    ET un message d'erreur "Erreur de lecture du badge, veuillez réessayer" est affiché

SCÉNARIO: Lecteur de badge inactif
    ÉTANT DONNÉ un lecteur de badge qui n'est pas actif
    QUAND je tente d'utiliser le lecteur
    ALORS aucun signal n'est émis par le lecteur
    ET un message "Lecteur inactif, contactez la maintenance" est affiché


SCÉNARIO: Récupération des logs d'accès
    ÉTANT DONNÉ que je suis connecté en tant qu'administrateur
    QUAND je demande à voir les logs d'accès
    ALORS tous les logs des tentatives d'accès doivent être affichés
    ET chaque log doit inclure l'identifiant du badge et le résultat de l'accès
