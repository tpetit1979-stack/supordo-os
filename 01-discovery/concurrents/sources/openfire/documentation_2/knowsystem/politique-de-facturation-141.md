---
url: https://documentation.openfire.fr/knowsystem/politique-de-facturation-141
url_finale: https://documentation.openfire.fr/knowsystem/politique-de-facturation-141
date_collecte: 2026-09-06
destination: documentation_2
---

En fonction de vos politiques commerciales, deux méthodes de facturation sont possibles:

- Facturer sur la base des quantités commandées,
- Facturation sur la base des quantités livrées au client.

## Méthodes de facturation

En fonction de vos politiques commerciales, deux méthodes de facturation sont possibles:

- Facturer sur la base des quantités commandées,
- Facturation sur la base des quantités livrées au client.

Facturation des quantités commandées : 

Cette règle est utilisée par défaut dans OpenFire. Cette politique de facturation signifie que les clients pourront être facturés dès la commande client confirmée, sur la base des quantités du bon de commande.

*La facture étant générée en brouillon, il reste possible de la modifier, pour facturer seulement quelques lignes de facture par exemple, avant de la valider.*

Facturation des quantités livrées :

Cette règle permettra de facturer les clients une fois la livraison effectuée. 

Il peut arriver qu'une livraison soit effectuée en plusieurs fois. Dans ces cas, il est donc préférable de facturer la quantité réellement livrée. Cette règle est a utiliser dans les cas où la quantité peut diverger entre la commande et la livraison. 

Ce mode de facturation a un impact sur le flux des ventes car vous devrez confirmer la quantité livrée avant de créer une facture.

Pour les articles du type « service », les quantités livrées sont gérées manuellement directement depuis la ligne de commande.

Attention: dans le cas où la facturation se fait sur les quantités livrées, seules les quantités effectivement marquées comme « livrées » sur le bon de commande seront facturées.

## Modifier la politique de facturation

Cette configuration peut se faire de façon générale ou de manière plus spécifique.

##### Modification générale:

Si vous souhaitez modifier ce fonction de façon générale, rendez-vous dans la partie Taxes et facturation du menu Ventes > Configuration > Configuration

Dans le cas d’une facturation sur la base des quantités livrées, une nouvelle colonne est ajoutée au niveau des lignes de commande de votre devis :

##### Modification Spécifique:

La politique de facturation peut être définie spécifiquement pour un article ou une catégorie d'article.

Ainsi, chaque ligne d'un bon de commande dispose de sa politique de facturation.

*Si vous avez sur un même bon de commande des fournitures et des prestations de service, les fournitures pourront par exemple être facturées en quantité livrée.*

Depuis un article ou une catégorie d'article, rendez-vous dans l'onglet Facturation, puis sélectionnez le mode voulu dans la partie dédiée:

La politique de facturation peut également être modifiée manuellement sur un devis, en vous rendant dans l'onglet Autres informations :

Attention: ce champ remplace les paramétrages des articles/catégories d'articles, ainsi les politiques de facturation des catégories d'articles ne seront alors plus appliquées.