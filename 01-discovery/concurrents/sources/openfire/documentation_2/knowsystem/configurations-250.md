---
url: https://documentation.openfire.fr/knowsystem/configurations-250
url_finale: https://documentation.openfire.fr/knowsystem/configurations-250
date_collecte: 2026-09-06
destination: documentation_2
---

Pour gérer efficacement le stock dans OpenFire, il est important de configurer correctement les paramètres liés à la gestion du stock.

Vous trouverez ci-dessous les principaux paramétrages à prendre en compte:

- Les emplacements de stockage : Vous pouvez définir les différents emplacements de stockage pour chaque entrepôt afin de savoir où se trouvent les produits dans votre entreprise. Vous pouvez également attribuer un emplacement de stockage par défaut pour chaque produit. Plus d'informations sur [les entrepôts et emplacements](https://documentation.openfire.fr/knowsystem/entrepots-et-emplacements-227)

- Les mouvements de stock : Vous pouvez enregistrer les mouvements de stock (entrées, sorties, transferts, etc.) pour chaque produit enregistré. Vous pouvez également effectuer des ajustements manuels du stock si nécessaire. Plus d'informations sur [les mouvements de Stock](https://documentation.openfire.fr/knowsystem/mouvement-de-stocks-248)

- Les seuils de stock minimum et maximum : Vous pouvez définir les seuils de stock minimum et maximum pour chaque produit afin de générer automatiquement des Ordres d'Approvisionnement lorsque les niveaux de stock tombent en dessous du seuil minimum.  *Plus d'informations sur [les règles de stock](https://documentation.openfire.fr/knowsystem/suivi-des-approvisionnements-247#scrollTop=0)*

- Les ordres d'approvisionnement : Vous pouvez créer des Ordres d'Approvisionnement pour commander des produits auprès de fournisseurs en fonction des seuils de stock minimum et maximum.  *Plus d'informations sur [les ordres d'approvisionnement](https://documentation.openfire.fr/knowsystem/ordre-d-approvisionnement-253)*

- Les inventaires physiques : Vous pouvez effectuer des inventaires physiques réguliers pour vérifier les niveaux de stock réels par rapport aux niveaux théoriques enregistrés dans OpenFire.  *Plus d'informations sur* *[Saisir un inventaire](https://documentation.openfire.fr/knowsystem/saisir-un-inventaire-57)*

## Configuration des Sociétés

Dans le menu Configuration de la société, il est possible de définir quels sont les magasins qui commandent, et quels sont les entrepôts qui réceptionnent les articles.

Ces options sont disponibles en bas de l'onglet Paramètres avancés :

En cas de multi société, il est également possible de définir laquelle est propriétaire du stock:

## Configuration de Routage Avancé

Pour utiliser les routes, activez l'option Routage avancé des articles défini par des règles dans la configuration de l'inventaire:

Cette option permet d'ajouter la possibilité d'ajouter des Routes dans l'onglet Inventaire des fiches Articles.

## Routes spécifiques par ligne de commande

Dans le menu **Ventes > Configuration**, il est possible d'activer l’option Choisir des routes spécifiques à chaque ligne de commande :

Cette option permet de définir la création d'un bon de commande selon les lignes de commandes, par exemple avec l'utilisation d'une Route pour fumisterie et une Route pour les poêles. Deux bons de livraison seront alors créés.

## Configuration de la stratégie d'enlèvement

Vous aurez la possibilité de définir dans règles dans la section Logistique des catégories d'articles. Cette partie permet de définir les routes et aussi les stratégies d'enlèvement.

*Par défaut, OpenFire prend d'abord les stocks les "plus âgés" (FIFO), mais ce comportement peut être modifié en Last In Last Out (LIFO)*