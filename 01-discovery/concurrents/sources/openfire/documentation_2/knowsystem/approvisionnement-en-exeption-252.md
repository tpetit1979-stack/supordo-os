---
url: https://documentation.openfire.fr/knowsystem/approvisionnement-en-exeption-252
url_finale: https://documentation.openfire.fr/knowsystem/approvisionnement-en-exeption-252
date_collecte: 2026-09-06
destination: documentation_2
---

Les approvisionnements sont dits en exception lorsqu’ils n’ont pas pu être traités par OpenFire. Cela signifie généralement que les demandes de prix n'ont pu être générée.

## Approvisionnement en exception


            Les approvisionnement en exception sont visibles depuis le menu **Inventaire > Rapports > Approvisionnements en exception** :

Plusieurs raisons d'erreur sont possibles, parmi lesquels :

- Aucun fournisseur n’est défini pour l’article à approvisionner,
- Aucune règles d'approvisionnement n'était défini pour cet article,
- Aucune adresse n’est définie au niveau du fournisseur,
- Aucun entrepôt d’approvisionnement n’est défini, etc...


L'erreur rencontrée est visible en cliquant sur l'approvisionnement en exception, puis en vous rnedant en bas de page dans l'historique de l'approvisionnement:

## Relance de l'approvisionnement en erreur

Lorsque l’anomalie est corrigée, il est possible de relancer l’approvisionnement via les règles de réapprovisionnement.

Il s'agit d'un moteur de calcul basé sur les règles d'approvisionnement et qui est lancé périodiquement sur OpenFire.

Par défaut, il est configuré pour s'exécuter une fois par jour (via une action planifiée), mais il est possible de le lancer manuellement, notamment pour relancer des approvisionnements en exception.

Pour cela, mettez-vous en mode Développeur et rendez-vous dans le menu **Inventaire > Opérations > Lancer les règles de réapprovisionnement** :

En cliquant sur Lancer les règles de réapprovisionnement, les approvisionnements planifiés vont alors être relancés: