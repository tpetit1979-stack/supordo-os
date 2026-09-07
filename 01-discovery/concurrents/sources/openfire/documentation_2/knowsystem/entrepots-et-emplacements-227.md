---
url: https://documentation.openfire.fr/knowsystem/entrepots-et-emplacements-227
url_finale: https://documentation.openfire.fr/knowsystem/entrepots-et-emplacements-227
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire permet de gérer vos entrepôts et emplacements de stockage de vos marchandises. Ceux-ci sont alors organisés hiérarchiquement.

 La création d'un entrepôt et d'un emplacement nécessite un certains nombre de paramétrages (Routes, séquences, etc...).

Aussi, pour toutes création d'un entrepôt ou d'un emplacement, merci de contacter le support OpenFire par mail à l'adresse support@openfire.fr, ou par téléphone au 02.30.96.02.65.

## Entrepôts

L'entrepôt désigne le bâtiment où sont stockés vos articles. Il est donc possible de gérer plusieurs entrepôts.

Pour accéder à la liste de vos entrepôts, activez le mode développeur. Pour cela,  rendez-vous dans l’onglet Configuration puis cliquez sur l’option Activer le mode développeur à droite :

Rendez-vous ensuite dans le menu Inventaire > Configuration > Entrepôts :

Le champ Adresse permet de définir l'adresse de réception qui apparaitra sur les bons de commande d'achats et les bons de livraisons.

Pour chaque entrepôt il est possible d'adapter le nombre d'étapes de réception et d'expédition.

Généralement, la réception s'effectue en une étape, mais je peux envisager de réceptionner en plusieurs étapes, par exemple pour mettre en place un contrôle qualité, ou pour prendre en compte le fait que je décharge dans une zone avant de mettre en stock:

Attention: La modification de ces options peut nécessiter des routes supplémentaires.

  *Plus d'informations sur [les routes](https://documentation.openfire.fr/knowsystem/routes-et-regles-de-stock-226)*

Vous pouvez également accéder à un certain nombre de paramétrages de gestion depuis le menu **Inventaire > Configuration** **> Configuration** :

- Approvisionnements : permet de réserver automatiquement les produits disponibles lors de la validation d'une commande client.
- Warehouses and Locations usage level : Niveau d'utilisation des entrepôts et des emplacements.
- Routes : Cette option vient compléter l'application de gestion d'entrepôt en mettant en œuvre les flux logistiques poussées et tirés selon les routes.
- Articles : Précision décimale pour le poids.
- Livraison directe : crée la route "expédition directe" et ajoute des tests complexes.
- Vagues de préparation : permet de regrouper les préparations pour en traiter plusieurs à la fois.
- Règles de stock minimum : permet de gérer les règles de stock minimum différemment en prenant en compte le calendrier des achats et des livraisons.

A savoir: OpenFire ajoute automatiquement des couleurs par société ou entrepôt afin de simplifier la lecture du tableau de bord. Il est tout de même possible de modifier les couleurs de chaque encart en cliquant sur le bouton Plus:

  *Plus d'informations sur [le Tableau de bord](https://documentation.openfire.fr/knowsystem/tableau-de-bord-et-generalites-164)*

## Emplacements


Un Emplacement est un espace spécifique dans votre entrepôt (une étagère, un plancher, une allée, etc…). Par conséquent, un emplacement ne peut faire partie que d’un seul entrepôt.

Il existe plusieurs types d'emplacements:

- Les Emplacements Physiques sont des emplacements internes qui font partie des entrepôts que vous possédez.
- Les Emplacements des Partenaires sont des espaces dans l’entrepôt d’un client et/ou d’un fournisseur. L'adresse client sera utilisée en cas de Drop Shipping.
- Les Emplacements Virtuels sont des lieux qui n’existent pas, mais dans lesquels les produits peuvent être placés quand ils ne sont pas encore (ou plus) physiquement dans un stock. Ils sont utilisés lorsque vous voulez placer des articles perdus hors de votre stock (dans la Perte de stock), ou lorsque vous voulez prendre en compte des articles qui sont sur le chemin de votre entrepôt (Approvisionnement).

Pour chaque emplacement, il est possible de définir une stratégie d'enlèvement (FIFO, LIFO, ...):

Des stratégies de rangement peuvent également être définie pour préciser à chaque réception que je stocke telle marchandise à tel emplacement.

A Savoir: le champ Société doit être renseigné au niveau de l'emplacement afin d'éviter d'éventuels erreurs lors de la saisie des inventaires.