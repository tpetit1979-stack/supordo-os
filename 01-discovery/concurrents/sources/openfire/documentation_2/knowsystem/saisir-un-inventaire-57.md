---
url: https://documentation.openfire.fr/knowsystem/saisir-un-inventaire-57
url_finale: https://documentation.openfire.fr/knowsystem/saisir-un-inventaire-57
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire permet, via les ajustements de stocks, de saisir les inventaires et ainsi de contrôler et mettre à jour les quantités réelles des articles dans votre entrepôt.

Avant la saisie d'un inventaire, si un suivi de stock est géré en temps réel, il faut bien vérifier que les bons de livraison client et les bons de réception fournisseurs soient validés avant la date concernée.

Il est possible d'effectuer un inventaire physique à tout moment par article ou par catégorie d'article, et par emplacement. Il est possible aussi de choisir de ne pas inclure les quantités nuls dans votre inventaire OpenFire.

## Démarrer un inventaire

Pour saisir l'inventaire, l'accès est "**Inventaire  > Opérations > Ajustement de stock"**, puis cliquer sur Créer :

Avant de démarrer l’inventaire qui est en statut "Brouillon", plusieurs champs sont à définir :

- Référence de l'inventaire correspond au nom de l'inventaire.
- Emplacement Inventorié est l’emplacement de stock défini en amont. Par défaut, il n'existe qu'un emplacement "stock" et tous les articles stockés se retrouvent dans le même emplacement. S'il existe plusieurs emplacements de stocks dans le logiciel (car différents dépôts magasins ou séparation emplacement entre le dépôt et le showroom), il faut __**impérativement**__ saisir un inventaire par emplacement.
- Date d’inventaire est la date et l'heure auxquelles l’ajustement de stock doit être appliquées. Etant donné que les mouvements de stocks sont générés via les bons de livraison client et les bons de réception fournisseur en temps réel, il est important que les mouvements de stocks soient tous validés avant la date de l'inventaire afin de gérer les stocks en temps réel après la date de saisie de l'inventaire.

Les articles se trouvant dans l'emplacement défini en amont peuvent être récupérés dans l'inventaire sur les éléments suivants :

- Tous les articles : le système pré-remplira automatiquement tous les articles avec leur quantité théorique présents dans l'emplacement défini,
- Une catégorie d’article : le système pré-remplira les articles d’une catégorie d’article sélectionnée présents dans l'emplacement défini,
- Un article seulement : un seul article est sélectionné pour faire l'ajustement de cet article qui se trouve dans l'emplacement défini (pour un ajustement d'un article en cours d'année par exemple).
- Sélectionner les produits manuellement : les articles sont à saisir manuellement les uns après les autres (conseillé lors d'un 1er inventaire)
- L’option Inclure les articles épuisés vous permet d’inclure les articles dont la quantité théorique est nulle le jour de la date d'inventaire.

Une fois les paramètres sélectionnés, cliquez sur Démarrer l’inventaire et l'ajustement de stock passe en statut "en cours".

## Saisir et valider l'inventaire

Par défaut, pour chaque ligne d'article, le système mettra la même quantité dans la colonne Quantité théorique et la quantité réelle.

A tout moment de la saisie de la quantité réelle de l'inventaire (statut "en cours"), une sauvegarde peut être effectuée. Les données sont ainsi conservées et l'inventaire peut être saisi en plusieurs fois. L'inventaire ne sera définitif qu'au moment de la validation.

  *Il est conseillé de mettre toute la colonne "Quantité réelle" à zéro avant de commencer le comptage en cliquant sur Mettre les quantités à 0.* 

L'option Créer les lignes manquantes à 0 permet à la fin de saisie d'inventaire, d'insérer les articles en stock (avec une quantité théorique) qui n'ont pas été saisie dans le tableau et des les ajouter avec une quantité réelle à 0.

Le bouton d'action Compiler les lignes permet de fusionner les lignes d’articles qui ont la même référence interne. La quantité sera ainsi cumulée sur une seule ligne d'article.

Code couleur des lignes :

- Ligne noire si la quantité théorique est positive et que la quantité réelle est identique à la quantité théorique

- Ligne bleue si la quantité théorique est positive et que la quantité réelle est différente de la quantité théorique

- Ligne rouge si la quantité théorique est négative.

- __SAISIE DE L'INVENTAIRE__

Il faut saisir la **quantité réelle** des articles dans l'emplacement indiqué dans la colonne "Quantité réelle". 

La **quantité théorique** concerne la quantité qu'OpenFire a calculé à date de l'inventaire en fonction des mouvements de stocks générés.

La **valeur unitaire** reprend par défaut le coût de l'article noté dans la fiche article. 

 **A Savoir:** Cette valeur peut être modifiée dans l'ajustement de stock mais ne modifiera pas le coût de la fiche de l'article ni dans les rapports de valorisation de stock. Cette valeur ne sera utilisée que pour l'affichage du montant du stock de l'inventaire visible en bas de tableau:

Dans **notes,** il est possible de saisir des informations complémentaires sur l'article (exemple : "abîmé",..)

Il est possible d'ajouter des lignes d'articles et / ou de supprimer la lignes au fur et à mesure de la saisie de l'inventaire.

- __VALIDATION DE L'INVENTAIRE__

Quand tous les articles sont saisies dans l'inventaire, avant la validation de l'inventaire :

 - cliquer sur Créer les lignes manquantes à 0 afin d'ajouter les articles non saisies avec une quantité théorique et de les passer en quantité réelle à 0.

 - cliquer sur "COMPILER LES LIGNES" si besoin.

 - cliquer sur "CONTROLER" : ce bouton permet de vérifier que les quantités saisies sont cohérentes :

* pas de quantités négatives

* pas de numéro de série manquant ou de lot avec une quantité différente de 0 ou 1

* pas de numéro de série identique pour 2 articles

* pas de numéro de série identique pour un même article

Après les vérifications faites, cliquer sur Valider l’inventaire : cette action est irréversible : des ajustements de stocks vont ainsi se générer à la date de l'inventaire afin que le stock réel soit mis à jour.

*Plus d'information sur [Valorisation de l'inventaire](https://documentation.openfire.fr/knowsystem/valoriser-les-stocks-191)*