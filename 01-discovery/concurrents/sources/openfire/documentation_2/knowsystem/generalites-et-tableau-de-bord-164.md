---
url: https://documentation.openfire.fr/knowsystem/generalites-et-tableau-de-bord-164
url_finale: https://documentation.openfire.fr/knowsystem/generalites-et-tableau-de-bord-164
date_collecte: 2026-09-06
destination: documentation_2
---

La gestion des stocks sur OpenFire est liée aux différents autres modules de gestion.  

En effet, à partir d'une commande client, il est possible de générer les bons d'achats et de réception en fonction de différentes règles d'approvisionnements.

Il est par exemple possible de définir un niveau de stock minimum qui, une fois atteint, déclenche le réapprovisionnement.

  Plus d'informations sur le [P](https://documentation.openfire.fr/knowsystem/processus-d-une-commande-d-achat-58)[rocessus d'une commande d'achat](https://documentation.openfire.fr/knowsystem/processus-d-une-commande-d-achat-58)


La configuration de la gestion des stocks est __à réaliser au préalable par la société OpenFire.__

En effet, avant de débuter la gestion des stocks sur OpenFire, différents points à préparer, parmi lesquels il vous faudra définir:

- quels sont vos entrepôts et emplacements de stockage,
- quelle est la procédure de réception des articles que vous souhaitez mettre en place (entrée direct en stock, réception avec contrôle qualité, etc...),
- quelle est la gestion des préparations et des livraisons à mettre en place.

La gestion des stocks est accessible depuis le module **Inventaire** :

## Navigation et tableau de bord

En vous rendant dans l'application Inventaire, vous accéderez au tableau de bord, ainsi qu'aux différents menu de gestion des stocks.

Cette page vous informe en temps réel sur les éléments clés de votre stock, sur les livraisons à effectuer, les produits à recevoir et sur les états d'avancements, ...

Chaque case donne les informations des données à traiter mais aussi de leur état (en attente, en retard ou reliquat).

Par défaut, OpenFire décompose votre magasin en deux types , les réceptions et les livraisons.

Les commandes fournisseurs non reçues seront affichées sur la partie Réception, via le bouton À recevoir :

Les commandes clients non encore livrées seront classées sur la partie livraisons. via le bouton À faire:

Dans le cas où toutes les opérations de stock sont effectuées, vous aurez comme affichage 0 à traiter.

Dans le cas de non achèvement, retards ou reliquats de stock, des indicateurs seront affichés le temps de compléter toutes vos opérations de stock.

A savoir: OpenFire ajoute automatiquement des couleurs par société ou entrepôt  afin de simplifier la lecture du tableau de bord:

Il est tout de même possible de modifier les couleurs de chaque encart en cliquant sur le bouton Plus:

L'application inventaire vous permet également d'accéder à l'ensemble des menus nécessaires à la gestion de vos stocks et de vos approvisionnements.

Le menu Opérations permet d’accéder à tous les mouvements qui peuvent être fait via l’inventaire.

Le menu Articles permet d’avoir une vue sur les articles, leurs variantes et les règles d’approvisionnement.

Le menu Analyse permet d'accéder aux différents reportings (rapport de valorisation d'inventaire, prévision de stock, etc...).

Le menu Configuration donne accès à la configuration des articles, des unités de mesure et des catégories d’unités de mesures, des entrepôts, mais aussi à la configuration générale du module.


## Gestion de stock en "double entrée"

La gestion de stock en double entrée sur OpenFire est une méthode de suivi des stocks qui utilise deux entrées pour enregistrer tout mouvement de stock dans le système.

Cela signifie que pour chaque entrée dans le stock (par exemple, une réception d'achat), il y aura également une sortie correspondante (par exemple, une sortie pour une vente). Cette méthode permet d'avoir une vue précise et à jour de la quantité de stock disponible en tout temps.

Les mouvements de stock représentent le transit de marchandises et de matériels entre des emplacements.

Ainsi, un inventaire sur OpenFire génère des mouvements de stock entre différents emplacements (éventuellement virtuels).

  Plus d'informations sur [les mouvements de Stock](https://documentation.openfire.fr/knowsystem/mouvement-de-stocks-248)

## Configuration des Sociétés

Dans le menu Configuration de la société, il est possible de définir quels sont les magasins qui commandent, et quels sont les entrepôts qui réceptionnent les articles.

Ces options sont disponibles en bas de l'onglet Paramètres avancés :

En cas de multi société, il est également possible de définir laquelle est propriétaire du stock: